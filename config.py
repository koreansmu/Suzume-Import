import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "24845544"
API_HASH = "57f32b90d5406552ab9156f6404fe5a8"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7158896048:AAEifu35rAfgBvI2qlY1DFFg8oHEaN1sk5M"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://github9210:ieMwBAIuNl2NEMRO@cluster0.lcwkg5r.mongodb.net/?retryWrites=true&w=majority"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 6000))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002064111110

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = 6257927828

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/koreansmu/SuzumeeLV",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/storm_techh")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/storm_core")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2d3fd5ccdd3d43dda6f17864d8eb7281")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "48d311d8910a4531ae81205e1f754d27")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQF7HOgAAaEuXC-Y5WpWU0ILOkHp1vhm0RPwXeWvYQveEkKYjDaPQ_WXxgiFWujmMJjHfmjlTLI8EKUc55U8HlxiTA6StHMV2JQrEtvnHdUpZ_VD1qg_oMXplOgcROtwNXevdhQR3o8vSiMS1VZjNjMTU3jiAUzVMT3Q1oPSqDHJzsTKpdwqJJZnwVl6HcCdUEMUdcSEgTnMXpZaZllNvHiyeFYpXrs3Lg5EH7DtIbLME9thi51EsGLpImXq-QE5IjQelZPoa7KPH8pCWgoOFBmiP8VclPtKIlK12TPxTxTn_hnQw-S7OGUjTgvIvaT6ar9XhKTdSG7zajhLF5uylVnOf3QMDgAAAAGFSB7bAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/urh7m5.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/zp9vzp.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/gdda3c.jpg"
STATS_IMG_URL = "https://files.catbox.moe/jtx6gx.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/velktq.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/33uq2t.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/x2cr8h.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/kcw9lh.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
