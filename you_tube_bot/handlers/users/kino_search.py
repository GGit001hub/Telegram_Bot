from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from deep_translator import GoogleTranslator as trans
from loader import dp

from .kino_api import movie,movie1,movie2
from .kino_api import movi_title,movi_title1,movi_title2
from states.poisk import Turlar
from keyboards.default.keyingi import ikki_key, bir_key, uch_key,starts





@dp.message_handler(state=Turlar.all_states_names,text="👆 Bosh sahifa ☝")
async def bshsahifa(ms:Message, state:FSMContext):
    await ms.answer("Bosh sahifa",reply_markup=starts)
    await state.finish()






@dp.message_handler(text="Kino Qidirish")
@dp.message_handler(state=Turlar.all_states_names,text="Kino Qidirish")
async def ksonni(ms:Message):
    await ms.answer("Kinolar nomini kiriting ✅\nKeyin malumotga ega bo'lasiz 📜")
    await Turlar.kino.set()




@dp.message_handler(state=Turlar.kino, text="👉 Keyingi sahifa 👉")
async def keykino(ms:Message, state:FSMContext):
    date = await state.get_data()
    vsf = date.get("user_xabar")
    videa = movie1(vsf)
    title = movi_title1(vsf)

    await state.update_data(kinourl1 = videa)
    await state.update_data(kinotitle1 = title)
    await ms.answer(videa)
    await ms.answer(title,reply_markup=ikki_key)

    await Turlar.kino.set()


@dp.message_handler(state=Turlar.kino, text="👉 Keyingi 👉")
async def keykino(ms:Message, state:FSMContext):
    date = await state.get_data()
    vsf = date.get("user_xabar")
    videa = movie2(vsf)
    title = movi_title2(vsf)

    await state.update_data(kinourl2 = videa)
    await state.update_data(kinotitle2 = title)
    await ms.answer(videa)
    await ms.answer(title,reply_markup=uch_key)

    await Turlar.kino.set()



@dp.message_handler(state=Turlar.kino, text="👈 Oldingi 👈")
async def keykino(ms:Message, state:FSMContext):
    date = await state.get_data()
    videa = date.get("kinourl1")
    title =date.get("kinotitle1")

    await state.update_data(kinourl1 = videa)
    await state.update_data(kinotitle1 = title)
    await ms.answer(videa)
    await ms.answer(title,reply_markup=ikki_key)

    await Turlar.kino.set()








@dp.message_handler(state=Turlar.kino, text="👈 Avvalgi 👈")
async def keykino(ms:Message, state:FSMContext):
    date = await state.get_data()
    videa = date.get("kinourl1")
    title =date.get("kinotitle1")

    await state.update_data(kinourl = videa)
    await state.update_data(kinotitle = title)
    await ms.answer(videa)
    await ms.answer(title,reply_markup=ikki_key)

    await Turlar.kino.set()












@dp.message_handler(state=Turlar.kino)
async def search_kinno(ms:Message, state:FSMContext):
    await state.finish()
    vsf = trans(source='auto',target='en').translate(ms.text)
    await state.update_data(user_xabar = vsf)

    vid_url = movie(vsf)
    title = movi_title(vsf)

    await state.update_data(kinourl = vid_url)
    await state.update_data(kinotitle = title)
    await ms.answer(vid_url)
    await ms.answer(title,reply_markup=bir_key)

    await Turlar.kino.set()












