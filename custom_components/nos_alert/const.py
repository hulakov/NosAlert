from enum import StrEnum

DOMAIN = "nos_alert"
DEFAULT_SCAN_INTERVAL = 10  # Scan interval in seconds (respects API soft limit of 8-10 req/min)

class LocationType(StrEnum):
    """Types of locations in Ukraine."""
    SPECIAL_CITY = "Місто з спеціальним статусом"
    AUTONOMOUS_REPUBLIC = "Автономна Республіка"
    OBLAST = "Область"
    RAION = "Район"
    HROMADA = "Громада"


CONF_API_TOKEN = "api_token"
CONF_LOCATIONS = "locations"

API_ACTIVE_ALERTS_URL = "https://api.alerts.in.ua/v1/alerts/active.json"

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
