from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.bitta import Holat


@dp.message_handler(CommandHelp(),state=Holat.all_states_names)
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
