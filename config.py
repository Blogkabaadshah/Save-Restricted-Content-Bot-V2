# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25680646"))
API_HASH = getenv("API_HASH", "0a403b1d2ac0aa5ba34a2fab2ba6a12b")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6964743059").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Blogkabaadshah:Blogkaking@cluster0.tu29h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002188008502")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002068126730"))
