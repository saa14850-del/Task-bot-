import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # database.py এর location
SETTINGS_PATH = os.path.join(BASE_DIR, "settings.json")

if not os.path.exists(SETTINGS_PATH):
    raise FileNotFoundError(f"settings.json ফাইল পাওয়া যায়নি! Path: {SETTINGS_PATH}")

with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
    settings = json.load(f)
