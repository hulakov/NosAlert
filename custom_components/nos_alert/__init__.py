"""The NosAlert Home Assistant integration."""

import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .config_flow import CONF_API_TOKEN, CONF_LOCATIONS
from .location_registry import location_registry
from .coordinator import NosAlertDataUpdateCoordinator
from .models import DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR, Platform.BINARY_SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up NosAlert from a config entry."""
    api_token: str = entry.data[CONF_API_TOKEN]
    locations: list[str] = entry.data.get(CONF_LOCATIONS, ["м. Київ"])

    _LOGGER.info("Setting up NosAlert integration for locations: %s", locations)

    coordinator = NosAlertDataUpdateCoordinator(
        hass,
        api_token=api_token,
        locations=locations,
    )

    await coordinator.async_config_entry_first_refresh()

    coordinator.start_ubilling_poller()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(update_listener))

    _LOGGER.info("NosAlert setup completed successfully for locations: %s", locations)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.info("Unloading NosAlert integration entry %s", entry.entry_id)
    coordinator: NosAlertDataUpdateCoordinator | None = hass.data.get(DOMAIN, {}).get(entry.entry_id)
    if coordinator:
        coordinator.stop_ubilling_poller()

    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Handle options update."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Migrate old entry."""
    _LOGGER.debug("Migrating from version %s", config_entry.version)

    if config_entry.version in (1, 2):
        new_data = {**config_entry.data}
        old_locations = new_data.get(CONF_LOCATIONS, [])
        new_locations = []
        
        for old_val in old_locations:
            loc = location_registry.find(old_val)
            new_locations.append(loc.slug if loc else old_val)
        
        new_data[CONF_LOCATIONS] = new_locations
        hass.config_entries.async_update_entry(config_entry, data=new_data, version=3)

    _LOGGER.info("Migration to version %s successful", config_entry.version)
    return True
