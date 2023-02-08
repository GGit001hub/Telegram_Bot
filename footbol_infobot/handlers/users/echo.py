from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext

from .api import birinchi_xb,ikkinchi_xb,uchinchi_xb
from keyboards.default.sledushiy import keys, keys_keyin, oldingi
from states.holat import Doimiy


## keyingi sahifa uchun handler
## 2-malumotga qaytadi

@dp.message_handler(text="👉 Keyingi sahifa 👉",state=Doimiy.xabar)
async def keyingi(ms: types.Message, state:FSMContext):
    date = await state.get_data()
    xabar = date.get("kelgan_xb")
    iki_xbr = ikkinchi_xb(xabar)

    await state.update_data(xbr2 = iki_xbr)
    await ms.answer(iki_xbr,reply_markup=keys_keyin)
    await Doimiy.xabar.set()





## keyingi malumotga qaytish uchun handler
## 3 - malumotga qaytadi


@dp.message_handler(text="👉 Keyingi 👉",state=Doimiy.xabar)
async def keyingi(ms: types.Message, state:FSMContext):
    date = await state.get_data()
    xabar = date.get("kelgan_xb")

    uhc_xbr = uchinchi_xb(xabar)
    await ms.answer(uhc_xbr,reply_markup=oldingi)
    await Doimiy.xabar.set()


### uchinchi xabarda turib
### oldingi bosilsa chiqadigan message

@dp.message_handler(text="👈 oldingi 👈",state=Doimiy.xabar)
async def keyingi(ms: types.Message, state:FSMContext):
    date = await state.get_data()
    xabar = date.get("xbr2")
    await ms.answer(xabar,reply_markup=keys_keyin)

    await Doimiy.xabar.set()



### orqaga qaytish uchun handler
### quyidagi kodda yozilgan


@dp.message_handler(text="👈 Avvalgi 👈",state=Doimiy.xabar)
async def keyingi(ms: types.Message, state:FSMContext):
    date = await state.get_data()
    xabar = date.get("birinchi")
    await ms.answer(xabar,reply_markup=keys)

    await Doimiy.xabar.set()


@dp.message_handler(text="🔎 Qidirish 🔎",state=Doimiy.xabar)
async def keyingi(ms: types.Message, state:FSMContext):
    await ms.answer("qidirish / yoqildi")

    await Doimiy.xabar.set()






# Echo bot
# @dp.message_handler(state=None)
@dp.message_handler(state=Doimiy.xabar)
async def bot_echo(ms: types.Message, state: FSMContext):
    msg =ms.text
    dates = birinchi_xb(msg)
    await state.update_data(kelgan_xb = msg)
    await state.update_data(birinchi = dates)

    await ms.answer(dates,reply_markup=keys)
    await Doimiy.xabar.set()









