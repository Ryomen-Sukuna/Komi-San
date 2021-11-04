from pyrogram import filters

from nksama import bot
from telegraph import upload_file


@bot.on_message(filters.command('ul'))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        message.reply_text(url)
