# NosAlert - Ukraine Air Raid Alerts CLI 🚨

Python CLI tool to check **active (red and yellow)** and **historical air raid alerts** in Ukraine using the official [alerts.in.ua API](https://devs.alerts.in.ua/#documentationgetting_started).

📖 **Official API Documentation:** [devs.alerts.in.ua](https://devs.alerts.in.ua/#documentationgetting_started)

---

## 🚀 Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure your API token in the **[.env](.env)** file (see template in **[.env.example](.env.example)**):
```env
ALERTS_TOKEN=YOUR_REAL_TOKEN_HERE
```

---

## 🖥 Usage

### 1. Check current active alerts (default: Kyiv / UID 31)
```bash
python cli/main.py
```

### 2. Check active alerts by Location Name or Location UID
```bash
# Using location name:
python cli/main.py -l "Чернігівська область"

# Using location UID (25 = Chernihiv, 17 = Mykolaiv, 31 = Kyiv):
python cli/main.py -l 25
```

### 3. Fetch alert history for the past month (by Name or UID)
```bash
# Fetch history for Kyiv (UID 31):
python cli/main.py -H -l 31 -n 5

# Fetch history for Lviv region:
python cli/main.py -H -l "Львівська область" -n 5
```

### 4. Enable verbose debugging mode (prints raw HTTP requests and API JSON payload)
```bash
python cli/main.py -v -l 17
```

---

## 📋 CLI Arguments (`python cli/main.py --help`)

| Argument | Long Option | Default | Description |
|---|---|---|---|
| `-l` | `--location` | `"м. Київ"` | Location title or numeric Location UID (e.g., `31`, `25`, `17`). |
| `-H` | `--history` | `False` | Switch to fetch historical alert data instead of active alerts. |
| `-n` | `--limit` | `10` | Number of history records to display. |
| `-p` | `--period` | `"month_ago"` | Period for alert history (`month_ago`). |
| `-v` | `--verbose` | `False` | Enable verbose logging of raw HTTP API requests and response JSON. |
