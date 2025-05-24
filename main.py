import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

if not api_id or not api_hash:
    raise RuntimeError("❌ API_ID або API_HASH не задані!")

with TelegramClient(StringSession(), int(api_id), api_hash) as client:
    print("\n🔐 TELETHON_SESSION:")
    print(client.session.save())
