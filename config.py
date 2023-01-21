from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "11888980"))
API_HASH = getenv("API_HASH", "a041669ed71104ef5a6e00234b3bd2f6")
BOT_TOKEN = getenv("BOT_TOKEN", "5449841253:AAEkKQL-oreIvz-TkVxUgVbANvqoBAZs20E")
SESSION_NAME = getenv("SESSION_NAME", "AgBGOJB4nkUw5_ytZC4I0gUiz383LrfDo_4j-HI2-e4LJFU2OC-ajk4EtASWoAMJwmxKo805sGDlpjyOySQD8meH3YyfQyWuPPD8MegfJabGxG-wmHYt_tUHJKNBqavS8NIB1MzKa33dl8bMzkOx4ujTHqQh5bXmwsYopZM3KYQLag9neoWB-IJ-bqp-0AMMbfPy-HIX3N0zRXZrk0NrNl0IFjyQyRFh-FB8igoEFQsRXIVTyPU3jXQUMnJkTX_-_nHGtYQc49ZCctzgQDKTIbyqaeAr_C1tLJ8uz-omnAqyi-mn2cBYtIX2PFStLwhBvCpQXcF0Ou4_jithFAdWAIqmAAAAAUACQ44A")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "O_Q_M")
ALIVE_NAME = getenv("ALIVE_NAME", "Kasul")
BOT_USERNAME = getenv("BOT_USERNAME", "Music_Spider_BBot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CQQQV")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LZZZ6")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "840551801").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5814191030").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
