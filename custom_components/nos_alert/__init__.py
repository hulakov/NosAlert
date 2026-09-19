"""The NosAlert Home Assistant integration."""

import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import CONF_API_TOKEN, CONF_LOCATIONS, DOMAIN
from .coordinator import NosAlertDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR, Platform.BINARY_SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up NosAlert from a config entry."""
    api_token: str = entry.data[CONF_API_TOKEN]
    locations: list[str] = entry.data.get(CONF_LOCATIONS, ["м. Київ"])

    coordinator = NosAlertDataUpdateCoordinator(
        hass,
        api_token=api_token,
        locations=locations,
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(update_listener))

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Handle options update."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Migrate old entry."""
    _LOGGER.debug("Migrating from version %s", config_entry.version)

    if config_entry.version == 1:
        new_data = {**config_entry.data}
        old_locations = new_data.get(CONF_LOCATIONS, [])
        new_locations = []
        
        from .const import LOCATION_UID_MAP
        
        for old_loc in old_locations:
            if old_loc.lower() in LOCATION_UID_MAP:
                new_locations.append(LOCATION_UID_MAP[old_loc.lower()])
            else:
                new_locations.append(old_loc)  # Fallback if somehow not found
        
        new_data[CONF_LOCATIONS] = new_locations
        hass.config_entries.async_update_entry(config_entry, data=new_data, version=2)

    _LOGGER.info("Migration to version %s successful", config_entry.version)
    return True
