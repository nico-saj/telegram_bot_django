from telegram.ext import ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extract user info from Telegram
    # user_id = update.message.from_user.id
    username = update.message.from_user.username

    # Check if the user is already in the database
    # user = session.query(User).filter_by(user_telegram_id=user_id).first()

    # if user:
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Welcome back, {username}!")
    # else:
    #     # Add the user to the database
    #     new_user = User(user_telegram_id=user_id, username=username)
    #     session.add(new_user)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello, {username}! You've been added to the database.")
