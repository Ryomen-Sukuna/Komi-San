import os

from pyrogram import filters

from nksama import bot
from nksama.utils.sendlog import send_log


@bot.on_message(filters.command('rename'))
def rename(_, message):
    try:
        filename = message.text.replace(message.text.split(" ")[0], "")

    except Exception as e:
        send_log(e)

    reply = message.reply_to_message
    if reply:
        x = message.reply_text("Downloading.....")
        path = reply.download(file_name=filename)
        x.edit("Uploading.....")
        message.reply_document(path)
        os.remove(path)
