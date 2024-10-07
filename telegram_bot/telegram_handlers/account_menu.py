from telegram.ext import ContextTypes
from telegram import Update

from telegram_bot.models import *
from telegram_bot.telegram_handlers.conversation_tree import *
from telegram_bot.telegram_handlers.helpers import *
from telegram_bot.telegram_handlers.db_helpers import *

async def create_account_menu_option(update: Update, context: ContextTypes.DEFAULT_TYPE, user):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Input account name:")

    return ACCOUNT_CREATE

async def account_create(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Account created!",
                                   reply_markup=start_menu())

    return MAIN_MENU_SELECT


async def open_account_menu_option(update: Update, context: ContextTypes.DEFAULT_TYPE, user):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Select account:")