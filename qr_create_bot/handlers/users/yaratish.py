from aiogram.types import Message
from loader import dp
import asyncio

from states.bitta import Holat
import requests
import json



@dp.message_handler(text="✅ QR cod yaratish")
async def yaratsn(ms:Message):
    print(ms.text,ms.from_user.full_name)
    msg = "🤖 <b>Bot jo'natilgan xabarga QR cod yaratib beradi</b>\n💡 QR cod yaratish uchun \
        \n📃 Matlar yoki Linklar jo'nating"
    await ms.answer(msg)
    await Holat.yaratish.set()




@dp.message_handler(state=Holat.yaratish)
async def asdasd(ms:Message):
    print(ms.text,ms.from_user.full_name)
    xabar = ms.text
    url = "https://easy-qr-code-generator.p.rapidapi.com/v1/generateqr"
    querystring = {"text":f"{xabar} ","width":"200"}
    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "easy-qr-code-generator.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    date = json.loads(response.text)
    rasm = (date['data'])

    await ms.answer_photo(photo=rasm)
    await Holat.kutish.set()


@dp.message_handler(state=Holat.kutish)
async def mazaqil(ms:Message):
    msg = f"❌ Kechirasiz {ms.from_user.full_name} 😔\
        \n🕙 Har 15 soniyada bitta chiqarish imkoni bor xolos\
        \n☺ 15 soniyadan keyin urunib ko'ring ‼"
    await ms.answer(msg)
    print(ms.text,ms.from_user.full_name)
    await asyncio.sleep(15)
    await Holat.yaratish.set()
    
