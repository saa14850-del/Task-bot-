import os
from dotenv import load_dotenv

load_dotenv()  # local development

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = [int(os.environ.get("ADMIN_ID"))]  # Admin ID integer থাকবেই
GROUP_ID = os.environ.get("GROUP_ID")      # String এর মতো রাখো, যেমন "secrethublink"
