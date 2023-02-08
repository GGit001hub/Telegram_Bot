from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


hayoq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Ha",callback_data="ha"),
            InlineKeyboardButton("❌ Yo'q",callback_data="yoq")
        ]
    ],
    row_width=5
)



channel_send = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Ha joylansin",callback_data="joylansin")
        ],
        [
            InlineKeyboardButton("❌ Yo'q shart emas",callback_data="joylanmasin")
        ]
    ]
)


