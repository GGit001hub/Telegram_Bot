from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


keys = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👉 Keyingi sahifa 👉"),
        ],
        [
            KeyboardButton("🔎 Qidirish 🔎")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


keys_keyin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👈 Avvalgi 👈"),
            KeyboardButton("👉 Keyingi 👉")
        ],
        [
            KeyboardButton("🔎 Qidirish 🔎")
        ]
    ],resize_keyboard=True,
    one_time_keyboard=True
)




oldingi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👈 oldingi 👈")
        ],
        [
            KeyboardButton("🔎 Qidirish 🔎")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)