import os
from dotenv import load_dotenv

load_dotenv()  # Local development only

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = [int(os.environ.get("ADMIN_ID"))]

GROUP_ID = os.environ.get("GROUP_ID")  # string-compatible, numeric ID বা link/username
if not GROUP_ID:
    raise ValueError("GROUP_ID environment variable set নেই!")
