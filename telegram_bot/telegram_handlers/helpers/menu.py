from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_menu():
    keyboard_values = [
        [
            {'label': 'Create Account', 'callback': 'create_account'},
            {'label': 'Open Account', 'callback': 'open_account'},
        ]
    ]

    return generate_menu(keyboard_values)


def account_menu():
    keyboard_values = [
        [
            {'label': 'Add account limit', 'callback': 'add_account_limit'},
            {'label': 'Set account balance', 'callback': 'set_account_balance'},
        ],
        [
            {'label': 'Add transaction', 'callback': 'create_transaction'},
            {'label': 'Remove transaction', 'callback': 'remove_transaction'},
        ],
        [
            {'label': 'Show statistics', 'callback': 'show_transactions'},
        ],
        [
            {'label': 'DANGEROUS! Delete account', 'callback': 'delete_account'}
        ],
        [
            {'label': 'Take back to Main Menu', 'callback': 'main_menu'}
        ]
    ]
    return generate_menu(keyboard_values)

def generate_menu(keyboard_values):
    keyboard = [
        [
            InlineKeyboardButton(button['label'], callback_data=button['callback']) for button in line
        ] for line in keyboard_values
    ]

    return InlineKeyboardMarkup(keyboard)