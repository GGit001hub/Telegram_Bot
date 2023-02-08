import io

from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp,bot
from .start import KANAL_ID
from .echo import ADMIN

from states.state_register import Ishchi,Sherig,Shogird,Hodim,Ustoz





@dp.message_handler(text="kanal_rasmi",state=Hodim.all_states_names,user_id = ADMIN)
@dp.message_handler(text="kanal_rasmi",state=Sherig.all_states_names,user_id = ADMIN)
@dp.message_handler(text="kanal_rasmi",state=Ustoz.all_states_names,user_id = ADMIN)
@dp.message_handler(text="kanal_rasmi",state=Ishchi.all_states_names,user_id = ADMIN)
@dp.message_handler(text="kanal_rasmi",state=Shogird.all_states_names,user_id = ADMIN)
@dp.message_handler(text="kanal_rasmi",user_id = ADMIN)
async def set_new_photo(ms:types.Message):
    sc_mess = ms.reply_to_message
    photo = sc_mess.photo[-1]
    #rasmni xotiraga 2 lik sanoq sistema orqali yuklaymiz
    photo = await photo.download(destination=io.BytesIO())
    #yuklangan rasmni qayta o'qiymiz
    input_file = types.InputFile(photo)
    # 1 - usul : Malumot o'zgartirishni
    await bot.set_chat_photo(chat_id=KANAL_ID,photo=input_file)





@dp.message_handler(text="kanal_nomi",state=Hodim.all_states_names,user_id = ADMIN)
@dp.message_handler(text="kanal_nomi",state=Sherig.all_states_names,user_id = ADMIN)
@dp.message_handler(text="kanal_nomi",state=Ustoz.all_states_names,user_id = ADMIN)
@dp.message_handler(text="kanal_nomi",state=Ishchi.all_states_names,user_id = ADMIN)
@dp.message_handler(text="kanal_nomi",state=Shogird.all_states_names,user_id = ADMIN)
@dp.message_handler(text="kanal_nomi",user_id = ADMIN)
async def set_title(ms:types.Message):
    sc_message = ms.reply_to_message
    titles = sc_message.text
    # 2 - usul : malumot o'zgartirish
    await bot.set_chat_title(chat_id=KANAL_ID, title=titles)



