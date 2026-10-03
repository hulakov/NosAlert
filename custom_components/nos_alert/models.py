"""Data models for NosAlert Home Assistant integration."""

from dataclasses import dataclass, field
from enum import StrEnum
import re
import unicodedata

try:
    from homeassistant.util import slugify as ha_slugify
except ImportError:
    ha_slugify = None


DOMAIN = "nos_alert"


class LocationType(StrEnum):
    """Types of locations in Ukraine."""
    SPECIAL_CITY = "Місто з спеціальним статусом"
    AUTONOMOUS_REPUBLIC = "Автономна Республіка"
    OBLAST = "Область"
    RAION = "Район"
    HROMADA = "Громада"


class AlertLevel(StrEnum):
    """Alert severity level (also used for per-threat level)."""
    NONE = "none"
    YELLOW = "yellow"
    RED = "red"


class AlertType(StrEnum):
    """Kinds of alerts reported by alerts.in.ua."""
    AIR_RAID = "air_raid"
    CHEMICAL = "chemical"
    RADIATION = "radiation"
    ARTILLERY_SHELLING = "artillery_shelling"
    URBAN_FIGHTS = "urban_fights"
    UNKNOWN = "unknown"


class ThreatType(StrEnum):
    """Specific threat kinds reported by alerts.in.ua."""
    TACTIC_AIRCRAFT_ACTIVITY = "tactic_aircraft_activity"
    STRATEGIC_AIRCRAFT_ACTIVITY = "strategic_aircraft_activity"
    MIG31K_DEPARTURE = "mig31k_departure"
    BALLISTIC_MISSILES = "ballistic_missiles"
    CRUISE_MISSILES = "cruise_missiles"
    UNSPECIFIED_MISSILES = "unspecified_missiles"
    DRONES = "drones"
    GUIDED_AERIAL_BOMBS = "guided_aerial_bombs"
    AIR_DEFENSE = "air_defense"
    UNKNOWN = "unknown"


# Mapping of threat types to human-readable Ukrainian descriptions
THREAT_DESCRIPTIONS: dict[ThreatType, str] = {
    ThreatType.TACTIC_AIRCRAFT_ACTIVITY: "✈️ Активність тактичної авіації",
    ThreatType.STRATEGIC_AIRCRAFT_ACTIVITY: "🛫 Зліт стратегічної авіації",
    ThreatType.MIG31K_DEPARTURE: "🚀 Зліт МіГ-31К (загроза 'Кинджал')",
    ThreatType.BALLISTIC_MISSILES: "💥 Загроза балістичного озброєння",
    ThreatType.CRUISE_MISSILES: "🚀 Загроза крилатих ракет",
    ThreatType.UNSPECIFIED_MISSILES: "🚀 Ракета в напрямку локації",
    ThreatType.DRONES: "🛸 БпЛА / Дрони (Шахеди)",
    ThreatType.GUIDED_AERIAL_BOMBS: "💣 Загроза КАБ/ФАБ",
    ThreatType.AIR_DEFENSE: "🛡️ Робота ППО",
    ThreatType.UNKNOWN: "❓ Невизначена загроза",
}


def _slugify_raw(text: str) -> str:
    """Helper for fallback text slugification."""
    if ha_slugify is not None:
        return ha_slugify(text)

    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    return re.sub(r"[^a-z0-9]+", "_", normalized.lower()).strip("_")


@dataclass
class BaseLocation:
    """Base class for administrative locations in Ukraine."""
    uid: int  # alerts.in.ua location uid (external, used only inside the API layer)
    name: str
    name_en: str
    type: LocationType = field(init=False)
    id: int = field(init=False)  # local id: ordinal number in LocationRegistry
    parent_id: int = field(init=False)  # local id of the containing oblast / special city

    @property
    def display_name(self) -> str:
        """Format location name with appropriate prefixes/suffixes for display."""
        clean_name = self.name.strip()
        match self.type:
            case LocationType.OBLAST:
                return f"{clean_name} область"
            case LocationType.AUTONOMOUS_REPUBLIC:
                return f"Автономна Республіка {clean_name}"
            case LocationType.SPECIAL_CITY:
                return clean_name
            case _:
                return clean_name

    @property
    def slug(self) -> str:
        """Generate slug with legacy suffixes for backward compatibility."""
        slug = _slugify_raw(self.name_en)
        match self.type:
            case LocationType.OBLAST:
                slug += "_oblast"
            case LocationType.RAION:
                slug += "_raion"
            case LocationType.HROMADA:
                slug += "_hromada"
            case LocationType.AUTONOMOUS_REPUBLIC:
                slug = f"autonomous_republic_of_{slug}"
        return slug


@dataclass
class Hromada(BaseLocation):
    pass


@dataclass
class District(BaseLocation):
    hromadas: list[Hromada] = field(default_factory=list)


@dataclass
class Location(BaseLocation):
    type: LocationType
    districts: list[District] = field(default_factory=list)


@dataclass
class Threat:
    """Specific threat within an alert (drones, ballistic missiles, etc.)."""
    threat_type: ThreatType
    description: str = ""
    level: AlertLevel = AlertLevel.YELLOW
    source_message: str = ""
    started_at: str | None = None

    def __post_init__(self) -> None:
        if not self.description:
            self.description = THREAT_DESCRIPTIONS.get(self.threat_type, "❓ Невизначена загроза")


@dataclass
class Alert:
    """Single active alert. Both alert APIs return a list of these."""
    location_id: int  # local id from LocationRegistry
    level: AlertLevel = AlertLevel.RED
    type: AlertType = AlertType.AIR_RAID
    started_at: str | None = None
    threats: list[Threat] = field(default_factory=list)


@dataclass
class LocationAlertStatus:
    """Aggregated alert status for a monitored location."""
    location: str
    alert_level: AlertLevel = AlertLevel.NONE
    is_active: bool = False
    alert_type: AlertType | None = None
    started_at: str | None = None
    threats: list[Threat] = field(default_factory=list)
    source_messages: list[str] = field(default_factory=list)
    affected_locations: list[str] = field(default_factory=list)

    @property
    def threats_count(self) -> int:
        return len(self.threats)
