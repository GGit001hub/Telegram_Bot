from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_uchun import strt_uchun
from states.state_register import Hodim,Sherig,Ustoz,Ishchi,Shogird
import asyncpg

traqam = []

KANAL_ID = -1001741886020

from loader import dp,bot,db
from data.config import ADMINS
from .echo import ADMIN


@dp.message_handler(CommandStart(),state=Hodim.all_states_names)
@dp.message_handler(CommandStart(),state=Sherig.all_states_names)
@dp.message_handler(CommandStart(),state=Ustoz.all_states_names)
@dp.message_handler(CommandStart(),state=Ishchi.all_states_names)
@dp.message_handler(CommandStart(),state=Shogird.all_states_names)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)


    await message.answer("Assalomu aleykum, {message.from_user.full_name}!\n\
        \nUstoz Shogird botga xush kelipsiz\
        \n<b>Bot haqidagi malumotlarni /help buyrug'i orqali bilib oling</b>")

    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)










@dp.message_handler(commands="restart",state=Hodim.all_states_names)
@dp.message_handler(commands="restart",state=Sherig.all_states_names)
@dp.message_handler(commands="restart",state=Ustoz.all_states_names)
@dp.message_handler(commands="restart",state=Ishchi.all_states_names)
@dp.message_handler(commands="restart",state=Shogird.all_states_names)
@dp.message_handler(commands="restart")
async def restar(ms:types.Message):
    await ms.answer("Bot qayta ishga tushdi",reply_markup=strt_uchun)










admin_xabarlari = ['yuborish',1,'joyla','kanalga_joyla','qada','yubor',"jo'nat","qo'sh","yes","ok",'okey','da','tashla','mayli','qada',
'joylayver','ruxsat','mumkin','yb','true']





@dp.message_handler(text=admin_xabarlari,state=Hodim.all_states_names,user_id=ADMIN)
@dp.message_handler(text=admin_xabarlari,state=Sherig.all_states_names,user_id=ADMIN)
@dp.message_handler(text=admin_xabarlari,state=Ustoz.all_states_names,user_id=ADMIN)
@dp.message_handler(text=admin_xabarlari,state=Ishchi.all_states_names,user_id=ADMIN)
@dp.message_handler(text=admin_xabarlari,state=Shogird.all_states_names,user_id=ADMIN)
@dp.message_handler(text=admin_xabarlari,user_id=ADMIN)
async def adminset(ms:types.Message):
    traqam.append(1)
    xabar = ms.reply_to_message
    javob =xabar.text
    chtadmin = KANAL_ID
    await bot.send_message(chat_id=chtadmin,text=javob)
    await ms.answer(f"😜 xabar kanalga joylashtirildi ✅\n👉 Bu {sum(traqam)} - xabar")
