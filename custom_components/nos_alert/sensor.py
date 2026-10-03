"""Sensor platform for NosAlert Home Assistant integration."""

from dataclasses import asdict
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

from .location_registry import location_registry
from .coordinator import NosAlertDataUpdateCoordinator
from .models import DOMAIN, AlertLevel, LocationAlertStatus

_LOGGER = logging.getLogger(__name__)


def _status(coordinator: NosAlertDataUpdateCoordinator, location: str) -> LocationAlertStatus:
    """Return current alert status for a location (empty status if no data yet)."""
    if coordinator.data and location in coordinator.data:
        return coordinator.data[location]
    return LocationAlertStatus(location=location)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up NosAlert sensor entities from config entry."""
    coordinator: NosAlertDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[SensorEntity] = []

    for loc in coordinator.locations:
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
    _attr_options = [AlertLevel.NONE.value, AlertLevel.YELLOW.value, AlertLevel.RED.value]

    def __init__(
        self,
        coordinator: NosAlertDataUpdateCoordinator,
        location: str,
    ) -> None:
        """Initialize the color sensor."""
        super().__init__(coordinator)
        self.location = location
        self._slug = location_registry.slugify_location(location)
        display_name = location_registry.get_location_display_name(location)

        self._attr_unique_id = f"nos_alert_{self._slug}_color"
        self._attr_suggested_object_id = f"nosalert_{self._slug}_color"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"nos_alert_{self._slug}")},
            name=f"NosAlert {display_name}",
            manufacturer="alerts.in.ua",
            model="Air Raid Alert Regional Monitor",
        )

    @property
    def native_value(self) -> str:
        """Return the state option of the sensor (red, yellow, none)."""
        return _status(self.coordinator, self.location).alert_level.value

    @property
    def icon(self) -> str:
        """Return dynamic icon based on alert severity."""
        state = self.native_value
        if state == AlertLevel.RED:
            return "mdi:shield-alert"
        elif state == AlertLevel.YELLOW:
            return "mdi:shield-alert-outline"
        return "mdi:shield-check"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return detailed state attributes including threats array."""
        status = _status(self.coordinator, self.location)
        state = self.native_value
        if state == AlertLevel.RED:
            icon_color = "red"
        elif state == AlertLevel.YELLOW:
            icon_color = "amber"
        else:
            icon_color = "green"

        return {
            "location_title": self.location,
            "alert_type": status.alert_type.value if status.alert_type else None,
            "started_at": status.started_at,
            "threats_count": status.threats_count,
            "threats": [asdict(t) for t in status.threats],
            "source_messages": status.source_messages,
            "icon_color": icon_color,
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
        self._slug = location_registry.slugify_location(location)
        display_name = location_registry.get_location_display_name(location)

        self._attr_unique_id = f"nos_alert_{self._slug}_active_threats"
        self._attr_suggested_object_id = f"nosalert_{self._slug}_active_threats"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"nos_alert_{self._slug}")},
            name=f"NosAlert {display_name}",
            manufacturer="alerts.in.ua",
            model="Air Raid Alert Regional Monitor",
        )

    @property
    def native_value(self) -> str:
        """Return human readable active threats string."""
        status = _status(self.coordinator, self.location)
        if not status.is_active:
            return "Відсутні"

        descs = list(dict.fromkeys(t.description for t in status.threats if t.description))
        if descs:
            return ", ".join(descs)

        return "Повітряна тривога"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return active threats details."""
        status = _status(self.coordinator, self.location)
        return {
            "threats_count": status.threats_count,
            "threats_list": [t.description for t in status.threats if t.description],
            "source_messages": status.source_messages,
            "threats_detail": [asdict(t) for t in status.threats],
            "icon_color": "red" if status.is_active else "green",
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
        self._slug = location_registry.slugify_location(location)
        display_name = location_registry.get_location_display_name(location)

        self._attr_unique_id = f"nos_alert_{self._slug}_start_time"
        self._attr_suggested_object_id = f"nosalert_{self._slug}_start_time"
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
        started_at = _status(self.coordinator, self.location).started_at
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
        self._slug = location_registry.slugify_location(location)
        display_name = location_registry.get_location_display_name(location)

        self._attr_unique_id = f"nos_alert_{self._slug}_affected_regions"
        self._attr_suggested_object_id = f"nosalert_{self._slug}_affected_regions"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, f"nos_alert_{self._slug}")},
            name=f"NosAlert {display_name}",
            manufacturer="alerts.in.ua",
            model="Air Raid Alert Regional Monitor",
        )

    @property
    def native_value(self) -> str:
        """Return human readable affected regions string."""
        status = _status(self.coordinator, self.location)
        if not status.is_active:
            return "Відсутні"

        affected = status.affected_locations
        if affected:
            # Join with comma and space
            val = ", ".join(affected)
            # Home Assistant states have a 255 char limit
            if len(val) > 255:
                return val[:252] + "..."
            return val

        return "Вся область"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return full list of affected regions in attributes to bypass 255 char limit."""
        return {
            "regions": _status(self.coordinator, self.location).affected_locations
        }
