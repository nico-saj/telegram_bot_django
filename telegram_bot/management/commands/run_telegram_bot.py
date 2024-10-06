from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram_bot.telegram_handlers import start  # Import your command handlers

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

        application.add_handler(CommandHandler('start', start))

        application.run_polling()