from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


strt_uchun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ustoz kerak"),
            KeyboardButton("Shogird kerak"),
        ],
        [
            KeyboardButton("Hodim kerak"),
            KeyboardButton("Ish joyi kerak"),
        ],
        [
            KeyboardButton("Sherik kerak"),
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
