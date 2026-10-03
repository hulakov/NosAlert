from enum import StrEnum
import logging
from typing import Any, TypeVar
import aiohttp

from .location_registry import location_registry
from .models import Alert, AlertLevel, AlertType, Threat, ThreatType

API_ACTIVE_ALERTS_URL = "https://api.alerts.in.ua/v1/alerts/active.json"

_LOGGER = logging.getLogger(__name__)

_E = TypeVar("_E", bound=StrEnum)


def _to_enum(enum_cls: type[_E], value: Any, default: _E) -> _E:
    """Convert a raw API string to enum member, falling back to default for unknown values."""
    try:
        return enum_cls(value)
    except ValueError:
        return default


class AlertsInUaClient:
    """Client for official alerts.in.ua API."""

    def __init__(self, session: aiohttp.ClientSession, api_token: str) -> None:
        """Initialize alerts.in.ua API client."""
        self._session = session
        self.api_token = api_token
        self._last_modified: str | None = None
        self._cached_alerts: list[Alert] = []

    async def fetch_alerts(self) -> list[Alert]:
        """Fetch active alerts with HTTP 304 caching support."""
        headers = {
            "Authorization": f"Bearer {self.api_token}",
        }
        if self._last_modified:
            headers["If-Modified-Since"] = self._last_modified

        async with self._session.get(API_ACTIVE_ALERTS_URL, headers=headers) as response:
            if response.status == 304:
                _LOGGER.debug("alerts.in.ua API returned 304 Not Modified; using cached data")
                return self._cached_alerts

            if response.status == 200:
                if "Last-Modified" in response.headers:
                    self._last_modified = response.headers["Last-Modified"]
                data = await response.json()
                alerts = (self._parse_alert(a) for a in data.get("alerts", []) if isinstance(a, dict))
                self._cached_alerts = [a for a in alerts if a is not None]
                return self._cached_alerts

            _LOGGER.error("alerts.in.ua API HTTP status error: %s", response.status)
            raise aiohttp.ClientResponseError(
                request_info=response.request_info,
                history=response.history,
                status=response.status,
                message=f"HTTP status {response.status}",
            )

    @staticmethod
    def _parse_alert(data: dict[str, Any]) -> Alert | None:
        """Convert raw alerts.in.ua alert JSON to Alert (None if the location is unknown to us)."""
        location = location_registry.find_by_uid(data.get("location_uid", ""))
        if location is None:
            _LOGGER.debug("Skipping alert for unknown location uid %s", data.get("location_uid"))
            return None

        threats = []
        for t in data.get("threats") or []:
            if not isinstance(t, dict):
                continue
            threat_type = _to_enum(ThreatType, t.get("threat_type"), ThreatType.UNKNOWN)
            threats.append(
                Threat(
                    threat_type=threat_type,
                    level=_to_enum(AlertLevel, t.get("level"), AlertLevel.YELLOW),
                    source_message=str(t.get("source_message", "")),
                    started_at=t.get("started_at"),
                )
            )

        return Alert(
            location_id=location.id,
            level=AlertLevel.YELLOW if data.get("alert_level") == "yellow" else AlertLevel.RED,
            type=_to_enum(AlertType, data.get("alert_type"), AlertType.UNKNOWN),
            started_at=data.get("started_at"),
            threats=threats,
        )
