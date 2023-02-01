
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6029847668:AAEs88Mc2H2Crc5rL_6hqpnEQHdEYMiCMyM")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "28123666"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "e0a07eff8e5ff1dd72edcac6bb213a42")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQGtIhIAE-07XFojA3qLwS7HrRiIffmVQFEv5UERxZ5A_W0n4Ruyogq9jlDD1bW8uY1MuhSvDeP10HaoUWv38R5yUc0Ngkzpfv4hi63LS0nljG4OuihGVleRz8dwrvWrt7PZChCkGj_24jMiSvLsxJZVY_XLnAXMbifo2dSCWe00cuLjci-ako3C0or7mNqTgIA_gTy_ePHnAeFnb_aPo2AXy-H_vR13rTEhLfzeQKCN68HNupvZ_mgPxFvTICOdpr1v8XTIg66BrQZXUD1tXmGx848njKaG0zMSuhtMS4wmdxS4GkmmmBEjH4Hy-rYxGfImBA3UvjKnVRZxkeu14Gcrcs1mQAAAAAFO9YB4AA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://prasad:12345@cluster0.cjtzf1k.mongodb.net/?retryWrites=true&w=majority")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1256202333").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "no").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "no").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "no").lower()




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
