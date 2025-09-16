import os
from dotenv import load_dotenv

load_dotenv()  # Local development only

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = [int(os.environ.get("ADMIN_ID"))]

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable set নেই!")
if not ADMINS:
    raise ValueError("ADMIN_ID environment variable set নেই!")
