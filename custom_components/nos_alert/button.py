"""Button platform for NosAlert Home Assistant integration."""

import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import NosAlertDataUpdateCoordinator
from .models import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up NosAlert button entities from config entry."""
    coordinator: NosAlertDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([NosAlertRefreshButton(coordinator, entry)])


class NosAlertRefreshButton(CoordinatorEntity[NosAlertDataUpdateCoordinator], ButtonEntity):
    """Button to manually or automatically trigger an immediate refresh of NosAlert data."""

    _attr_translation_key = "refresh"
    _attr_icon = "mdi:refresh"

    def __init__(
        self,
        coordinator: NosAlertDataUpdateCoordinator,
        entry: ConfigEntry,
    ) -> None:
        """Initialize the single global refresh button."""
        super().__init__(coordinator)
        self.entry = entry

        self._attr_unique_id = f"nos_alert_{entry.entry_id}_refresh"
        self._attr_suggested_object = "nosalert_refresh"
        self._attr_name = "NosAlert Refresh"

    async def async_press(self) -> None:
        """Handle the button press."""
        _LOGGER.info("Refresh triggered via button.nosalert_refresh")
        await self.coordinator.async_request_refresh()
