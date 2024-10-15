from telegram.ext import ContextTypes, ConversationHandler
from telegram import Update

from telegram_bot.models import *
from telegram_bot.telegram_handlers.helpers import *
from telegram_bot.telegram_handlers.account.menu import accounts_list_menu

async def main_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Selected option: {query.data}")

    match query.data:
        case 'create_account':
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Input account name:")
            return ACCOUNT_CREATE
        case 'open_account':
            reply_markup = await accounts_list_menu(user_telegram_id=update.callback_query.from_user.id)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Select account:", reply_markup=reply_markup)
            return ACCOUNT_OPEN
