from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp,bot

from states.state_register import Ishchi,Sherig,Shogird,Hodim,Ustoz
from keyboards.inline.admin import hayoq
from keyboards.default.start_uchun import strt_uchun



@dp.message_handler(text="Hodim kerak",state=Hodim.all_states_names)
@dp.message_handler(text="Hodim kerak",state=Sherig.all_states_names)
@dp.message_handler(text="Hodim kerak",state=Ustoz.all_states_names)
@dp.message_handler(text="Hodim kerak",state=Ishchi.all_states_names)
@dp.message_handler(text="Hodim kerak",state=Shogird.all_states_names)
async def druga(ms:Message):
    msg = "<b>Hodim topish uchun ariza</b>\
        \n \n❗ Hozir sizga bir nechta savollar beriladi\
        \n✔ Siz savollarga javob berasiz\
        \n👍 Oxirida malumotlaringiz to'gri bo'lsa \"Ha\" tugmasini bosing"
    
    savol = "<strong>Idora nomini kiriting</strong>"
    await ms.answer(msg)
    await ms.answer(savol)
    await Ishchi.i_name.set()





@dp.message_handler(text="Ish joyi kerak",state=Hodim.all_states_names)
@dp.message_handler(text="Ish joyi kerak",state=Sherig.all_states_names)
@dp.message_handler(text="Ish joyi kerak",state=Ustoz.all_states_names)
@dp.message_handler(text="Ish joyi kerak",state=Ishchi.all_states_names)
@dp.message_handler(text="Ish joyi kerak",state=Shogird.all_states_names)
# @dp.message_handler(text="Ish joyi kerak")
async def druga(ms:Message):
    msg = "<b>Ish joyi topish uchun ariza</b>\
        \n \n❗ Hozir sizga bir nechta savollar beriladi\
        \n✔ Siz savollarga javob berasiz\
        \n👍 Oxirida malumotlaringiz to'gri bo'lsa \"Ha\" tugmasini bosing"
    
    savol = "<strong>Ism Familyangizni kiriting</strong>"
    await ms.answer(msg)
    await ms.answer(savol)
    await Hodim.h_name.set()





@dp.message_handler(text="Sherik kerak",state=Hodim.all_states_names)
@dp.message_handler(text="Sherik kerak",state=Sherig.all_states_names)
@dp.message_handler(text="Sherik kerak",state=Ustoz.all_states_names)
@dp.message_handler(text="Sherik kerak",state=Ishchi.all_states_names)
@dp.message_handler(text="Sherik kerak",state=Shogird.all_states_names)
# @dp.message_handler(text="Sherik kerak")
async def druga(ms:Message):
    msg = "<b>Sherig topish uchun ariza</b>\
        \n \n❗ Hozir sizga bir nechta savollar beriladi\
        \n✔ Siz savollarga javob berasiz\
        \n👍 Oxirida malumotlaringiz to'gri bo'lsa \"Ha\" tugmasini bosing"
    
    savol = "<strong>Ism Familyangizni kiriting</strong>"
    await ms.answer(msg)
    await ms.answer(savol)
    await Sherig.sh_name.set()




@dp.message_handler(text="Shogird kerak",state=Hodim.all_states_names)
@dp.message_handler(text="Shogird kerak",state=Sherig.all_states_names)
@dp.message_handler(text="Shogird kerak",state=Ustoz.all_states_names)
@dp.message_handler(text="Shogird kerak",state=Ishchi.all_states_names)
@dp.message_handler(text="Shogird kerak",state=Shogird.all_states_names)
# @dp.message_handler(text="Shogird kerak")
async def bur_shog(ms:Message):
    msg = "<b>Shogird topish uchun ariza</b>\
        \n \nHozir sizga bir nechta savollar beriladi\
        \nSiz savollarga javob berasiz\
        \nOxirida malumotlaringiz to'gri bo'lsa \"Ha\" tugmasini bosing"
    
    savol = "<strong>Ism Familyangizni kiriting</strong>"
    await ms.answer(msg)
    await ms.answer(savol)
    await Shogird.surname.set()







@dp.message_handler(text="Ustoz kerak",state=Hodim.all_states_names)
@dp.message_handler(text="Ustoz kerak",state=Sherig.all_states_names)
@dp.message_handler(text="Ustoz kerak",state=Ustoz.all_states_names)
@dp.message_handler(text="Ustoz kerak",state=Ishchi.all_states_names)
@dp.message_handler(text="Ustoz kerak",state=Shogird.all_states_names)
# @dp.message_handler(text="Ustoz kerak")
async def ustoz(ms:Message):
    msg = "<b>Ustoz topish uchun ariza</b>\
        \n \nHozir sizga bir nechta savollar beriladi\
        \nSiz savollarga javob berasiz\
        \nOxirida malumotlaringiz to'gri bo'lsa \"Ha\" tugmasini bosing\
        \nBekor qilish uchun \"Bekor qilish\" bosing\n \n"
    
    savol = "<strong>Ism Familyangizni kiriting</strong>"

    await ms.answer(msg)
    await ms.answer(savol)
    await ms.delete()
    await Ustoz.us_surname.set()



