from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

for_tell = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📞 Telefon nomer yuborish",request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)




