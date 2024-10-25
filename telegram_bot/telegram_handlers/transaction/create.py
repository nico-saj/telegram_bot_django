from telegram.ext import ContextTypes
from telegram import Update

from telegram_bot.models import *
from telegram_bot.telegram_handlers.helpers import *

async def transaction_set_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['transaction_amount'] = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Input transaction evaluation time in format 'YYYY-MM-DD HH:MM':")
    return TRANSACTION_SET_DATE

async def transaction_set_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['transaction_date'] = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Input transaction comment (if needed):")

    return TRANSACTION_SET_COMMENT

async def transaction_set_comment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Transaction.objects.acreate(account_id=context.user_data['selected_account_id'],
                                      status=context.user_data['transaction_status'],
                                      amount=abs(int(context.user_data['transaction_amount'])),
                                      evaluated_at=context.user_data['transaction_date'],
                                      comment=update.message.text)
    account = await Account.objects.aget(id=context.user_data['selected_account_id'])
    transaction_amount = context.user_data['transaction_amount'] if context.user_data['transaction_status'] == 'income' else -abs(int(context.user_data['transaction_amount']))
    new_balance = account.balance + transaction_amount
    await Account.objects.filter(id=context.user_data['selected_account_id']).aupdate(balance=new_balance)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Transaction created!",
                                   reply_markup=account_menu())

    return ACCOUNT_MENU_SELECT