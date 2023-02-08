# import asyncio

# from aiogram import types
# from states.poisk import Turlar

# from data.config import ADMINS
# from loader import dp,bot

# @dp.message_handler(state=Turlar.all_states_names,text="/reklama", user_id=ADMINS)
# @dp.message_handler(text="/reklama", user_id=ADMINS)
# async def send_ad_to_all(message: types.Message):
#     users = await db.select_all_users()
#     for user in users:
#         user_id = user[3]
#         await bot.send_message(chat_id=user_id, text="<a href='https://t.me/zakaz_mod'>Quyidagi kanlaga obuna bo'ling</a>")
#         await asyncio.sleep(0.05)

   

# @dp.message_handler(state=Turlar.all_states_names,text="/bot_reklama", user_id=ADMINS)
# @dp.message_handler(text="/bot_reklama", user_id=ADMINS)
# async def send_ad_to_all(message: types.Message):
#     users = await db.select_all_users()
#     for user in users:
#         user_id = user[3]
#         matn = "You tube endi telegramda\n\
#                 \nHech qanday guruhga azo bo'lmasdan ishlating \
#                 \n<a href='https://t.me/movieshorts_bot'>You tube</a> bot orqali\
#                      \nIstagan videolaringizni topishiz mumkin"
#         await bot.send_message(chat_id=user_id, text=matn,disable_web_page_preview=True)
#         await asyncio.sleep(0.05)





# @dp.message_handler(state=Turlar.all_states_names,text="/bot_fudbol", user_id=ADMINS)
# @dp.message_handler(text="/bot_fudbol", user_id=ADMINS)
# async def send_ad_to_all(message: types.Message):
#     users = await db.select_all_users()
#     for user in users:
#         user_id = user[3]
#         await bot.send_message(chat_id=user_id, text="\n<b>Quyidagi bot orqali fudbolchilar haqida\
#             \nKo'plab malumotlarga ega bo'lasiz</b> \
#             \n<a href='https://t.me/footbol_infobot'>Football bots</a>\n <strong>fudbol haqida malumot</strong>")
#         await asyncio.sleep(0.05)
