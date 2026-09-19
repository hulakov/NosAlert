import re
import unicodedata
from dataclasses import dataclass, field
from .const import LocationType

try:
    from homeassistant.util import slugify as ha_slugify
except ImportError:
    ha_slugify = None

def _slugify_raw(text: str) -> str:
    """Helper for fallback text slugification."""
    if ha_slugify is not None:
        return ha_slugify(text)
        
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    return re.sub(r"[^a-z0-9]+", "_", normalized.lower()).strip("_")

@dataclass
class BaseLocation:
    uid: int
    name: str
    name_en: str
    type: LocationType = field(init=False)
    parent_location_uid: str = field(init=False)
    
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
                return f"місто {clean_name}"
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
