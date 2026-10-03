"""API client for fast Ubilling Aerial Alerts API."""

import logging
import aiohttp

from .location_registry import location_registry
from .models import Alert

API_UBILLING_ALERTS_URL = "https://ubilling.net.ua/aerialalerts/"
UBILLING_SCAN_INTERVAL = 2  # Scan interval in seconds for fast trigger Ubilling API

_LOGGER = logging.getLogger(__name__)


class UbillingAlertsClient:
    """Client for fast Ubilling Aerial Alerts API."""

    def __init__(self, session: aiohttp.ClientSession) -> None:
        """Initialize Ubilling API client."""
        self._session = session

    async def fetch_alerts(self) -> list[Alert]:
        """Fetch active region-level alerts (one Alert per region with an active alert).

        Ubilling only reports whether a region has an alert, so the alerts carry
        no threat details and use the default level/type.
        """
        async with self._session.get(
            API_UBILLING_ALERTS_URL,
            timeout=aiohttp.ClientTimeout(total=4),
        ) as response:
            if response.status != 200:
                _LOGGER.debug("Ubilling API returned HTTP status %s", response.status)
                return []

            data = await response.json()

        alerts = []
        for region_name, info in data.get("states", {}).items():
            if not isinstance(info, dict) or not info.get("alertnow"):
                continue
            location = location_registry.find(region_name)
            if location is None:
                _LOGGER.debug("Skipping Ubilling alert for unknown region %s", region_name)
                continue
            alerts.append(Alert(location_id=location.id))
        return alerts
