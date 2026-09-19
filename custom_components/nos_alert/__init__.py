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

    if config_entry.version in (1, 2):
        new_data = {**config_entry.data}
        old_locations = new_data.get(CONF_LOCATIONS, [])
        new_locations = []
        
        from .const import slugify_location
        
        for old_loc in old_locations:
            # Both old cyrillic "м. Київ" and old uid "31" can be resolved via slugify_location
            # because slugify_location handles Cyrillic -> English slugs, and we should also
            # handle UID string if it's from version 2. Wait, slugify_location might not handle "31" natively
            # unless "31" is mapped to a slug.
            # Let's import LOCATION_SLUG_MAP to resolve UIDs safely.
            from .const import LOCATION_SLUG_MAP
            
            loc_str = str(old_loc).strip()
            # If it's already a recognized slug, keep it
            if loc_str in LOCATION_SLUG_MAP.values():
                new_locations.append(loc_str)
            # If it's a known key in slug map (e.g. "31" or "м. київ")
            elif loc_str.lower() in LOCATION_SLUG_MAP:
                new_locations.append(LOCATION_SLUG_MAP[loc_str.lower()])
            else:
                # Fallback to general slugification
                new_locations.append(slugify_location(loc_str))
        
        new_data[CONF_LOCATIONS] = new_locations
        hass.config_entries.async_update_entry(config_entry, data=new_data, version=3)

    _LOGGER.info("Migration to version %s successful", config_entry.version)
    return True
