import asyncio
import aiogram
from aiogram.types import Message

from data.config import ADMINS
from loader import dp, db, bot
from .echo import ADMIN

from states.state_register import Ishchi,Sherig,Shogird,Hodim,Ustoz


@dp.message_handler(text="!kanal",state=Hodim.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!kanal",state=Sherig.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!kanal",state=Ustoz.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!kanal",state=Ishchi.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!kanal",state=Shogird.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!kanal",user_id = ADMIN)
async def send_ad_to_all(message:Message):
    users = await db.select_all_users()
    for user in users:
        adminid = user[3]
        msg = f"Bizning rasmiy kanalga obuna bo'ling\
            \n<a href='https://t.me/hodimishchi'>Kanlimiz linki 👌 Ustoz shogird kanali</a>"
        await bot.send_message(chat_id=adminid, text=msg)
        await asyncio.sleep(0.25)         







@dp.message_handler(text="!chatbot",state=Hodim.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!chatbot",state=Sherig.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!chatbot",state=Ustoz.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!chatbot",state=Ishchi.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!chatbot",state=Shogird.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!chatbot",user_id = ADMIN)
async def send_ad_to_all(message:Message):
    users = await db.select_all_users()
    for user in users:
        adminid = user[3]
        msg = f"<b>Bu bot orqali istagan odamingizga xabar yuborishiz mumkin</b>\
            \n<a href='https://t.me/usermisbot'>Har qanday xabar bot nomidan boradi</a>"
        await bot.send_message(chat_id=adminid, text=msg)
        await asyncio.sleep(0.2)  







@dp.message_handler(text="!youtube",state=Hodim.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!youtube",state=Sherig.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!youtube",state=Ustoz.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!youtube",state=Ishchi.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!youtube",state=Shogird.all_states_names,user_id = ADMIN)
@dp.message_handler(text="!youtube",user_id = ADMIN)
async def send_ad_to_all(message:Message):
    users = await db.select_all_users()
    for user in users:
        adminid = user[3]
        msg = f"  <b>You tube bot</b>  \
            \nYou tube dan istagan video, kino , yutub kanallarni topib beradi\
            \n<a href='https://t.me/movieshorts_bot'>You tube bot linki 👌 Telegramdagi you tube</a>"
        await bot.send_message(chat_id=adminid, text=msg)
        await asyncio.sleep(0.25)  


