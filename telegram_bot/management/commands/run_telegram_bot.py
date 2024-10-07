from django.core.management.base import BaseCommand
from django.conf import settings
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    filters
)
from telegram_bot.telegram_handlers import *  # Import your command handlers

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

        # application.add_handler(CommandHandler('start', start))
        # application.add_handler(CallbackQueryHandler(welcome_button))

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", start)],
            states={
                # MAIN_MENU: [CommandHandler("start", start)],
                MAIN_MENU_SELECT: [CallbackQueryHandler(start_menu_handler)],
                ACCOUNT_CREATE: [MessageHandler(filters.TEXT, account_create)],
                # PHOTO: [MessageHandler(filters.PHOTO, photo), CommandHandler("skip", skip_photo)],
                # LOCATION: [
                #     MessageHandler(filters.LOCATION, location),
                #     CommandHandler("skip", skip_location),
                # ],
                # BIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, bio)],
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        )

        application.add_handler(conv_handler)

        application.run_polling()