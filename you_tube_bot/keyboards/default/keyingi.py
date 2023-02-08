from aiogram.types import ReplyKeyboardMarkup,KeyboardButton




starts = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Video Qidirish"),
            KeyboardButton("Kino Qidirish")
        ],
        [
            KeyboardButton("Kannal Qidirish")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)







bir_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👉 Keyingi sahifa 👉")
        ],
        [
            KeyboardButton("👆 Bosh sahifa ☝")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


ikki_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👈 Avvalgi 👈"),
            KeyboardButton("👉 Keyingi 👉"),
        ],
        [
            KeyboardButton("👆 Bosh sahifa ☝")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)



uch_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👈 Oldingi 👈")
        ],
        [
            KeyboardButton("👆 Bosh sahifa ☝")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
