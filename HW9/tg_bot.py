from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters
import re

TOKEN = ""

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def clear_string(update, context):
    string = update.message.text
    pattern = "[А-Яа-я]*абв[А-Яа-я]*"
    replacement = "$#*@%!!!"
    context.bot.send_message(update.effective_chat.id, replacement.join(re.split(pattern, string)))


clear_string_handler = MessageHandler(Filters.text, clear_string)

dispatcher.add_handler(clear_string_handler)

updater.start_polling()
updater.idle()
