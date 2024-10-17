from asgiref.sync import sync_to_async
from telegram.ext import ContextTypes
from telegram import Update

from telegram_bot.models import *
from telegram_bot.telegram_handlers.helpers import *

async def transactions_index(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_date, end_date = update.message.text.split(' - ')
    transactions_exists = await Transaction.objects.filter(evaluated_at__range=[f"{start_date} 00:00:00", f"{end_date} 23:59:59"]).aexists()
    transactions = await sync_to_async(lambda: list(Transaction.objects.filter(evaluated_at__range=[f"{start_date} 00:00:00", f"{end_date} 23:59:59"])))()

    if transactions_exists:
        transactions_text = f"\n".join([f"{transaction.evaluated_at} - {transaction.amount} ({transaction.comment})" for transaction in transactions])
    else:
        transactions_text = 'No transaction found!'

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=transactions_text,
                                   reply_markup=account_menu())

    return ACCOUNT_MENU_SELECT