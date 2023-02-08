from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from deep_translator import GoogleTranslator as trans
from loader import dp

from states.poisk import Turlar
from .kanal_api import kanal_name


@dp.message_handler(state=Turlar.kanall)
async def fff(ms:Message):
    xabar = trans(source='auto',target='en').translate(ms.text)
    date = kanal_name(xabar)
    await ms.answer(date)
    await Turlar.kanall.set()
