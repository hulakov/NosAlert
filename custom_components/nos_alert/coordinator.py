"""DataUpdateCoordinator for NosAlert Home Assistant integration."""

from datetime import timedelta
import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    API_ACTIVE_ALERTS_URL,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    THREAT_DESCRIPTIONS,
)
from .location_helpers import LOCATIONS_BY_UID, resolve_location_uid

_LOGGER = logging.getLogger(__name__)





class NosAlertDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
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
        self._last_modified: str | None = None
        self._cached_alerts_list: list[dict[str, Any]] = []

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from API using aiohttp session with caching support."""
        session = async_get_clientsession(self.hass)
        headers = {
            "Authorization": f"Bearer {self.api_token}",
        }
        if self._last_modified:
            headers["If-Modified-Since"] = self._last_modified

        try:
            async with session.get(API_ACTIVE_ALERTS_URL, headers=headers) as response:
                if response.status == 304:
                    _LOGGER.debug("API returned 304 Not Modified; using cached alerts data")
                elif response.status == 200:
                    if "Last-Modified" in response.headers:
                        self._last_modified = response.headers["Last-Modified"]
                    data = await response.json()
                    self._cached_alerts_list = data.get("alerts", [])
                else:
                    _LOGGER.error("NosAlert API error: HTTP status %s", response.status)
                    raise UpdateFailed(f"HTTP error status {response.status}")
        except Exception as err:
            if not self._cached_alerts_list and not isinstance(err, UpdateFailed):
                raise UpdateFailed(f"Error communicating with NosAlert API: {err}") from err
            _LOGGER.warning("Network error fetching NosAlert API data: %s", err)

        # Parse alerts data for each configured location
        result: dict[str, Any] = {}

        for loc in self.locations:
            loc_uid = resolve_location_uid(loc)

            # Filter alerts for specified location.
            # We use LOCATIONS_BY_UID because the alerts.in.ua API has a bug where
            # `location_oblast_uid` for districts wrongly duplicates the district's own UID.
            target_alerts = [
                a for a in self._cached_alerts_list
                if str(a.get("location_uid", "")) == loc
                or str(a.get("location_uid", "")) == loc_uid
                or str(a.get("location_oblast_uid", "")) == loc_uid
                or (str(a.get("location_uid", "")) in LOCATIONS_BY_UID and LOCATIONS_BY_UID[str(a.get("location_uid", ""))].get("parent_oblast_uid") == loc_uid)
            ]

            if not target_alerts:
                result[loc] = {
                    "alert_level": "none",
                    "is_active": False,
                    "alert_type": None,
                    "started_at": None,
                    "threats_count": 0,
                    "threats": [],
                    "source_messages": [],
                }
                continue

            has_red = any(a.get("alert_level") == "red" for a in target_alerts)
            has_yellow = any(a.get("alert_level") == "yellow" for a in target_alerts)

            if has_red:
                overall_level = "red"
            elif has_yellow:
                overall_level = "yellow"
            else:
                overall_level = "red"

            # Gather earliest started_at timestamp
            start_times = [a.get("started_at") for a in target_alerts if a.get("started_at")]
            earliest_start = min(start_times) if start_times else None

            # Collect detailed threats
            all_threats = []
            source_messages = []
            for alert in target_alerts:
                for threat in alert.get("threats") or []:
                    t_type = threat.get("threat_type", "unknown")
                    t_desc = THREAT_DESCRIPTIONS.get(t_type, f"❓ {t_type}")
                    threat_item = {
                        "threat_type": t_type,
                        "description": t_desc,
                        "level": threat.get("level", "yellow"),
                        "source_message": threat.get("source_message", ""),
                        "started_at": threat.get("started_at"),
                    }
                    all_threats.append(threat_item)
                    if threat.get("source_message"):
                        source_messages.append(threat.get("source_message"))

            result[loc] = {
                "alert_level": overall_level,
                "is_active": True,
                "alert_type": target_alerts[0].get("alert_type", "air_raid"),
                "started_at": earliest_start,
                "threats_count": len(all_threats),
                "threats": all_threats,
                "source_messages": source_messages,
            }

        return result
