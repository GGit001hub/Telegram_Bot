from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from .echo import ADMIN
from .start import admin_xabarlari
from states.state_register import Hodim,Shogird,Ishchi,Ustoz,Sherig


@dp.message_handler(commands="help",state=Hodim.all_states_names)
@dp.message_handler(commands="help",state=Sherig.all_states_names)
@dp.message_handler(commands="help",state=Ustoz.all_states_names)
@dp.message_handler(commands="help",state=Ishchi.all_states_names)
@dp.message_handler(commands="help",state=Shogird.all_states_names)
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Bu bot orqali",
        "Dasturlash bo'yicha",
        "  #Ustoz",
        "  #Shogirt",
        "  #Hodim",
        "  #Ishchi",
        "  #Sherig",
        "<strong>Topishingiz mumkin</strong>",
        " ",
        "Bot haqida <a href='t.me/Bot_creatorN1'>malumot</a>")
    
    await message.answer("\n".join(text),disable_web_page_preview=True)







@dp.message_handler(commands="admin_help",state=Hodim.all_states_names)
@dp.message_handler(commands="admin_help",state=Sherig.all_states_names)
@dp.message_handler(commands="admin_help",state=Ustoz.all_states_names)
@dp.message_handler(commands="admin_help",state=Ishchi.all_states_names)
@dp.message_handler(commands="admin_help",state=Shogird.all_states_names)
@dp.message_handler(commands='admin_help')
async def admin_uchun(ms:types.Message):
    tekshirish = ms.from_user.id
    msg = f"   ✅ <b>Admin uchun yordam</b> 😉\n\
        \n1) -\n Kelgan xabarga admin quyidagi so'zlarni\" <b>reply</b> \" qilib yozsa\
        \n‼ Shu xabar kanalga joylanadi 🔑 <b>Kalit so'zlar</b> 👁 \n"

    for xabar in admin_xabarlari:
        msg+=f"#{xabar} , "
    
    msg += f"\n2) - \
        \nAdmin botdagi bironta matnga \" reply \" qilib\
        \n<code>kanal_nomi</code>  deb yosa shu matn kanal nomiga aylanadi\
        \n3) - \nBotdagi bironta rasmga \" reply \" qilib\
        \n<code>kanal_rasmi</code> deb yozsa shu rasm kanal rasmiga qylanadi ❗"


    if tekshirish == ADMIN:
        await ms.answer(msg)
    else:
        await ms.answer("❌ Kechirasiz bu comanda faqat admin uchun 😔")

