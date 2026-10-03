"""Binary sensor platform for NosAlert Home Assistant integration."""

import logging
from typing import Any

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import slugify

from .location_registry import location_registry
from .coordinator import NosAlertDataUpdateCoordinator
from .models import DOMAIN, LocationAlertStatus

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up NosAlert binary sensor entities from config entry."""
    coordinator: NosAlertDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[BinarySensorEntity] = []

    for loc in coordinator.locations:
        entities.append(NosAlertBinarySensor(coordinator, loc))

    async_add_entities(entities)


class NosAlertBinarySensor(CoordinatorEntity[NosAlertDataUpdateCoordinator], BinarySensorEntity):
    """Binary sensor entity representing overall air raid alert state (ON = Alert Active)."""

    _attr_has_entity_name = True
    _attr_translation_key = "air_raid_alert"
    _attr_device_class = BinarySensorDeviceClass.SAFETY

    def __init__(
        self,
        coordinator: NosAlertDataUpdateCoordinator,
        location: str,
    ) -> None:
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self.location = location
        self._slug = location_registry.slugify_location(location)
        display_name = location_registry.get_location_display_name(location)

        self._attr_unique_id = f"nos_alert_{self._slug}_alert"
        self._attr_suggested_object_id = f"nosalert_{self._slug}_alert"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"nos_alert_{self._slug}")},
            name=f"NosAlert {display_name}",
            manufacturer="alerts.in.ua",
            model="Air Raid Alert Regional Monitor",
        )

    @property
    def is_on(self) -> bool:
        """Return True if an alert (red or yellow) is active."""
        return self._status.is_active

    @property
    def _status(self) -> LocationAlertStatus:
        if self.coordinator.data and self.location in self.coordinator.data:
            return self.coordinator.data[self.location]
        return LocationAlertStatus(location=self.location)

    @property
    def icon(self) -> str:
        """Return dynamic bell icon based on alert state."""
        return "mdi:bell-ring-outline" if self.is_on else "mdi:bell-outline"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return extra attributes."""
        status = self._status
        return {
            "location_title": self.location,
            "alert_level": status.alert_level.value,
            "threats_count": status.threats_count,
            "icon_color": "red" if self.is_on else "green",
        }

