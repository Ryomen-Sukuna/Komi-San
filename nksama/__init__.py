import os

from pyrogram import Client
from redis import Redis

bot = Client(
    'bot',
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ['API_HASH'],
    bot_token=os.environ['BOT_TOKEN'],
    plugins=dict(root=f"{__name__}/plugins")
)

r = os.environ.get("REDIS_URL").split(":")
REDIS_PASSWORD = r[2]
REDIS_PORT = r[1]

REDIS_DB = Redis(
    host=r[0],
    password=REDIS_PASSWORD,
    port=REDIS_PORT,
    decode_responses=True,
)

REDIS_DB.ping()
PYRO_SESSION = os.environ['PYRO_SESSION']

musicbot = Client(
    PYRO_SESSION,
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ['API_HASH'],
)

help_message = []
