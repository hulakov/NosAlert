"""Constants for the NosAlert Home Assistant integration."""

DOMAIN = "nos_alert"
DEFAULT_SCAN_INTERVAL = 7  # Scan interval in seconds (respects API soft limit of 8-10 req/min)

CONF_API_TOKEN = "api_token"
CONF_LOCATIONS = "locations"

API_ACTIVE_ALERTS_URL = "https://api.alerts.in.ua/v1/alerts/active.json"

# Mapping of location titles (lowercased) to official Location UIDs
LOCATION_UID_MAP = {
    "хмельницька область": "3",
    "вінницька область": "4",
    "рівненська область": "5",
    "волинська область": "8",
    "дніпропетровська область": "9",
    "житомирська область": "10",
    "закарпатська область": "11",
    "запорізька область": "12",
    "івано-франківська область": "13",
    "київська область": "14",
    "кіровоградська область": "15",
    "луганська область": "16",
    "миколаївська область": "17",
    "одеська область": "18",
    "полтавська область": "19",
    "сумська область": "20",
    "тернопільська область": "21",
    "харківська область": "22",
    "херсонська область": "23",
    "черкаська область": "24",
    "чернігівська область": "25",
    "чернівецька область": "26",
    "львівська область": "27",
    "донецька область": "28",
    "автономна республіка крим": "29",
    "крим": "29",
    "м. севастополь": "30",
    "севастополь": "30",
    "м. київ": "31",
    "київ": "31",
}

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
