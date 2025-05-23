# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# write up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "27099161")
API_HASH = os.getenv("API_HASH", "4ebbba630c8da1e27875ba399ae78a7f")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7926814511:AAGwnHIZr3Q4E0IBITenetnJ8rcAujXaaaA")
BOT_ID = int(BOT_TOKEN.split(":")[0])  # Extracted Bot ID from BOT_TOKEN
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://modkha7110:modkha7110@cluster0.4jiwjny.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5340147496").split()))  # list separated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None)  # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002690516753"))  # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002616889016"))  # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq")  # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F")  # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "999999999"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "99999999"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/savinvidbot")  # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/username_of_admin")
