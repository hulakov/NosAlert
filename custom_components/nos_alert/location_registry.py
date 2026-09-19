"""Location helper functions and types for NosAlert."""

from typing import Iterator
try:
    from .const import LocationType
    from .models import BaseLocation, Hromada, District, Location, _slugify_raw
except ImportError:
    from const import LocationType
    from models import BaseLocation, Hromada, District, Location, _slugify_raw

class LocationRegistry:
    """Registry encapsulating all administrative locations in Ukraine."""

    def __init__(self, raw_locations: list[Location]):
        self._locations_by_uid: dict[str, BaseLocation] = {}
        for loc in self._iter_all_locations(raw_locations):
            self._locations_by_uid[str(loc.uid)] = loc

    def _iter_all_locations(self, locations: list[Location]) -> Iterator[BaseLocation]:
        """Yield all location objects (oblast, district, hromada) with injected parent UIDs and types."""
        for loc in locations:
            # loc itself is an oblast (or city with special status)
            loc.parent_location_uid = str(loc.uid)
            yield loc
            
            for district in loc.districts:
                district.type = LocationType.RAION
                district.parent_location_uid = str(loc.uid)
                yield district
                
                for hromada in district.hromadas:
                    hromada.type = LocationType.HROMADA
                    hromada.parent_location_uid = str(loc.uid)
                    yield hromada

    def get(self, location_uid: str) -> BaseLocation | None:
        return self._locations_by_uid.get(str(location_uid))

    def resolve_location_uid(self, location_name_or_uid: str) -> str:
        """Resolves any location string (slug, uid, cyrillic, english) to a valid UID."""
        location_str = str(location_name_or_uid).strip()
        if location_str in self._locations_by_uid:
            return location_str
            
        location_lower = location_str.lower()
        
        for location_uid, location_data in self._locations_by_uid.items():
            # Match against slug, display_name, english or cyrillic name
            if location_lower in (
                location_data.slug, 
                location_data.name.lower(), 
                location_data.name_en.lower(),
                location_data.display_name.lower(),
            ):
                return location_uid
                
        return location_str

    def get_location_display_name(self, location_name_or_uid: str) -> str:
        """Get clean human-readable display name for location in Ukrainian (e.g. 'Київ', 'Вінницька область')."""
        location_uid = self.resolve_location_uid(location_name_or_uid)
        if location_uid in self._locations_by_uid:
            return self._locations_by_uid[location_uid].display_name
        # Fallback
        return str(location_name_or_uid).strip()

    def slugify_location(self, location_name_or_uid: str) -> str:
        """Convert location name or UID to a clean, standardized English slug for entity IDs."""
        location_uid = self.resolve_location_uid(location_name_or_uid)
        if location_uid in self._locations_by_uid:
            return self._locations_by_uid[location_uid].slug
        
        location_clean = str(location_name_or_uid).strip()
        return _slugify_raw(location_clean)
        
    @property
    def all_locations(self) -> dict[str, BaseLocation]:
        return self._locations_by_uid

try:
    from .locations_data import LOCATIONS
except ImportError:
    from locations_data import LOCATIONS

# Initialize the singleton registry instance
location_registry = LocationRegistry(LOCATIONS)
