import requests
from pyrogram import filters

from nksama import bot


@bot.on_message(filters.command('pat'))
def pat(_, message):
    reply = message.reply_to_message
    if reply:
        res = requests.get(
            'https://some-random-api.ml/animu/pat'
        ).json()
        url = res['link']
        reply.reply_animation(url)

    else:
        message.reply_animation(url)
