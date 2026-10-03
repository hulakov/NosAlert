"""Location helper functions and types for NosAlert."""

from typing import Iterator

from .locations_data import LOCATIONS
from .models import BaseLocation, Location, LocationType, _slugify_raw


class LocationRegistry:
    """Registry encapsulating all administrative locations in Ukraine.

    Every location gets a local `id` equal to its ordinal number in the registry.
    API clients match their own identifiers to these ids, so the rest of the
    integration never deals with provider-specific uids.
    """

    def __init__(self, raw_locations: list[Location]):
        self._locations: list[BaseLocation] = []
        self._by_uid: dict[str, BaseLocation] = {}
        for loc in self._iter_all_locations(raw_locations):
            loc.id = len(self._locations)
            self._locations.append(loc)
            self._by_uid[str(loc.uid)] = loc

        # Parents are always registered before their children, so ids are known by now.
        for oblast in raw_locations:
            oblast.parent_id = oblast.id
            for district in oblast.districts:
                district.parent_id = oblast.id
                for hromada in district.hromadas:
                    hromada.parent_id = oblast.id

    def _iter_all_locations(self, locations: list[Location]) -> Iterator[BaseLocation]:
        """Yield all location objects (oblast, district, hromada) with injected types."""
        for loc in locations:
            yield loc
            for district in loc.districts:
                district.type = LocationType.RAION
                yield district
                for hromada in district.hromadas:
                    hromada.type = LocationType.HROMADA
                    yield hromada

    def get(self, location_id: int) -> BaseLocation | None:
        """Get location by local id."""
        if 0 <= location_id < len(self._locations):
            return self._locations[location_id]
        return None

    def find_by_uid(self, uid: str | int) -> BaseLocation | None:
        """Get location by external alerts.in.ua uid."""
        return self._by_uid.get(str(uid))

    def find(self, name_or_uid: str) -> BaseLocation | None:
        """Find a location by uid, slug, or Ukrainian/English name (optionally prefixed with 'м.')."""
        text = str(name_or_uid).strip()
        if text in self._by_uid:
            return self._by_uid[text]

        text = text.lower()
        if text.startswith("м."):
            text = text[2:].strip()

        for loc in self._locations:
            if text in (loc.slug, loc.name.lower(), loc.name_en.lower(), loc.display_name.lower()):
                return loc
        return None

    def get_location_display_name(self, name_or_uid: str) -> str:
        """Get clean human-readable display name for location in Ukrainian (e.g. 'місто Київ', 'Вінницька область')."""
        loc = self.find(name_or_uid)
        return loc.display_name if loc else str(name_or_uid).strip()

    def slugify_location(self, name_or_uid: str) -> str:
        """Convert location name or UID to a clean, standardized English slug for entity IDs."""
        loc = self.find(name_or_uid)
        return loc.slug if loc else _slugify_raw(str(name_or_uid).strip())

    @property
    def all_locations(self) -> list[BaseLocation]:
        return self._locations


# Initialize the singleton registry instance
location_registry = LocationRegistry(LOCATIONS)

