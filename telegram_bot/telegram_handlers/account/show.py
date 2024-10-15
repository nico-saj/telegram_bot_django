from asgiref.sync import sync_to_async
from telegram.ext import ContextTypes
from telegram import Update

from telegram_bot.models import *
from telegram_bot.telegram_handlers.helpers import *
from telegram_bot.telegram_handlers.account.menu import *

async def account_open(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['selected_account_id'] = update.callback_query.data
    account = await sync_to_async(Account.objects.get, thread_sensitive=True)(id=context.user_data['selected_account_id'])

    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Selected account: {account.name}")

    account_info = (f"Account info\n"
                    f"Account name: {account.name}\n"
                    f"Account balance: {account.balance}\n"
                    f"Account limit: {account.limit}\n")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=account_info,
                                   reply_markup=account_menu())

    return ACCOUNT_MENU_SELECT