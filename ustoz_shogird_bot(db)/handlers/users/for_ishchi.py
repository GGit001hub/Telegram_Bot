from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp,bot

from states.state_register import Hodim,Sherig,Ustoz,Ishchi,Shogird
from keyboards.inline.admin import hayoq,channel_send
from keyboards.default.start_uchun import strt_uchun
from .echo import ADMIN


telreg = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"


# @dp.message_handler(text="Ish joyi kerak",state=Hodim.all_states_names)
# @dp.message_handler(text="Ish joyi kerak",state=Sherig.all_states_names)
# @dp.message_handler(text="Ish joyi kerak",state=Ustoz.all_states_names)
# @dp.message_handler(text="Ish joyi kerak",state=Ishchi.all_states_names)
# @dp.message_handler(text="Ish joyi kerak",state=Shogird.all_states_names)
@dp.message_handler(text="Ish joyi kerak")
async def druga(ms:Message):
    msg = "<b>Ish joyi topish uchun ariza</b>\
        \n \n❗ Hozir sizga bir nechta savollar beriladi\
        \n✔ Siz savollarga javob berasiz\
        \n👍 Oxirida malumotlaringiz to'gri bo'lsa \"Ha\" tugmasini bosing"
    
    savol = "<strong>Ism Familyangizni kiriting</strong>"
    await ms.answer(msg)
    await ms.answer(savol)
    await Hodim.h_name.set()


@dp.message_handler(state=Hodim.h_name)
async def namesur(ms:Message, state:FSMContext):
    msg = (ms.text).title()
    await state.update_data(ism = msg)

    xabar = "👴 Yosh \n \nYoshingizni kiriting !"
    await ms.answer(xabar)
    await Hodim.h_yosh.set()


@dp.message_handler(state=Hodim.h_yosh)
async def yoshxona(ms:Message, state:FSMContext):
    xabar = ms.text
    try:
        yosh = int(xabar)
        await state.update_data(age = yosh)

        msg = "📞 <b> Telefon nomer </b>\n \
            \nTelefon nomer kiriting ? 👇\nQuyidagi ko'rinishda\n \n +998901234567"
        await ms.answer(msg) 
        await Hodim.h_phone.set()
    except ValueError:
        await ms.answer("Yoshingizni to'g'ri kiriting ⛔")

### telefon nomer uchun handler



@dp.message_handler(state=Hodim.h_phone,content_types="contact")
@dp.message_handler(state=Hodim.h_phone,regexp=telreg)
async def telxona(ms:Message, state:FSMContext):
    if ms.contact:
        nomer = ms.contact.phone_number
    else:
        nomer = ms.text
    await state.update_data(phone = nomer)

    msg = "📚 <b>Texnologiya</b>\n"
    msg += "\nTalab qilinadigan texnologiyalarni kiriting?\
        \nTexnologiya nomlarini vergul bilan ajrating. "
    await ms.answer(msg)
    await Hodim.h_texnologiya.set()
    
@dp.message_handler(state=Hodim.h_phone)
async def notugri(ms:Message, state:FSMContext):
    await ms.answer("❌ Noto'gri nomer kiritildi\n🔄 Boshqattan nomer kiriting")


### texnologiya uchun handler

@dp.message_handler(state=Hodim.h_texnologiya)
async def texxona(ms:Message, state:FSMContext):
    xabar = ms.text
    await state.update_data(texnolog = xabar)

    msg = "🌐 <b>Hudut:</b>\n"
    msg += "\nYashaydigan hududingiz !\nViloyat, Shahar yoki Respublika\nkiriting"
    await ms.answer(msg)

    await Hodim.h_hudud.set()

### yashash hududi uchun handler

@dp.message_handler(state=Hodim.h_hudud)
async def hudutxona(ms:Message, state:FSMContext):
    xabar = ms.text.title()
    await state.update_data(hudut = xabar)

    msg = "💰 <b>NARX: </b>\n"
    msg += "\nTo'lov narxi qancha ?\nKerakli summani kiriting ! :\n \n"
    await ms.answer(msg)

    await Hodim.h_narx.set()

### narxi uchun yasalgan handler

@dp.message_handler(state=Hodim.h_narx)
async def narxxona(ms:Message, state:FSMContext):
    xabar = ms.text
    await state.update_data(narx = xabar)

    msg = "👷‍♂️ <b>Kasp:</b>\n"
    msg += "\nIshlaydigan yoki o'qiydigan\nJoyingizni kiriting"
    await ms.answer(msg)

    await Hodim.h_kasp.set()

### kasp yoki hunar uchun handler

@dp.message_handler(state=Hodim.h_kasp)
async def kaspxona(ms:Message, state:FSMContext):
    xabar = ms.text
    await state.update_data(kasp = xabar)

    msg = "🕰<b> Murojaat qilish vaqti:</b>\n"
    msg += "\nQaysi vaqtda murojaat qilish mumkin?\nBo'sh vaqtingiz !!"
    await ms.answer(msg)

    await Hodim.h_m_vaqti.set()


### murojat qilish vaqti uchun handler

@dp.message_handler(state=Hodim.h_m_vaqti)
async def vatxona(ms:Message, state:FSMContext):
    xabar = ms.text
    await state.update_data(murojat = xabar)

    msg = "🔎<b> Maqsad: </b>\n"
    msg += "\nMaqsadingiz haqida qisqacha yozib qoldiring"
    await ms.answer(msg)

    await Hodim.h_shmaqsad.set()

### maqsad qoldirish uchun handler

@dp.message_handler(state=Hodim.h_shmaqsad)
async def maqsadxona(ms:Message, state:FSMContext):
    xabar = ms.text
    telegraph = ms.from_user.username
    await state.update_data(maqsad = xabar)
    await state.update_data(tg_manzil = telegraph)


    date = await state.get_data()

    ismi = date.get("ism")
    yoshi = date.get("age")
    telnomer = date.get("phone")
    txnlg = date.get("texnolog")
    manzil = date.get("hudut")
    narxi = date.get("narx")
    kaspi = date.get("kasp")
    mrj_vaqt = date.get("murojat")
    maqsad = date.get("maqsad")
    
    hashtag = str(txnlg)
    q1 = hashtag.split(",")
 
    malumotnoma = "<b>Ish joyi kerak : </b>\n"
    malumotnoma += f"\n👨‍🏫 Hodim  {ismi}\n🕙 Yoshi : {yoshi}\n🖍 Telegram manzil @{telegraph}"
    malumotnoma += f"\n☎ Telefon nomer : {telnomer}\n💻 Texnologiya : {txnlg}\n📍 Manzil : {manzil}"
    malumotnoma += f"\n💲 Narxi : {narxi}\n👨🏻‍💻 Kaspi : {kaspi}\n⏰ Murojat vaqti : {mrj_vaqt}\n🔎 Maqsadi : {maqsad}\n"
    malumotnoma += f"\n  <b> #hodim   #{manzil}</b>\n"

    for hsh in q1:
        sqlit = hsh.strip()
        malumotnoma += f" #{sqlit}, "

    savol = "Malumotlar to'grimi ?"

    await state.update_data(ikkinchi1 = malumotnoma)
    await ms.answer(malumotnoma)
    await ms.answer(savol,reply_markup=hayoq)

    await Hodim.h_admin_set.set()






@dp.callback_query_handler(state=Hodim.h_admin_set,text="ha")
async def haboss(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()

    malumotnoma = date.get("ikkinchi1")

    await bot.send_message(chat_id=ADMIN,text=malumotnoma)
    await call.message.answer("Malumotlar yuborildi ✅",reply_markup=strt_uchun)
    await call.message.delete()
    await state.finish()




@dp.callback_query_handler(state=Hodim.h_admin_set,text="yoq")
async def yoqboss(call:CallbackQuery, state:FSMContext):
    await call.message.answer("So'rov bekor qilindi ❌",reply_markup=strt_uchun)
    await call.message.delete()
    await state.finish()



