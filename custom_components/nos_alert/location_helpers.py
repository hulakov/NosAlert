"""Location helper functions and types for NosAlert."""

import re
import unicodedata
from enum import StrEnum
from typing import Any, NotRequired, TypedDict

try:
    from homeassistant.util import slugify as ha_slugify
except ImportError:
    ha_slugify = None

class LocationType(StrEnum):
    """Types of locations in Ukraine."""
    SPECIAL_CITY = "Місто з спеціальним статусом"
    AUTONOMOUS_REPUBLIC = "Автономна Республіка"
    OBLAST = "Область"
    RAION = "Район"
    HROMADA = "Громада"

class Hromada(TypedDict):
    uid: int
    name: str
    name_en: str

class District(TypedDict):
    uid: int
    name: str
    name_en: str
    hromadas: NotRequired[list[Hromada]]

class Location(TypedDict):
    uid: int
    name: str
    type: LocationType
    name_en: str
    districts: NotRequired[list[District]]

def iter_all_locations():
    """Flatten hierarchical LOCATIONS into individual location dicts (oblast, district, hromada).

    Injects 'type' field based on nesting level for backward compatibility,
    since districts and hromadas don't store 'type' explicitly in the hierarchy.
    """
    try:
        from .locations import LOCATIONS
    except ImportError:
        from locations import LOCATIONS
    for loc in LOCATIONS:
        # loc itself is an oblast (or city with special status)
        yield {**loc, "parent_oblast_uid": loc["uid"]}
        for district in loc.get("districts", []):
            yield {**district, "type": LocationType.RAION, "parent_oblast_uid": loc["uid"]}
            for hromada in district.get("hromadas", []):
                yield {**hromada, "type": LocationType.HROMADA, "parent_oblast_uid": loc["uid"]}

def _slugify_raw(text: str) -> str:
    """Helper for fallback text slugification."""
    if ha_slugify is not None:
        return ha_slugify(text)
        
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    return re.sub(r"[^a-z0-9]+", "_", normalized.lower()).strip("_")

# Build the main map once at module level
LOCATIONS_BY_UID: dict[str, dict[str, Any]] = {}

for _loc in iter_all_locations():
    _uid = str(_loc["uid"])
    _name = _loc["name"]
    _name_en = _loc["name_en"]
    _slug = _slugify_raw(_name_en)
    
    LOCATIONS_BY_UID[_uid] = {
        "uid": _uid,
        "name": _name,
        "name_en": _name_en,
        "slug": _slug,
        "parent_oblast_uid": str(_loc.get("parent_oblast_uid")),
        "display_name": re.sub(r"^м\.\s*", "", _name, flags=re.IGNORECASE).strip(),
        "name_without_m": re.sub(r"^м\.\s*", "", _name, flags=re.IGNORECASE).strip(),
    }

def resolve_location_uid(location_input: str) -> str:
    """Resolves any location string (slug, uid, cyrillic, english) to a valid UID."""
    loc_str = str(location_input).strip()
    if loc_str in LOCATIONS_BY_UID:
        return loc_str
        
    loc_lower = loc_str.lower()
    
    for uid, data in LOCATIONS_BY_UID.items():
        # Match against slug, english, cyrillic, or stripped cyrillic
        if loc_lower in (
            data["slug"], 
            data["name"].lower(), 
            data["name_en"].lower(), 
            data["name_without_m"].lower()
        ):
            return uid
            
    return loc_str

def get_location_display_name(location_input: str) -> str:
    """Get clean human-readable display name for location (e.g. 'Kyiv' instead of 'м. Київ')."""
    uid = resolve_location_uid(location_input)
    if uid in LOCATIONS_BY_UID:
        return LOCATIONS_BY_UID[uid]["display_name"]
    # Fallback
    loc_clean = str(location_input).strip()
    without_m = re.sub(r"^м\.\s*", "", loc_clean, flags=re.IGNORECASE).strip()
    return without_m if without_m else loc_clean

def slugify_location(location: str) -> str:
    """Convert location name or UID to a clean, standardized English slug for entity IDs."""
    uid = resolve_location_uid(location)
    if uid in LOCATIONS_BY_UID:
        return LOCATIONS_BY_UID[uid]["slug"]
    
    loc_clean = str(location).strip()
    without_m = re.sub(r"^м\.\s*", "", loc_clean, flags=re.IGNORECASE).strip()
    return _slugify_raw(without_m if without_m else loc_clean)
