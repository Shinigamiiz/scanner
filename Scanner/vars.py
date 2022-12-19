
import os

que = {}
admins = {}

SESSION_STRING = os.environ.get("SESSION_STRING", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
API_ID = int(os.environ.get("API_ID", 13715737))
API_HASH = os.environ.get("API_HASH", None)
OWNER_ID = (os.environ.get("OWNER_ID", None))
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
UPDATE = os.environ.get("UPDATE", None)
CMD_OP = list(os.environ.get("CMD_OP", "/ . ? !").split())
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", None)

SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
SUDO_USERS.add(OWNER_ID)
SUDO_USERS = list(SUDO_USERS)
GBAN_CHATS = set(int(x) for x in os.environ.get("GBAN_CHATS", "").split())

SESSION_STRING = "BQASEzwjmt8pS4nCNxXvt_Rh5ZmEiLu9Z_W-Zw3swcUFcedaOJPqjneZGtwO-AoqtBJKw_MQbOjQAtprq4RFX_KqC5FHRzmmD52GwLKfiSxvTgFN8KYPJC9dWwZXiUxKJ-_O_ZYHqh3Wxq3dkdeAltbetF-RhkdjE5YGJDHvr6VjaaGXagcCWeZDGIDAlTllhs5uXwtS04rlq4I2OkJf3c6XHb_GzFs0ZzG-lDjaesHqjbGoVWHFiFWtDTfc_u-mEQ7Fqnz5yqyKHzTZNxgkET46pepUSoQoDMzYMq3Wsa8IFAPXciWjQKqW6taxASHaTGdpPXKjmpV5GW5Yh4EeutKdAAAAASqzwtAA"
BOT_TOKEN = "5722220703:AAFZZqkmvrdXXD9zCwsKSbU-AUWGEUVLQDg"
API_ID = "13715737"
API_HASH = "9b5ff18e133fed80f0f6cd7bf30cffdd"
OWNER_ID = "5667156680"
SUPPORT_CHAT = "Chizurubot2"
MONGO_DB_URI = "mongodb+srv://eren:eren@cluster0.aor5rcv.mongodb.net/?retryWrites=true&w=majority"
LOG_CHANNEL_ID = (-1001854008187)
SUDO_USERS = "5667156680"
