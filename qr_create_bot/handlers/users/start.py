from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.qarasin import startga
from states.bitta import Holat


@dp.message_handler(CommandStart(),state=Holat.all_states_names)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    print(message.text,message.from_user.full_name)
    await message.answer(f"š Salom, {message.from_user.full_name}! š\
        \nš¤ Bu bot orqali matnlarga š qr cod yaratishingiz mumkin ā\n",reply_markup=startga)
