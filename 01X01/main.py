from decouple import config
api_token = config('API_TOKEN')

from telegram import Update
from telegram.ext import CallbackContext, Updater
from telegram.ext import CommandHandler

updater = Updater(api_token)
dispatcher = updater.dispatcher

def add_member(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    source_channel = '@playlist_dorhami'
    destination_channel = '@testhunteradder'

    source_chat_id = context.bot.get_chat(source_channel)
    destination_chat_id = context.bot.get_chat(destination_channel)
    members = context.bot.get_chat_members_count(source_chat_id)
    for member in range(members):
        user_id = context.bot.get_chat_member(source_chat_id, member).user.id
        try:
            context.bot.add_chat_member(destination_chat_id, user_id)
        except:
            pass
    context.bot.send_message(chat_id, "finish")

dispatcher.add_handler(CommandHandler('add', add_member))

updater.start_polling()