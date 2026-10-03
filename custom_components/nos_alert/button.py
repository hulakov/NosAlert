"""Button platform for NosAlert Home Assistant integration."""

import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import NosAlertDataUpdateCoordinator
from .location_registry import location_registry
from .models import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up NosAlert button entities from config entry."""
    coordinator: NosAlertDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[ButtonEntity] = []
    for loc in coordinator.locations:
        entities.append(NosAlertRefreshButton(coordinator, loc))

    async_add_entities(entities)


class NosAlertRefreshButton(CoordinatorEntity[NosAlertDataUpdateCoordinator], ButtonEntity):
    """Button to manually or automatically trigger an immediate refresh of NosAlert data."""

    _attr_has_entity_name = True
    _attr_translation_key = "refresh"
    _attr_icon = "mdi:refresh"

    def __init__(
        self,
        coordinator: NosAlertDataUpdateCoordinator,
        location: str,
    ) -> None:
        """Initialize the location-specific refresh button."""
        super().__init__(coordinator)
        self.location = location
        self._slug = location_registry.slugify_location(location)
        display_name = location_registry.get_location_display_name(location)

        self._attr_unique_id = f"nos_alert_{self._slug}_refresh"
        self._attr_suggested_object_id = f"nosalert_{self._slug}_refresh"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"nos_alert_{self._slug}")},
            name=f"NosAlert {display_name}",
            manufacturer="alerts.in.ua",
            model="Air Raid Alert Regional Monitor",
        )

    async def async_press(self) -> None:
        """Handle the button press."""
        _LOGGER.info("Refresh triggered via button for location '%s'", self.location)
        await self.coordinator.async_request_refresh()
