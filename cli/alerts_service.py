import json
import logging
import time
import urllib.request
from datetime import datetime

import os
import sys

# Ensure custom_components/nos_alert directory is in path to import constants without HA dependencies
_const_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "custom_components", "nos_alert"))
if _const_dir not in sys.path:
    sys.path.insert(0, _const_dir)

from const import THREAT_DESCRIPTIONS
from location_helpers import LOCATIONS_BY_UID, resolve_location_uid





def fetch_api_json(url: str, token: str):
    """Fetches JSON directly from the alerts.in.ua REST API."""
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def format_level_badge(alert_level: str) -> str:
    """Formats the alert severity level (red / yellow) directly from API alert_level field."""
    if alert_level == "red":
        return "🔴 ЧЕРВОНИЙ (Повітряна тривога / Загальна небезпека)"
    elif alert_level == "yellow":
        return "🟡 ЖОВТИЙ (Підвищена загроза / Часткова небезпека)"
    return f"⚪ {str(alert_level).upper()}"


def format_duration(started_at, finished_at) -> str:
    """Calculates and formats the alert duration in Ukrainian for console display."""
    if not started_at or not finished_at:
        return "триває / не вказано"
    try:
        s_dt = datetime.fromisoformat(str(started_at).replace("Z", "+00:00")) if isinstance(started_at, str) else started_at
        f_dt = datetime.fromisoformat(str(finished_at).replace("Z", "+00:00")) if isinstance(finished_at, str) else finished_at
        
        diff_seconds = int((f_dt - s_dt).total_seconds())
        if diff_seconds < 0:
            return "не вказано"
        
        minutes = diff_seconds // 60
        hours = minutes // 60
        rem_minutes = minutes % 60
        
        if hours > 0:
            return f"{hours} год {rem_minutes} хв"
        return f"{minutes} хв"
    except Exception:
        return "не вказано"


def check_active_alerts(api_token: str, location: str, verbose: bool = False):
    """Fetches and displays current active alerts (red and yellow) directly from the API."""
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    print("\n" + "=" * 60)
    print(f" 📍 Перевірка активних тривог для: {location}")
    print(f" ⏰ Час перевірки: {current_time}")
    print("=" * 60)

    try:
        url = "https://api.alerts.in.ua/v1/alerts/active.json"
        raw_data = fetch_api_json(url, api_token)
        alerts_list = raw_data.get("alerts", [])

        target_uid = resolve_location_uid(location)

        # Filter alerts for specified location.
        # We use LOCATIONS_BY_UID because the alerts.in.ua API has a bug where
        # `location_oblast_uid` for districts wrongly duplicates the district's own UID.
        target_alerts = [
            a for a in alerts_list
            if str(a.get("location_uid", "")) == location
            or str(a.get("location_uid", "")) == target_uid
            or str(a.get("location_oblast_uid", "")) == target_uid
            or (str(a.get("location_uid", "")) in LOCATIONS_BY_UID and LOCATIONS_BY_UID[str(a.get("location_uid", ""))].get("parent_oblast_uid") == target_uid)
        ]

        if verbose:
            print("\n" + "🐛 [VERBOSE DEBUG LOG]".center(60, "-"))
            print(f"📡 HTTP Request Endpoint: {url}")
            print(f"📦 Raw API Response Payload (Всього активних тривог в Україні: {len(alerts_list)}):")
            print(json.dumps(alerts_list, indent=2, ensure_ascii=False, default=str))
            print(f"\n🎯 Filtered Alerts for Location '{location}' (UID: {target_uid}, {len(target_alerts)} items):")
            print(json.dumps(target_alerts, indent=2, ensure_ascii=False, default=str))
            print("-" * 60 + "\n")

        if not target_alerts:
            print(f" ✅ У локації '{location}' НЕМАЄ активних тривог (ані червоних, ані жовтих).")
            print("=" * 60 + "\n")
            return

        has_red = any(a.get("alert_level") == "red" for a in target_alerts)
        has_yellow = any(a.get("alert_level") == "yellow" for a in target_alerts)

        if has_red and has_yellow:
            print(" 🚨 ЗАГАЛЬНИЙ СТАТУС: ЧЕРВОНИЙ ТА ЖОВТИЙ (Комплексна небезпека)")
        elif has_red:
            print(" 🔴 ЗАГАЛЬНИЙ СТАТУС: ЧЕРВОНИЙ (Повітряна тривога / Висока небезпека)")
        elif has_yellow:
            print(" 🟡 ЗАГАЛЬНИЙ СТАТУС: ЖОВТИЙ (Підвищена загроза / Часткова небезпека)")
        print("-" * 60)

        for alert in target_alerts:
            loc_title = alert.get("location_title", location)
            alert_type = alert.get("alert_type", "air_raid")
            started_at = alert.get("started_at", "—")
            raw_level = alert.get("alert_level", "red")
            badge = format_level_badge(raw_level)

            print(f"\n 📍 Локація: {loc_title}")
            print(f" 🚨 СТАТУС ТРИВОГИ: {badge}")
            print(f" 📌 Тип тривоги: {alert_type}")
            print(f" ⏱️ Початок: {started_at}")

            threats = alert.get("threats") or []
            if threats:
                print("\n 🔍 Активні деталізовані загрози:")
                for threat in threats:
                    t_type = threat.get("threat_type", "unknown")
                    t_level = threat.get("level", "yellow")
                    t_msg = threat.get("source_message", "")
                    
                    type_str = THREAT_DESCRIPTIONS.get(t_type, f"❓ {t_type}")
                    level_icon = "🔴" if t_level == "red" else "🟡"
                    
                    msg_str = f" ({t_msg})" if t_msg else ""
                    print(f"   {level_icon} {type_str}{msg_str}")
            else:
                print(" ℹ️ Додаткових конкретизованих загроз не вказано.")

        print("\n" + "=" * 60 + "\n")

    except Exception as e:
        print(f"❌ Помилка під час отримання активних даних: {e}")


def check_alerts_history(api_token: str, location: str, period: str = "month_ago", limit: int = 10, verbose: bool = False):
    """Fetches and displays alert history for the specified period directly from the API."""
    print("\n" + "=" * 60)
    print(f" 📜 Історія тривог для: {location} (Період: {period})")
    print(f" ⚠️ Зверніть увагу: ліміт запитів історії — 2 запити на хвилину.")
    print("=" * 60)

    try:
        target_uid = resolve_location_uid(location)
        url = f"https://api.alerts.in.ua/v1/regions/{target_uid}/alerts/{period}.json"
        raw_data = fetch_api_json(url, api_token)
        alerts_list = raw_data.get("alerts", [])

        if verbose:
            print("\n" + "🐛 [VERBOSE DEBUG LOG]".center(60, "-"))
            print(f"📡 HTTP Request Endpoint: {url}")
            print(f"📦 Raw JSON Response Payload ({len(alerts_list)} items total):")
            print(json.dumps(alerts_list[:limit], indent=2, ensure_ascii=False, default=str))
            print("-" * 60 + "\n")

        if not alerts_list:
            print(f" ℹ️ Історія тривог для '{location}' порожня або відсутня.")
            print("=" * 60 + "\n")
            return

        total_count = len(alerts_list)
        show_count = min(limit, total_count)
        print(f"\n 📊 Всього записів за період: {total_count} (показано {show_count}):\n")

        for idx, alert in enumerate(alerts_list[:limit], 1):
            alert_id = alert.get("id", "—")
            loc_title = alert.get("location_title", location)
            started_at = alert.get("started_at", "—")
            finished_at = alert.get("finished_at")
            alert_type = alert.get("alert_type", "air_raid")
            notes = alert.get("notes", "")

            duration_str = format_duration(started_at, finished_at)
            finished_display = finished_at if finished_at else "триває / не вказано"
            notes_str = f" | Примітка: {notes}" if notes else ""

            print(f" {idx:2d}. [ID {alert_id}] {loc_title}")
            print(f"     ⏱️ Початок:    {started_at}")
            print(f"     🏁 Завершення: {finished_display}")
            print(f"     ⏳ Тривалість: {duration_str}")
            print(f"     📌 Тип:        {alert_type}{notes_str}")
            print("     " + "-" * 50)

        print("\n" + "=" * 60 + "\n")

    except Exception as e:
        print(f"❌ Помилка під час завантаження історії: {e}")


def monitor_alerts(api_token: str, location: str, interval: int = 10, verbose: bool = False):
    """Monitors live alert status for a given location, printing updates whenever the state changes."""
    target_uid = resolve_location_uid(location)

    print("\n" + "=" * 65)
    print(f" 👀 РЕЖИМ МОНІТОРИНГУ ТРИВОГ ДЛЯ: {location}")
    print(f" ⏱️ Інтервал перевірки: кожні {interval} сек. (Натисніть Ctrl+C для виходу)")
    print("=" * 65)

    previous_state = None

    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            url = "https://api.alerts.in.ua/v1/alerts/active.json"

            try:
                raw_data = fetch_api_json(url, api_token)
                alerts_list = raw_data.get("alerts", [])
            except Exception as req_err:
                print(f" ⚠️ [{current_time}] Помилка з'єднання з API: {req_err}")
                time.sleep(interval)
                continue

            target_uid = resolve_location_uid(location)

            # Filter alerts for specified location.
            # We use LOCATIONS_BY_UID because the alerts.in.ua API has a bug where
            # `location_oblast_uid` for districts wrongly duplicates the district's own UID.
            target_alerts = [
                a for a in alerts_list
                if str(a.get("location_uid", "")) == location
                or str(a.get("location_uid", "")) == target_uid
                or str(a.get("location_oblast_uid", "")) == target_uid
                or (str(a.get("location_uid", "")) in LOCATIONS_BY_UID and LOCATIONS_BY_UID[str(a.get("location_uid", ""))].get("parent_oblast_uid") == target_uid)
            ]

            current_state = {}
            for a in target_alerts:
                a_id = a.get("id")
                current_state[a_id] = {
                    "location_title": a.get("location_title"),
                    "alert_level": a.get("alert_level", "red"),
                    "alert_type": a.get("alert_type", "air_raid"),
                    "started_at": a.get("started_at"),
                    "threats": a.get("threats") or [],
                }

            if previous_state is None:
                if not current_state:
                    print(f" [{current_time}] ✅ У локації '{location}' НЕМАЄ активних тривог. Моніторинг активний...")
                else:
                    print(f" [{current_time}] 🚨 ВИЯВЛЕНО АКТИВНІ ТРИВОГИ:")
                    for a_id, item in current_state.items():
                        badge = format_level_badge(item["alert_level"])
                        print(f"   • {item['location_title']} | {badge} | Початок: {item['started_at']}")
                        if item["threats"]:
                            for t in item["threats"]:
                                icon = "🔴" if t.get("level") == "red" else "🟡"
                                desc = THREAT_DESCRIPTIONS.get(t.get("threat_type"), f"❓ {t.get('threat_type')}")
                                msg = f" ({t.get('source_message')})" if t.get("source_message") else ""
                                print(f"     {icon} {desc}{msg}")
                previous_state = current_state
            else:
                if current_state != previous_state:
                    new_alert_ids = set(current_state.keys()) - set(previous_state.keys())
                    finished_alert_ids = set(previous_state.keys()) - set(current_state.keys())
                    updated_alert_ids = set(current_state.keys()) & set(previous_state.keys())

                    print(f"\n🔔 [{current_time}] ⚡ ЗМІНА СТАТУСУ ТРИВОГИ:")

                    for a_id in finished_alert_ids:
                        old_item = previous_state[a_id]
                        print(f"   🟢 ВІДБІЙ ТРИВОГИ! -> {old_item['location_title']} (ID: {a_id})")

                    for a_id in new_alert_ids:
                        new_item = current_state[a_id]
                        badge = format_level_badge(new_item["alert_level"])
                        print(f"   🚨 ОГОЛОШЕНО ТРИВОГУ! -> {new_item['location_title']} | {badge}")
                        if new_item["threats"]:
                            for t in new_item["threats"]:
                                icon = "🔴" if t.get("level") == "red" else "🟡"
                                desc = THREAT_DESCRIPTIONS.get(t.get("threat_type"), f"❓ {t.get('threat_type')}")
                                msg = f" ({t.get('source_message')})" if t.get("source_message") else ""
                                print(f"     {icon} {desc}{msg}")

                    for a_id in updated_alert_ids:
                        if current_state[a_id] != previous_state[a_id]:
                            item = current_state[a_id]
                            badge = format_level_badge(item["alert_level"])
                            print(f"   🔄 ОНОВЛЕННЯ ЗАТРОЗ -> {item['location_title']} | {badge}")
                            if item["threats"]:
                                for t in item["threats"]:
                                    icon = "🔴" if t.get("level") == "red" else "🟡"
                                    desc = THREAT_DESCRIPTIONS.get(t.get("threat_type"), f"❓ {t.get('threat_type')}")
                                    msg = f" ({t.get('source_message')})" if t.get("source_message") else ""
                                    print(f"     {icon} {desc}{msg}")

                    if not current_state:
                        print(f"   ✅ Усі тривоги скасовано. У локації '{location}' спокійно.")

                    print("-" * 65)
                    previous_state = current_state

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n\n👋 Моніторинг зупинено користувачем. Бережіть себе!\n")
