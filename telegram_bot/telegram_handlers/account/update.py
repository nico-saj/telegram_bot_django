from asgiref.sync import sync_to_async
from telegram.ext import ContextTypes
from telegram import Update

from telegram_bot.models import *
from telegram_bot.telegram_handlers.helpers import *

async def account_set_limit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    account = await Account.objects.aget(id=context.user_data['selected_account_id'])

    account.limit = update.message.text
    await sync_to_async(account.save, thread_sensitive=True)()

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Account updated!",
                                   reply_markup=account_menu())

    return ACCOUNT_MENU_SELECT

async def account_set_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    account = await Account.objects.aget(id=context.user_data['selected_account_id'])

    account.balance = update.message.text
    await sync_to_async(account.save, thread_sensitive=True)()

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Account updated!",
                                   reply_markup=account_menu())

    return ACCOUNT_MENU_SELECT