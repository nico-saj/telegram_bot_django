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

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", start)],
            states={
                MAIN_MENU_SELECT: [CallbackQueryHandler(main_menu_handler)],

                ACCOUNT_CREATE: [MessageHandler(filters.TEXT, account_create)],
                ACCOUNT_OPEN: [CallbackQueryHandler(account_open)],
                ACCOUNT_MENU_SELECT: [CallbackQueryHandler(account_menu_handler)],
                ACCOUNT_SET_LIMIT: [MessageHandler(filters.TEXT, account_set_limit)],
                ACCOUNT_SET_BALANCE: [MessageHandler(filters.TEXT, account_set_balance)],

                TRANSACTION_SET_AMOUNT: [MessageHandler(filters.TEXT, transaction_set_amount)],
                TRANSACTION_SET_DATE: [MessageHandler(filters.TEXT, transaction_set_date)],
                TRANSACTION_SET_COMMENT: [MessageHandler(filters.TEXT, transaction_set_comment)],
                TRANSACTIONS_INDEX: [MessageHandler(filters.TEXT, transactions_index)],
                TRANSACTION_REMOVE_LIST: [MessageHandler(filters.TEXT, transaction_remove_list)],
                TRANSACTION_REMOVE: [CallbackQueryHandler(transaction_remove)],
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        )

        application.add_handler(conv_handler)

        application.run_polling()