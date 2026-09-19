"""Constants for the NosAlert Home Assistant integration."""

import re
from typing import Any

try:
    from .locations import LOCATIONS, LocationType
except ImportError:
    from locations import LOCATIONS, LocationType

DOMAIN = "nos_alert"
DEFAULT_SCAN_INTERVAL = 7  # Scan interval in seconds (respects API soft limit of 8-10 req/min)

CONF_API_TOKEN = "api_token"
CONF_LOCATIONS = "locations"

API_ACTIVE_ALERTS_URL = "https://api.alerts.in.ua/v1/alerts/active.json"

def iter_all_locations():
    """Flatten hierarchical LOCATIONS into individual location dicts (oblast, district, hromada).

    Injects 'type' field based on nesting level for backward compatibility,
    since districts and hromadas don't store 'type' explicitly in the hierarchy.
    """
    for loc in LOCATIONS:
        yield loc  # has 'type' field (Область / Місто з спеціальним статусом)
        for district in loc.get("districts", []):
            yield {**district, "type": LocationType.RAION}
            for hromada in district.get("hromadas", []):
                yield {**hromada, "type": LocationType.HROMADA}




# Mapping of threat types to human-readable Ukrainian descriptions
THREAT_DESCRIPTIONS = {
    "tactic_aircraft_activity": "✈️ Активність тактичної авіації",
    "strategic_aircraft_activity": "🛫 Зліт стратегічної авіації",
    "mig31k_departure": "🚀 Зліт МіГ-31К (загроза 'Кинджал')",
    "ballistic_missiles": "💥 Загроза балістичного озброєння",
    "cruise_missiles": "🚀 Загроза крилатих ракет",
    "unspecified_missiles": "🚀 Ракета в напрямку локації",
    "drones": "🛸 БпЛА / Дрони (Шахеди)",
    "guided_aerial_bombs": "💣 Загроза КАБ/ФАБ",
    "air_defense": "🛡️ Робота ППО",
    "unknown": "❓ Невизначена загроза",
}

# --- Dynamic dictionary construction from official LOCATIONS database ---

LOCATIONS_BY_UID: dict[str, Any] = {str(loc["uid"]): loc for loc in iter_all_locations()}

LOCATION_UID_MAP: dict[str, str] = {}
LOCATION_SLUG_MAP: dict[str, str] = {}
LOCATION_DISPLAY_NAME_MAP: dict[str, str] = {}


def _slugify_raw(text: str) -> str:
    """Helper for fallback text slugification."""
    try:
        from homeassistant.util import slugify as ha_slugify
        return ha_slugify(text)
    except ImportError:
        import unicodedata
        normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
        return re.sub(r"[^a-z0-9]+", "_", normalized.lower()).strip("_")


for _loc in iter_all_locations():
    _uid = str(_loc["uid"])
    _name = _loc["name"]
    _name_en = _loc["name_en"]
    _ltype = _loc["type"]

    # 1. UID mapping
    LOCATION_UID_MAP[_uid] = _uid
    LOCATION_UID_MAP[_name.lower()] = _uid
    LOCATION_UID_MAP[_name_en.lower()] = _uid

    # 2. Slug mapping
    _slug = _slugify_raw(_name_en)
    LOCATION_SLUG_MAP[_uid] = _slug
    LOCATION_SLUG_MAP[_name.lower()] = _slug
    LOCATION_SLUG_MAP[_name_en.lower()] = _slug

    # 3. Display name mapping (always English as requested)
    _display = _name_en
    LOCATION_DISPLAY_NAME_MAP[_uid] = _display
    LOCATION_DISPLAY_NAME_MAP[_name.lower()] = _display
    LOCATION_DISPLAY_NAME_MAP[_name_en.lower()] = _display

    # Handle "м. " / "м." stripped titles (e.g. "київ" -> "31")
    _without_m = re.sub(r"^м\.\s*", "", _name, flags=re.IGNORECASE).strip()
    if _without_m:
        LOCATION_UID_MAP[_without_m.lower()] = _uid
        LOCATION_SLUG_MAP[_without_m.lower()] = _slug
        LOCATION_DISPLAY_NAME_MAP[_without_m.lower()] = _display

# Extra shorthand aliases
LOCATION_UID_MAP["крим"] = "29"
LOCATION_SLUG_MAP["крим"] = "crimea"
LOCATION_DISPLAY_NAME_MAP["крим"] = "Crimea"


def slugify_location(location: str) -> str:
    """Convert location name or UID to a clean, standardized English slug for entity IDs."""
    loc_clean = str(location).strip()
    loc_lower = loc_clean.lower()

    if loc_lower in LOCATION_SLUG_MAP:
        return LOCATION_SLUG_MAP[loc_lower]

    without_m = re.sub(r"^м\.\s*", "", loc_clean, flags=re.IGNORECASE).strip()
    if without_m.lower() in LOCATION_SLUG_MAP:
        return LOCATION_SLUG_MAP[without_m.lower()]

    return _slugify_raw(without_m if without_m else loc_clean)


def get_location_display_name(location: str) -> str:
    """Get clean human-readable display name for location (e.g. 'Kyiv' instead of 'м. Київ')."""
    loc_clean = str(location).strip()
    loc_lower = loc_clean.lower()

    if loc_lower in LOCATION_DISPLAY_NAME_MAP:
        return LOCATION_DISPLAY_NAME_MAP[loc_lower]

    without_m = re.sub(r"^м\.\s*", "", loc_clean, flags=re.IGNORECASE).strip()
    if without_m.lower() in LOCATION_DISPLAY_NAME_MAP:
        return LOCATION_DISPLAY_NAME_MAP[without_m.lower()]

    return without_m if without_m else loc_clean
