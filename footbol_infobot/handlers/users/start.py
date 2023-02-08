from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp,bot
from states.holat import Doimiy
import asyncpg

USER_ID = []
USERNAME = []
JAMI = []

Data_Baza = {
    
}

@dp.message_handler(state=Doimiy.all_states_names, commands='start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = message.from_user.full_name
    user_id = message.from_user.id
       
    if user in USERNAME:
        await message.answer(f"<b>Football Info Bot (FIB)</b> \n \
            \nBu bot <b>fudbolchilar</b> haqidaa malumotlar beradi\n\
             \nBotdan foydalanish uchun fodbolchi ismini kiriting")   
    else:
        USERNAME.append(user)
        USER_ID.append(user_id)
        JAMI.append(1)
        Data_Baza[user] = user_id
        await message.answer(f"<b>Football Info Bot (FIB)</b> \n \
            \nBu bot <b>fudbolchilar</b> haqidaa malumotlar beradi\n\
             \nBotdan foydalanish uchun fodbolchi ismini kiriting")

        ## adminga xabaar yuborish
        msg = f"‼👇‼ <b>BAZAG QO'SHILGANLAR</b> ‼👇‼\n\
            \n👤 {message.from_user.full_name}\n💡 id : <code>{message.from_user.id}</code>\
             \n📃 Bazada {sum(JAMI)} ta foydalanuvchi bor ✅"
        await bot.send_message(chat_id=1173831936,text=msg)

    await Doimiy.xabar.set()