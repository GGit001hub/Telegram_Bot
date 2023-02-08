from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp,bot


from states.state_register import Shogird,Ustoz,Sherig,Ishchi,Hodim
from keyboards.default.start_uchun import strt_uchun
from keyboards.inline.admin import hayoq
from .echo import ADMIN


telreg = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"


# @dp.message_handler(text="Shogird kerak",state=Hodim.all_states_names)
# @dp.message_handler(text="Shogird kerak",state=Sherig.all_states_names)
# @dp.message_handler(text="Shogird kerak",state=Ustoz.all_states_names)
# @dp.message_handler(text="Shogird kerak",state=Ishchi.all_states_names)
# @dp.message_handler(text="Shogird kerak",state=Shogird.all_states_names)
@dp.message_handler(text="Shogird kerak")
async def bur_shog(ms:Message):
    msg = "<b>Shogird topish uchun ariza</b>\
        \n \nHozir sizga bir nechta savollar beriladi ❓\
        \n✅ Siz savollarga javob berasiz\
        \n📃 Oxirida malumotlaringiz to'gri bo'lsa \"Ha\" tugmasini bosing"
    
    savol = "<strong>Ism Familyangizni kiriting</strong>"
    await ms.answer(msg)
    await ms.answer(savol)
    await Shogird.surname.set()

### ism uvhun handler

@dp.message_handler(state=Shogird.surname)
async def ismzona(ms:Message, state:FSMContext):
    xabar = ms.text.title()
    await state.update_data(name = xabar)

    msg = "👴 Yosh \n \nYoshingizni kiriting !"
    await ms.answer(msg)

    await Shogird.yosh.set()

### Yosh uchun handler

@dp.message_handler(state=Shogird.yosh)
async def yoshxona(ms:Message, state:FSMContext):
    xabar = ms.text
    try:
        yosh = int(xabar)
        await state.update_data(age = yosh)

        msg = "📞 <b> Telefon nomer </b>\n \
            \nTelefon nomer kiriting ? 👇\nQuyidagi ko'rinishda\n \n +998901234567"
        await ms.answer(msg) 
        await Shogird.phone.set()
    except ValueError:
        await ms.answer("Yoshingizni to'g'ri kiriting ⛔")

### telefon nomer uchun handler



@dp.message_handler(state=Shogird.phone,content_types="contact")
@dp.message_handler(state=Shogird.phone,regexp=telreg)
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
    await Shogird.texnologiya.set()
    
@dp.message_handler(state=Shogird.phone)
async def notugri(ms:Message, state:FSMContext):
    await ms.answer("❌ Noto'gri nomer kiritildi\n🔄 Boshqattan nomer kiriting")


### texnologiya uchun handler

@dp.message_handler(state=Shogird.texnologiya)
async def texxona(ms:Message, state:FSMContext):
    xabar = ms.text
    await state.update_data(texnolog = xabar)

    msg = "🌐 <b>Hudut:</b>\n"
    msg += "\nYashaydigan hududingiz !\nViloyat, Shahar yoki Respublika\nkiriting"
    await ms.answer(msg)

    await Shogird.hudud.set()

### yashash hududi uchun handler

@dp.message_handler(state=Shogird.hudud)
async def hudutxona(ms:Message, state:FSMContext):
    xabar = ms.text.title()
    await state.update_data(hudut = xabar)

    msg = "💰 <b>NARX: </b>\n"
    msg += "\nTo'lov narxi qancha ?\nKerakli summani kiriting ! :\n \n"
    await ms.answer(msg)

    await Shogird.narx.set()

### narxi uchun yasalgan handler

@dp.message_handler(state=Shogird.narx)
async def narxxona(ms:Message, state:FSMContext):
    xabar = ms.text
    await state.update_data(narx = xabar)

    msg = "👷‍♂️ <b>Kasp:</b>\n"
    msg += "\nIshlaydigan yoki o'qiydigan\nJoyingizni kiriting"
    await ms.answer(msg)

    await Shogird.kasp.set()

### kasp yoki hunar uchun handler

@dp.message_handler(state=Shogird.kasp)
async def kaspxona(ms:Message, state:FSMContext):
    xabar = ms.text
    await state.update_data(kasp = xabar)

    msg = "🕰<b> Murojaat qilish vaqti:</b>\n"
    msg += "\nQaysi vaqtda murojaat qilish mumkin?\nBo'sh vaqtingiz !!"
    await ms.answer(msg)

    await Shogird.m_vaqti.set()


### murojat qilish vaqti uchun handler

@dp.message_handler(state=Shogird.m_vaqti)
async def vatxona(ms:Message, state:FSMContext):
    xabar = ms.text
    await state.update_data(murojat = xabar)

    msg = "🔎<b> Maqsad: </b>\n"
    msg += "\nMaqsadingiz haqida qisqacha yozib qoldiring"
    await ms.answer(msg)

    await Shogird.maqsad.set()

### maqsad qoldirish uchun handler

@dp.message_handler(state=Shogird.maqsad)
async def fikrxona(ms:Message, state:FSMContext):
    malumot = ms.text
    tel_manzil = ms.from_user.username
    await state.update_data(fikr = malumot)
    await state.update_data(locat_tel = tel_manzil)

    date = await state.get_data()
    ismi = date.get("name")
    yoshi = date.get("age")
    telnomer = date.get("phone")
    texnolog = date.get("texnolog")
    manzil = date.get("hudut")
    narxi = date.get("narx")
    hunar = date.get("kasp")
    m_vaqti = date.get("murojat")
    fikri = date.get("fikr")

    hashtag = str(texnolog)
    q1 = hashtag.split(",")

    malumotnoma = "\n  <b> Shogird kerak : </b>\n"
    malumotnoma += f"\n🧑‍🎓 Shogird : {ismi}\n🕙 Yoshi : {yoshi}\n🖍 Telegram manzil @{tel_manzil}"
    malumotnoma += f"\n☎ Telefon nomer : {telnomer}\n💻 Texnologiya : {texnolog}\n📍 Manzil : {manzil}"
    malumotnoma += f"\n💲 Narxi : {narxi}\n👨🏻‍💻 Kaspi : {hunar}\n⏰ Murojat vaqti : {m_vaqti}\n🔎 Maqsadi : {fikri}\n"
    malumotnoma += f"\n  <b> #ustoz   #{manzil}</b>\n"

    for hsh in q1:
        sqlit = hsh.strip()
        malumotnoma += f" #{sqlit}, "

    # print(q1)


    msg = "Malumotlaringiz Tayyor\nAdminga yuboraymi ???"

    await state.update_data(adminxabar = malumotnoma)
    await ms.answer(malumotnoma)
    await ms.answer(msg,reply_markup=hayoq)
    await Shogird.admin_set.set()

### javobni tekshiruvchi handler
### ha yoki yo'q tugmalari uchun


@dp.callback_query_handler(state=Shogird.admin_set,text="ha")
async def haboss(call:CallbackQuery,state:FSMContext):
    date = await state.get_data()
    telegraph = date.get("tg_manzil")

    malumotnoma = date.get("adminxabar")

    await bot.send_message(chat_id=ADMIN,text=malumotnoma)
    await call.message.answer("Malumotlar yuborildi ✅",reply_markup=strt_uchun)
    await call.message.delete()
    await state.finish()



@dp.callback_query_handler(state=Shogird.admin_set,text="yoq")
async def yoqboss(call:CallbackQuery, state:FSMContext):
    await call.message.answer("So'rov bekor qilindi ❌",reply_markup=strt_uchun)
    await call.message.delete()
    await state.finish()



