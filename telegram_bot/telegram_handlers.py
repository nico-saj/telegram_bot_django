from asgiref.sync import sync_to_async
from telegram.ext import ContextTypes
from telegram import Update
from telegram_bot.models import *

@sync_to_async
def find_or_create_user(user_telegram_id, username):
    user = User.objects.get(user_telegram_id=user_telegram_id)

    if not user:
        user = User.objects.create(user_telegram_id=user_telegram_id, username=username)

    return user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    username = update.message.from_user.username

    user = await find_or_create_user(user_id, username)

    if user:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Welcome back, {username}! Your id is {user.id}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello, {user.username}! You've been added to the database. Your id is {user.id}")
