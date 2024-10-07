from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_menu():
    keyboard_values = [
        [
            {'label': 'Create Account', 'callback': 'create_account'},
            {'label': 'Open Account', 'callback': 'open_account'},
        ]
    ]

    return generate_menu(keyboard_values)

def buttons(button):
    return InlineKeyboardButton(button['label'], callback_data=button['callback'])

def generate_menu(keyboard_values):
    keyboard = list(map(lambda line: list(map(buttons, line)), keyboard_values))

    return InlineKeyboardMarkup(keyboard)