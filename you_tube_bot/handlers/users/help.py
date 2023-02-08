from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.poisk import Turlar

@dp.message_handler(commands="help",state=Turlar.all_states_names)
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "<a href='https://t.me/Bot_creatorN1'>Fikrlar bo'lsa yuboring</a> - Bot haqida",)
    
    await message.answer("\n".join(text),disable_web_page_preview=True)
