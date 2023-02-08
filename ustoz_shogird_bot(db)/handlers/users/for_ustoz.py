from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Regexp
from loader import dp,bot

from states.state_register import Ustoz,Shogird,Sherig,Hodim,Ishchi
from keyboards.default.tell_button import for_tell
from keyboards.default.start_uchun import strt_uchun
from keyboards.inline.admin import hayoq
from .echo import ADMIN



telreg = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

@dp.message_handler(state=Shogird.all_states_names,commands="restart")
@dp.message_handler(state=Ustoz.all_states_names,commands="restart")
async def restar(ms:Message,state:FSMContext):
    await ms.answer("Bot qayta ishga tushdi",reply_markup=strt_uchun)
    await state.finish()




###  Ustoz kerak tugmasi uchun handler


# @dp.message_handler(text="Ustoz kerak",state=Hodim.all_states_names)
# @dp.message_handler(text="Ustoz kerak",state=Sherig.all_states_names)
# @dp.message_handler(text="Ustoz kerak",state=Ustoz.all_states_names)
# @dp.message_handler(text="Ustoz kerak",state=Ishchi.all_states_names)
# @dp.message_handler(text="Ustoz kerak",state=Shogird.all_states_names)
@dp.message_handler(text="Ustoz kerak")
async def ustoz(ms:Message):
    msg = "<b>Ustoz topish uchun ariza</b>\
        \n \n❓ Hozir sizga bir nechta savollar beriladi\
        \n✅ Siz savollarga javob berasiz\
        \n📃 Oxirida malumotlaringiz to'gri bo'lsa \"Ha\" tugmasini bosing"
    
    savol = "<strong>Ism Familyangizni kiriting</strong>"

    await ms.answer(msg)
    await ms.answer(savol)
    await ms.delete()
    await Ustoz.us_surname.set()

### ism familyasi uchun handler

@dp.message_handler(state=Ustoz.us_surname)
async def ismxona(ms:Message,state:FSMContext):
    ismi = ms.text.title()
    await state.update_data(name = ismi)

    msg = "👴 Yosh \n \nYoshingizni kiriting !"
    await ms.answer(msg)
    await Ustoz.us_yosh.set()

## Yosh uchun handler

@dp.message_handler(state=Ustoz.us_yosh)
async def yoshxona(ms:Message, state:FSMContext):
    yos = ms.text
    try:
        yosh = int(yos)
        await state.update_data(age = yosh)
    
        msg = "📞 <b> Telefon nomer </b>\n \
            \nTelefon nomer kiriting ? yoki \n \
            \nQuyidaki knopkani bosing 👇"
        await ms.answer(msg, reply_markup=for_tell)
        await Ustoz.us_phone.set()
    except ValueError:
        await ms.answer("Yoshingizni to'g'ri kiriting")


## telefon nomer uchun handler

@dp.message_handler(state=Ustoz.us_phone,content_types="contact")
@dp.message_handler(state=Ustoz.us_phone,regexp=telreg)
async def telcona(ms:Message, state:FSMContext):
    if ms.contact:
        nomer = ms.contact.phone_number
    else:
        nomer = ms.text
    await state.update_data(phone = nomer)


    msg = "📚 <b>Texnologiya</b>\n"
    msg += "\nSiz o'rganishni xoxlaydigan\nDasturlarni kiriting 👇\nVergul bilan ajratib qo'ying"
    await ms.answer(msg,reply_markup=strt_uchun)
    await Ustoz.us_texno.set()

@ dp.message_handler(state=Ustoz.us_phone)
async def notugri(ms:Message):
    await ms.answer("Siz noto'g'ri nomer kiritdingiz\nIltimos nomeringizni tekshiring")



### texnologiyalar uchun handler

@dp.message_handler(state=Ustoz.us_texno)
async def texnxona(ms:Message, state:FSMContext):
    mesags = ms.text
    await state.update_data(texnologiya =mesags)

    msg = "🌐 <b>Hudut:</b>\n"
    msg += "\nYashaydigan hududingiz !\nViloyat, Shahar yoki Respublika\nkiriting"
    await ms.answer(msg)
    await Ustoz.us_hudut.set()


### hudut uchun hanler

@dp.message_handler(state=Ustoz.us_hudut)
async def huduxona(ms:Message, state: FSMContext):
    malumot = ms.text.title()
    await state.update_data(manzil = malumot)

    msg = "💰 <b>NARX: </b>\n"
    msg += "\nTo'lov qilasizmi ?\nKerakli summani kiriting :\n \n"
    await ms.answer(msg)
    await Ustoz.us_narx.set()

### narx uchun handler

@dp.message_handler(state=Ustoz.us_narx)
async def narxona(ms:Message, state:FSMContext):
    malumot = ms.text
    await state.update_data(narx = malumot)

    msg = "👷‍♂️ <b>Kasp:</b>\n"
    msg += "\nIshlasangiz ishlaydigan yoki\nO'qisangiz o'qiydigan joyingizni yozing"
    await ms.answer(msg)
    await Ustoz.us_kasp.set()

### kasp uchun handler

@dp.message_handler(state=Ustoz.us_kasp)
async def kaspxona(ms:Message, state:FSMContext):
    malumot = ms.text
    await state.update_data(kaspi = malumot)

    msg = "🕰<b> Murojaat qilish vaqti:</b>\n"
    msg += "\nQaysi vaqtda murojaat qilish mumkin?\nBo'sh vaqtingiz !!"
    await ms.answer(msg)
    await Ustoz.us_murojat.set()

### murojat uchun handler

@dp.message_handler(state=Ustoz.us_murojat)
async def murxona(ms:Message, state:FSMContext):
    malumot = ms.text
    await state.update_data(murojat = malumot)

    msg = "🔎<b> Maqsad: </b>\n"
    msg += "\nMaqsadingiz haqida qisqacha yozib qoldiring"
    await ms.answer(msg)
    await Ustoz.us_fikr.set()


### fikr qoldirish uchun handler
## va malumotlarni tekshirish uchun

@dp.message_handler(state=Ustoz.us_fikr)
async def fikrxona(ms:Message, state:FSMContext):
    malumot = ms.text
    tel_manzil = ms.from_user.username
    await state.update_data(fikr = malumot)
    await state.update_data(locat_tel = tel_manzil)

    date = await state.get_data()
    ismi = date.get("name")
    yoshi = date.get("age")
    telnomer = date.get("phone")
    texnolog = date.get("texnologiya")
    manzil = date.get("manzil")
    narxi = date.get("narx")
    hunar = date.get("kaspi")
    m_vaqti = date.get("murojat")
    fikri = date.get("fikr")

    hashtag = str(texnolog)
    q1 = hashtag.split(",")

    malumotnoma = "\n<b> Ustoz kerak : </b>\n"
    malumotnoma += f"\n🧑‍🎓 Shogird : {ismi}\n🕙 Yoshi : {yoshi}\n🖍 Telegram manzil @{tel_manzil}"
    malumotnoma += f"\n☎ Telefon nomer : {telnomer}\n💻 Texnologiya : {texnolog}\n📍 Manzil : {manzil}"
    malumotnoma += f"\n💲 Narxi : {narxi}\n👨🏻‍💻 Kaspi : {hunar}\n⏰ Murojat vaqti : {m_vaqti}\n🔎 Maqsadi : {fikri}\n"
    malumotnoma += f"\n  <b> #Shogird   #{manzil}</b>\n"

    for hsh in q1:
        sqlit = hsh.strip()
        malumotnoma += f" #{sqlit}, "



    msg = "Malumotlaringiz Tayyor\nAdminga yuboraymi ???"

    await state.update_data(ikkinchi3 = malumotnoma)
    await ms.answer(malumotnoma)
    await ms.answer(msg,reply_markup=hayoq)
    await Ustoz.admin_yubor.set()


## ha knopka bosilsa
## quyidagilar amalga oshadi

@dp.callback_query_handler(text="ha",state=Ustoz.admin_yubor)
async def ybma(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    malumotnoma = date.get("ikkinchi3")

    await call.message.answer("Malumotlar adminga yuorildi 🚚",reply_markup=strt_uchun)
    await bot.send_message(chat_id=ADMIN,text=malumotnoma)
    await call.message.delete()
    await state.finish()

### yoq knopka bosilsa

@dp.callback_query_handler(text="yoq",state=Ustoz.admin_yubor)
async def ybma(call:CallbackQuery, state:FSMContext):
    await call.message.answer("So'rov yuborilmadi",reply_markup=strt_uchun)
    await call.message.delete()
    await state.finish()