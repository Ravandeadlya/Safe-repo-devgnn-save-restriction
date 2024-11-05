# Safe-repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "")
LOG_GROUP = int(getenv("LOG_GROUP", ""))
FORCESUB = getenv("FORCESUB", "")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # fill this only if you dont want to force your subscriber to login by this they can use the old method of invite link and can extract from public without login
MONGO_DB = getenv("MONGO_DB", "")
