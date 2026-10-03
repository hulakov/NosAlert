import asyncio
from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .alerts_in_ua_api import AlertsInUaClient
from .ubilling_api import UbillingAlertsClient, UBILLING_SCAN_INTERVAL
from .location_registry import location_registry
from .models import DOMAIN, Alert, AlertLevel, LocationAlertStatus, Threat

DEFAULT_SCAN_INTERVAL = 10  # Scan interval in seconds for alerts.in.ua API (respects soft limit of 8-10 req/min)

_LOGGER = logging.getLogger(__name__)


class NosAlertDataUpdateCoordinator(DataUpdateCoordinator[dict[str, LocationAlertStatus]]):
    """Class to manage fetching NosAlert data from official API."""

    def __init__(
        self,
        hass: HomeAssistant,
        api_token: str,
        locations: list[str],
    ) -> None:
        """Initialize the coordinator."""
        self.api_token = api_token
        self.locations = locations
        self._cached_alerts: list[Alert] = []

        session = async_get_clientsession(hass)
        self.alerts_client = AlertsInUaClient(session, api_token)
        self.ubilling_client = UbillingAlertsClient(session)

        # Fast trigger poller state tracking
        self._ubilling_active_ids: set[int] | None = None
        self._ubilling_poller_task: asyncio.Task[None] | None = None

        # Local ids of monitored locations and of the oblasts containing them
        self._relevant_ids: set[int] = set()
        for loc in locations:
            location = location_registry.find(loc)
            if location:
                self._relevant_ids.update((location.id, location.parent_id))

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )

    async def _async_update_data(self) -> dict[str, LocationAlertStatus]:
        """Fetch alerts from alerts.in.ua and aggregate them per configured location."""
        try:
            self._cached_alerts = await self.alerts_client.fetch_alerts()
        except Exception as err:
            if not self._cached_alerts:
                raise UpdateFailed(f"Error communicating with NosAlert API: {err}") from err
            _LOGGER.warning("Network error fetching NosAlert API data: %s", err)

        new_data = {loc: self._build_status(loc) for loc in self.locations}
        self._log_status_changes(new_data)
        return new_data

    def _log_status_changes(self, new_data: dict[str, LocationAlertStatus]) -> None:
        """Log significant alert, severity, threat, or affected regions changes."""
        if not self.data:
            for loc, status in new_data.items():
                if status.is_active:
                    threat_names = [t.description for t in status.threats]
                    _LOGGER.info(
                        "Initial alert status for '%s': ACTIVE (level=%s, threats=%d: %s)",
                        loc,
                        status.alert_level.value,
                        status.threats_count,
                        threat_names or "none",
                    )
                else:
                    _LOGGER.debug("Initial alert status for '%s': SAFE (no active alerts)", loc)
            return

        for loc, new_status in new_data.items():
            old_status = self.data.get(loc)
            if old_status is None:
                continue

            # 1. Alert activation or deactivation
            if new_status.is_active != old_status.is_active:
                if new_status.is_active:
                    threat_names = [t.description for t in new_status.threats]
                    _LOGGER.info(
                        "🚨 ALERT ACTIVATED for '%s'! Level: %s, Threats (%d): %s",
                        loc,
                        new_status.alert_level.value,
                        new_status.threats_count,
                        threat_names or "none",
                    )
                else:
                    _LOGGER.info("🟢 ALERT CLEARED for '%s'! Status is now SAFE", loc)
                continue

            # If still active, check for changes in severity, threats, or affected regions
            if new_status.is_active:
                # 2. Severity level change (e.g. Yellow <-> Red)
                if new_status.alert_level != old_status.alert_level:
                    _LOGGER.info(
                        "⚠️ Severity level changed for '%s': %s -> %s",
                        loc,
                        old_status.alert_level.value,
                        new_status.alert_level.value,
                    )

                # 3. Threats list change
                old_threats = [t.threat_type for t in old_status.threats]
                new_threats = [t.threat_type for t in new_status.threats]
                if old_threats != new_threats:
                    new_threat_names = [t.description for t in new_status.threats]
                    _LOGGER.info(
                        "🛡️ Threats updated for '%s' (%d active): %s",
                        loc,
                        new_status.threats_count,
                        new_threat_names or "none",
                    )

                # 4. Affected regions change
                if new_status.affected_locations != old_status.affected_locations:
                    _LOGGER.info(
                        "📍 Affected regions updated for '%s': %s",
                        loc,
                        ", ".join(new_status.affected_locations) or "none",
                    )

    def _build_status(self, loc: str) -> LocationAlertStatus:
        """Aggregate cached alerts for a single configured location."""
        monitored = location_registry.find(loc)
        if monitored is None:
            return LocationAlertStatus(location=loc)

        alerts = [
            a for a in self._cached_alerts
            if a.location_id == monitored.id
            or location_registry.get(a.location_id).parent_id == monitored.id
        ]
        if not alerts:
            return LocationAlertStatus(location=loc)

        if any(a.level == AlertLevel.RED for a in alerts):
            level = AlertLevel.RED
        elif any(a.level == AlertLevel.YELLOW for a in alerts):
            level = AlertLevel.YELLOW
        else:
            level = AlertLevel.RED

        start_times = [a.started_at for a in alerts if a.started_at]

        threats: list[Threat] = [t for a in alerts for t in a.threats]
        source_messages = [t.source_message for t in threats if t.source_message]

        affected_locations: list[str] = []
        for alert in alerts:
            alert_loc = location_registry.get(alert.location_id)
            circle = "🔴" if alert.level == AlertLevel.RED else "🟡"
            # No space between circle and name to guarantee they stay together
            loc_display = f"{circle}{alert_loc.name}"
            if loc_display not in affected_locations:
                affected_locations.append(loc_display)
        affected_locations.sort(key=lambda x: x.lstrip("🔴🟡 \xa0"))

        return LocationAlertStatus(
            location=loc,
            alert_level=level,
            is_active=True,
            alert_type=alerts[0].type,
            started_at=min(start_times) if start_times else None,
            threats=threats,
            source_messages=source_messages,
            affected_locations=affected_locations,
        )

    def start_ubilling_poller(self) -> None:
        """Start the fast Ubilling polling background task."""
        if self._ubilling_poller_task is None or self._ubilling_poller_task.done():
            self._ubilling_poller_task = self.hass.async_create_background_task(
                self._async_ubilling_poller_loop(),
                name=f"{DOMAIN}_ubilling_poller",
            )
            _LOGGER.debug("Started Ubilling fast trigger poller task")

    def stop_ubilling_poller(self) -> None:
        """Stop the fast Ubilling polling background task."""
        if self._ubilling_poller_task and not self._ubilling_poller_task.done():
            self._ubilling_poller_task.cancel()
            self._ubilling_poller_task = None
            _LOGGER.debug("Stopped Ubilling fast trigger poller task")

    async def _async_ubilling_poller_loop(self) -> None:
        """Poll Ubilling every 2s and force an alerts.in.ua refresh when relevant alert state changes."""
        while True:
            try:
                await asyncio.sleep(UBILLING_SCAN_INTERVAL)
                alerts = await self.ubilling_client.fetch_alerts()
                active_ids = {a.location_id for a in alerts} & self._relevant_ids

                if self._ubilling_active_ids is not None and active_ids != self._ubilling_active_ids:
                    added_ids = active_ids - self._ubilling_active_ids
                    removed_ids = self._ubilling_active_ids - active_ids

                    added_names = [
                        location_registry.get(i).display_name
                        for i in added_ids if location_registry.get(i)
                    ]
                    removed_names = [
                        location_registry.get(i).display_name
                        for i in removed_ids if location_registry.get(i)
                    ]

                    changes = []
                    if added_names:
                        changes.append(f"started in {added_names}")
                    if removed_names:
                        changes.append(f"cleared in {removed_names}")

                    _LOGGER.info(
                        "⚡ Ubilling fast trigger detected alert state change (%s). Requesting immediate alerts.in.ua refresh!",
                        ", ".join(changes) if changes else f"{sorted(self._ubilling_active_ids)} -> {sorted(active_ids)}",
                    )
                    await self.async_request_refresh()
                self._ubilling_active_ids = active_ids
            except asyncio.CancelledError:
                break
            except Exception as err:
                _LOGGER.debug("Ubilling fast trigger poller error: %s", err)
