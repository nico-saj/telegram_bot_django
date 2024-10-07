
from telegram.ext import ContextTypes, ConversationHandler
from telegram import Update

from telegram_bot.models import *
from telegram_bot.telegram_handlers.account_menu import create_account_menu_option, open_account_menu_option

from telegram_bot.telegram_handlers.conversation_tree import *
from telegram_bot.telegram_handlers.helpers import *
from telegram_bot.telegram_handlers.db_helpers import *

async def start_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")

    match query.data:
        case 'create_account':
            return await create_account_menu_option(update, context, await find_user(update.callback_query.from_user.id))
        case 'open_account':
            return await open_account_menu_option(update, context, await find_user(update.callback_query.from_user.id))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    username = update.message.from_user.username

    user = await find_or_create_user(user_id, username)

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Welcome {user.username}! What do you want to do?",
                                   reply_markup=start_menu())

    return MAIN_MENU_SELECT

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"See you soon!")

    return ConversationHandler.END