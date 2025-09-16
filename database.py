import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.join(BASE_DIR, "settings.json")

if not os.path.exists(SETTINGS_PATH):
    raise FileNotFoundError(f"settings.json ফাইল পাওয়া যায়নি! Path: {SETTINGS_PATH}")

with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
    settings = json.load(f)

warns = {}  # {chat_id: {user_id: count}}

def get_welcome():
    return settings.get("welcome_message")

def get_rules():
    return settings.get("rules_message")

def get_warn_limit():
    return settings.get("warn_limit", 3)

def is_locked(feature):
    return settings.get("locks", {}).get(feature, "off") == "on"

def get_custom_response(command):
    return settings.get("custom_commands", {}).get(command.lower())

def save_settings():
    with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)
