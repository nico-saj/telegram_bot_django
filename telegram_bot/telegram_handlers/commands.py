from telegram.ext import ContextTypes, ConversationHandler
from telegram import Update

from telegram_bot.models import *
from telegram_bot.telegram_handlers.helpers import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user, _ = await User.objects.aget_or_create(user_telegram_id=update.message.from_user.id, defaults={ 'username': update.message.from_user.username })

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Welcome {user.username}! What do you want to do?",
                                   reply_markup=start_menu())

    return MAIN_MENU_SELECT

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"See you soon!")

    return ConversationHandler.END