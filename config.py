#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "14050586")
API_HASH = os.environ.get("API_HASH", "42a60d9c657b106370c79bb0a8ac560c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8171526481:AAFOVH76GFAQNl-4gf3VvRRh0yLPF9QthH8")
ADMIN = int(os.environ.get("ADMIN", '5446367898'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "Animes_India_bots_support_group")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "Animes_India_bots_support_group")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Krishna:krishna@cluster0.ecime.mongodb.net/")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002173560131')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://graph.org/file/bd91761f6e938e2e6d23a.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '5446367898'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002145984196)
