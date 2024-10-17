from asgiref.sync import sync_to_async
from telegram.ext import ContextTypes
from telegram import Update

from telegram_bot.models import *
from telegram_bot.telegram_handlers.helpers import *

async def transaction_remove_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date = update.message.text
    transactions_exists = await Transaction.objects.filter(evaluated_at__range=[f"{date} 00:00:00", f"{date} 23:59:59"]).aexists()
    transactions = await sync_to_async(lambda: list(Transaction.objects.filter(evaluated_at__range=[f"{date} 00:00:00", f"{date} 23:59:59"])))()

    if transactions_exists:
        menu = generate_menu([[{ 'label': f"{transaction.evaluated_at} - {transaction.amount}", 'callback': transaction.id }] for transaction in transactions])
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text='Select transaction to delete:',
                                       reply_markup=menu)

        return TRANSACTION_REMOVE
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text='No transaction found.',
                                       reply_markup=account_menu())
        return ACCOUNT_MENU_SELECT

async def transaction_remove(update: Update, context: ContextTypes.DEFAULT_TYPE):
    transaction = await Transaction.objects.aget(id=update.callback_query.data)

    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Selected transaction for delete: {transaction.evaluated_at} - {transaction.amount}")

    await transaction.adelete()

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Transaction removed!",
                                   reply_markup=account_menu())
    return ACCOUNT_MENU_SELECT