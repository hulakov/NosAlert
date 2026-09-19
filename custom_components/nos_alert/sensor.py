"""Sensor platform for NosAlert Home Assistant integration."""

from datetime import datetime
import logging
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import slugify

from .const import CONF_LOCATIONS, DOMAIN
from .location_helpers import (
    get_location_display_name,
    slugify_location,
)
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
        entities.append(NosAlertThreatsSensor(coordinator, loc))
        entities.append(NosAlertAffectedRegionsSensor(coordinator, loc))
        entities.append(NosAlertStartTimeSensor(coordinator, loc))

    async_add_entities(entities)


class NosAlertColorSensor(CoordinatorEntity[NosAlertDataUpdateCoordinator], SensorEntity):
    """Sensor entity representing the alert color level (red, yellow, none)."""

    _attr_has_entity_name = True
    _attr_translation_key = "alert_color"
    _attr_device_class = SensorDeviceClass.ENUM
    _attr_options = ["none", "yellow", "red"]

    def __init__(
        self,
        coordinator: NosAlertDataUpdateCoordinator,
        location: str,
    ) -> None:
        """Initialize the color sensor."""
        super().__init__(coordinator)
        self.location = location
        self._slug = slugify_location(location)
        display_name = get_location_display_name(location)

        self._attr_unique_id = f"nos_alert_{self._slug}_color"
        self._attr_suggested_object = f"nosalert_{self._slug}_color"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"nos_alert_{self._slug}")},
            name=f"NosAlert {display_name}",
            manufacturer="alerts.in.ua",
            model="Air Raid Alert Regional Monitor",
        )

    @property
    def native_value(self) -> str:
        """Return the state option of the sensor (red, yellow, none)."""
        loc_data = self.coordinator.data.get(self.location, {}) if self.coordinator.data else {}
        return loc_data.get("alert_level", "none")

    @property
    def icon(self) -> str:
        """Return dynamic icon based on alert severity."""
        state = self.native_value
        if state == "red":
            return "mdi:shield-alert"
        elif state == "yellow":
            return "mdi:shield-alert-outline"
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


class NosAlertThreatsSensor(CoordinatorEntity[NosAlertDataUpdateCoordinator], SensorEntity):
    """Sensor entity displaying active threats list in human readable format."""

    _attr_has_entity_name = True
    _attr_translation_key = "active_threats"
    _attr_icon = "mdi:radar"

    def __init__(
        self,
        coordinator: NosAlertDataUpdateCoordinator,
        location: str,
    ) -> None:
        """Initialize the threats summary sensor."""
        super().__init__(coordinator)
        self.location = location
        self._slug = slugify_location(location)
        display_name = get_location_display_name(location)

        self._attr_unique_id = f"nos_alert_{self._slug}_active_threats"
        self._attr_suggested_object = f"nosalert_{self._slug}_active_threats"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"nos_alert_{self._slug}")},
            name=f"NosAlert {display_name}",
            manufacturer="alerts.in.ua",
            model="Air Raid Alert Regional Monitor",
        )

    @property
    def native_value(self) -> str:
        """Return human readable active threats string."""
        loc_data = self.coordinator.data.get(self.location, {}) if self.coordinator.data else {}
        if not loc_data.get("is_active"):
            return "Відсутні"

        threats = loc_data.get("threats", [])
        if threats:
            descs = list(dict.fromkeys([t.get("description") for t in threats if t.get("description")]))
            if descs:
                return ", ".join(descs)

        return "Повітряна тривога"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return active threats details."""
        loc_data = self.coordinator.data.get(self.location, {}) if self.coordinator.data else {}
        threats = loc_data.get("threats", [])
        return {
            "threats_count": len(threats),
            "threats_list": [t.get("description") for t in threats if t.get("description")],
            "source_messages": loc_data.get("source_messages", []),
            "threats_detail": threats,
        }


class NosAlertStartTimeSensor(CoordinatorEntity[NosAlertDataUpdateCoordinator], SensorEntity):
    """Sensor entity representing the alert start timestamp."""

    _attr_has_entity_name = True
    _attr_translation_key = "alert_start_time"
    _attr_device_class = SensorDeviceClass.TIMESTAMP

    def __init__(
        self,
        coordinator: NosAlertDataUpdateCoordinator,
        location: str,
    ) -> None:
        """Initialize the start time sensor."""
        super().__init__(coordinator)
        self.location = location
        self._slug = slugify_location(location)
        display_name = get_location_display_name(location)

        self._attr_unique_id = f"nos_alert_{self._slug}_start_time"
        self._attr_suggested_object = f"nosalert_{self._slug}_start_time"
        self._attr_icon = "mdi:clock-alert-outline"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"nos_alert_{self._slug}")},
            name=f"NosAlert {display_name}",
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


class NosAlertAffectedRegionsSensor(CoordinatorEntity[NosAlertDataUpdateCoordinator], SensorEntity):
    """Sensor returning a readable string of affected regions within the monitored area."""

    _attr_has_entity_name = True
    _attr_translation_key = "affected_regions"
    _attr_icon = "mdi:map-marker-multiple-outline"

    def __init__(
        self,
        coordinator: NosAlertDataUpdateCoordinator,
        location: str,
    ) -> None:
        """Initialize the affected regions sensor."""
        super().__init__(coordinator)
        self.location = location
        self._slug = slugify_location(location)
        display_name = get_location_display_name(location)

        self._attr_unique_id = f"nos_alert_{self._slug}_affected_regions"
        self._attr_suggested_object = f"nosalert_{self._slug}_affected_regions"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"nos_alert_{self._slug}")},
            name=f"NosAlert {display_name}",
            manufacturer="alerts.in.ua",
            model="Air Raid Alert Regional Monitor",
        )

    @property
    def native_value(self) -> str:
        """Return human readable affected regions string."""
        loc_data = self.coordinator.data.get(self.location, {}) if self.coordinator.data else {}
        if not loc_data.get("is_active"):
            return "Відсутні"

        affected = loc_data.get("affected_locations", [])
        if affected:
            # Join with newlines
            val = "\n".join(affected)
            # Home Assistant states have a 255 char limit
            if len(val) > 255:
                return val[:252] + "..."
            return val

        return "Вся область"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return full list of affected regions in attributes to bypass 255 char limit."""
        loc_data = self.coordinator.data.get(self.location, {}) if self.coordinator.data else {}
        return {
            "regions": loc_data.get("affected_locations", [])
        }
