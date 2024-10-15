from asgiref.sync import sync_to_async
from telegram.ext import ContextTypes
from telegram import Update

from telegram_bot.models import *
from telegram_bot.telegram_handlers.helpers import *

async def account_create(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await sync_to_async(Account.objects.create, thread_sensitive=True)(
        user_id=(await User.objects.aget(user_telegram_id=update.message.from_user.id)).id,
        name=update.message.text
    )


    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Account created!",
                                   reply_markup=start_menu())

    return MAIN_MENU_SELECT
