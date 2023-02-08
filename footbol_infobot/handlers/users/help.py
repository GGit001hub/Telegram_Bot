from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.holat import Doimiy


@dp.message_handler(state=Doimiy.all_states_names, commands='help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "<a href='https://t.me/Bot_creatorN1'>/bot_haqida</a> - Bot haqida malumot")
    
    await message.answer("\n".join(text),disable_web_page_preview=True)
