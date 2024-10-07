from asgiref.sync import sync_to_async
from telegram_bot.models import *

@sync_to_async
def find_or_create_user(user_telegram_id, username):
    user = User.objects.get(user_telegram_id=user_telegram_id)

    if not user:
        user = User.objects.create(user_telegram_id=user_telegram_id, username=username)

    return user

@sync_to_async
def find_user(user_telegram_id):
    return User.objects.get(user_telegram_id=user_telegram_id)
