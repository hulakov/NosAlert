"""Sensor platform for NosAlert Home Assistant integration."""

from datetime import datetime
import logging
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import slugify

from .const import CONF_LOCATIONS, DOMAIN
from .coordinator import NosAlertDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up NosAlert sensor entities from config entry."""
    coordinator: NosAlertDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    locations: list[str] = entry.data.get(CONF_LOCATIONS, ["м. Київ"])

    entities: list[SensorEntity] = []

    for loc in locations:
        entities.append(NosAlertColorSensor(coordinator, loc))
        entities.append(NosAlertStartTimeSensor(coordinator, loc))

    async_add_entities(entities)


class NosAlertColorSensor(CoordinatorEntity[NosAlertDataUpdateCoordinator], SensorEntity):
    """Sensor entity representing the alert color status (red, yellow, none)."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: NosAlertDataUpdateCoordinator,
        location: str,
    ) -> None:
        """Initialize the color sensor."""
        super().__init__(coordinator)
        self.location = location
        self._slug = slugify(location)

        self._attr_name = f"Alert Color"
        self._attr_unique_id = f"nos_alert_{self._slug}_color"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"nos_alert_{self._slug}")},
            name=f"NosAlert {location}",
            manufacturer="alerts.in.ua",
            model="Air Raid Alert Regional Monitor",
        )

    @property
    def native_value(self) -> str:
        """Return the state of the sensor (red, yellow, none)."""
        loc_data = self.coordinator.data.get(self.location, {}) if self.coordinator.data else {}
        return loc_data.get("alert_level", "none")

    @property
    def icon(self) -> str:
        """Return dynamic icon based on alert severity."""
        state = self.native_value
        if state == "red":
            return "mdi:shield-alert"
        elif state == "yellow":
            return "mdi:shield-half-full"
        return "mdi:shield-check"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return detailed state attributes including threats array."""
        loc_data = self.coordinator.data.get(self.location, {}) if self.coordinator.data else {}
        return {
            "location_title": self.location,
            "alert_type": loc_data.get("alert_type"),
            "started_at": loc_data.get("started_at"),
            "threats_count": loc_data.get("threats_count", 0),
            "threats": loc_data.get("threats", []),
            "source_messages": loc_data.get("source_messages", []),
        }


class NosAlertStartTimeSensor(CoordinatorEntity[NosAlertDataUpdateCoordinator], SensorEntity):
    """Sensor entity representing the alert start timestamp."""

    _attr_has_entity_name = True
    _attr_device_class = SensorDeviceClass.TIMESTAMP

    def __init__(
        self,
        coordinator: NosAlertDataUpdateCoordinator,
        location: str,
    ) -> None:
        """Initialize the start time sensor."""
        super().__init__(coordinator)
        self.location = location
        self._slug = slugify(location)

        self._attr_name = f"Alert Start Time"
        self._attr_unique_id = f"nos_alert_{self._slug}_start_time"
        self._attr_icon = "mdi:clock-alert-outline"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"nos_alert_{self._slug}")},
            name=f"NosAlert {location}",
            manufacturer="alerts.in.ua",
            model="Air Raid Alert Regional Monitor",
        )

    @property
    def native_value(self) -> datetime | None:
        """Return the start timestamp as datetime object."""
        loc_data = self.coordinator.data.get(self.location, {}) if self.coordinator.data else {}
        started_at = loc_data.get("started_at")
        if not started_at:
            return None
        try:
            return datetime.fromisoformat(str(started_at).replace("Z", "+00:00"))
        except Exception:
            return None
