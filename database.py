import json

with open("settings.json", "r", encoding="utf-8") as f:
    settings = json.load(f)

# Warn tracking in memory
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
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)
