from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
import asyncpg

from loader import dp, bot
from states.poisk import Turlar
from keyboards.default.keyingi import starts
from data.config import ADMINS

USER_ID = []
USERNAME = []
JAMI = []

Data_Baza = {
    
}


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = message.from_user.full_name
    user_id = message.from_user.id
       
    if user in USERNAME:
        await message.answer(f"π Salom, {message.from_user.full_name}!\
            \nπ€ Botdan foydalanish uchun \
            \nπ <b>Video, Kino yoki You tube kanallar</b> \
            \nπ Nomini kiriting βΌ",reply_markup=starts)
    else:
        USERNAME.append(user)
        USER_ID.append(user_id)
        JAMI.append(1)
        Data_Baza[user] = user_id
        await message.answer(f"Salom, {message.from_user.full_name}!\
            \nBotdan foydalanish uchun \
            \n<b>Video, Kino yoki You tube kanallar</b> \
            \n Nomini kiriting βΌ",reply_markup=starts)

        ## adminga xabaar yuborish
        msg = f"βΌπβΌ <b>BAZAG QO'SHILGANLAR</b> βΌπβΌ\n\
            \nπ€ {message.from_user.full_name}\nπ‘ id : <code>{message.from_user.id}</code>\
             \nπ Bazada {sum(JAMI)} ta foydalanuvchi bor β"
        await bot.send_message(chat_id=1173831936,text=msg)





    

@dp.message_handler(commands="start",state=Turlar.all_states_names)
async def stop(ms:types.Message, state:FSMContext):
    await ms.answer("Bot ishga tushdi")
    await state.finish()


### video uchun

@dp.message_handler(state=Turlar.all_states_names,text="Video Qidirish")
@dp.message_handler(text="Video Qidirish")
async def bot_echo(message: types.Message):
    await message.answer("Video nomini kiriting\nVideo poisk (on) β")
    await Turlar.video.set()



## kino uchun

@dp.message_handler(text="Kino Qidirish")
@dp.message_handler(state=Turlar.all_states_names,text="Kino Qidirish")
async def ksonni(ms:types.Message):
    await ms.answer("Kinolar nomini kiriting β\nKeyin malumotga ega bo'lasiz π")
    await Turlar.kino.set()




@dp.message_handler(text="Kannal Qidirish")
@dp.message_handler(text="Kannal Qidirish",state=Turlar.all_states_names)
async def kanals(ms:types.Message):
    await ms.answer("You tube dagi kanallar nomini kiriting\nchannels poisk (on) β")
    await Turlar.kanall.set()
