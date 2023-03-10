from decouple import config
api_token = config('API_TOKEN')

from telegram import Update
from telegram.ext import CallbackContext, Updater
from telegram.ext import CommandHandler

updater = Updater(api_token)
dispatcher = updater.dispatcher

def add_member(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    source_channel = '@your source channel'
    destination_channel = '@your destination channel'
    # get channels id
    source_chat_id = context.bot.get_chat(source_channel).id
    destination_chat_id = context.bot.get_chat(destination_channel).id
    # get all members from source channel
    members = context.bot.get_chat_members_count(source_chat_id)
    # start add members to channel
    for member in range(members):
        user_id = context.bot.get_chat_member(source_chat_id, member).user.id
        try:
            context.bot.add_chat_member(destination_chat_id, user_id)
        except:
            pass
    context.bot.send_message(chat_id, "finish")

# add handler => when user send /add then process start
dispatcher.add_handler(CommandHandler('add', add_member))

updater.start_polling()