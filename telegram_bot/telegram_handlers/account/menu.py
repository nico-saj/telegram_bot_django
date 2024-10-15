from asgiref.sync import sync_to_async
from telegram.ext import ContextTypes
from telegram import Update

from telegram_bot.models import *
from telegram_bot.telegram_handlers.helpers import *

async def accounts_list_menu(user_telegram_id):
    user = await User.objects.aget(user_telegram_id=user_telegram_id)
    accounts = await sync_to_async(lambda: list(user.account_set.all()))()
    return generate_menu([[{'label': account.name, 'callback': account.id}] for account in accounts])

async def account_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Selected option: {query.data}")

    match query.data:
        case 'add_account_limit':
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Input account limit:")
            return ACCOUNT_SET_LIMIT
        case 'set_account_balance':
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Input account balance:")
            return ACCOUNT_SET_BALANCE
        case 'create_transaction':
            return await create_transaction__account_menu_option(update, context)
        case 'remove_transaction':
            return await remove_transaction__account_menu_option(update, context)
        case 'show_transactions':
            return await create_transaction__account_menu_option(update, context)
        case 'delete_account':
            return await delete_account__account_menu_option(update, context)
        case 'main_menu':
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Select menu option:", reply_markup=start_menu())
            return MAIN_MENU_SELECT