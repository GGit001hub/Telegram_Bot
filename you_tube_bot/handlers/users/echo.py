from aiogram import types
from aiogram.dispatcher import FSMContext
from deep_translator import GoogleTranslator as trans


from loader import dp
from keyboards.default.keyingi import bir_key,ikki_key,uch_key
from states.poisk import Turlar
from .video_srch import get_video,malumots, get_video2, get_video3, malumots2, malumots3








@dp.message_handler(state=Turlar.video,text="👉 Keyingi sahifa 👉")
async def keyin_bir(ms:types.Message, state:FSMContext):
    data = await state.get_data()
    xabar = data.get('msg')

    title = malumots2(xabar)
    vid = get_video2(xabar)
    await state.update_data(tit1 = title)
    await state.update_data(vid1 = vid)

    await ms.answer(vid)
    await ms.answer(title,reply_markup=ikki_key)
    await Turlar.video.set()






@dp.message_handler(state=Turlar.video,text="👉 Keyingi 👉")
async def keyin_bir(ms:types.Message, state:FSMContext):
    data = await state.get_data()
    xabar = data.get('msg')

    title = malumots3(xabar)
    vid = get_video3(xabar)

    await ms.answer(vid)
    await ms.answer(title,reply_markup=uch_key)
    await Turlar.video.set()




@dp.message_handler(state=Turlar.video,text="👈 Avvalgi 👈")
async def keyin_bir(ms:types.Message, state:FSMContext):
    data = await state.get_data()

    title = data.get("av_title")
    vid = data.get("av_vid")

    await ms.answer(vid)
    await ms.answer(title,reply_markup=bir_key)
    await Turlar.video.set()





@dp.message_handler(state=Turlar.video,text="👈 Oldingi 👈")
async def keyin_bir(ms:types.Message, state:FSMContext):
    data = await state.get_data()

    title = data.get("tit1")
    vid = data.get("vid1")

    await ms.answer(vid)
    await ms.answer(title,reply_markup=ikki_key)
    await Turlar.video.set()






@dp.message_handler(state=Turlar.video)
async def vigetpost(ms:types.Message, state:FSMContext):

    xabar = trans(source='auto',target='en').translate(ms.text)
    vid = get_video(xabar)
    test = malumots(xabar)
    
    await state.update_data(av_title =test)
    await state.update_data(av_vid = vid)
    await state.update_data(msg = xabar)

    await ms.answer(vid)
    await ms.answer(test,reply_markup=bir_key)
    await Turlar.video.set()


