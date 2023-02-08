from aiogram.types import Message
from loader import dp
import requests
import json

# from .api import namangan


@dp.message_handler(state=None)
async def namxona(ms:Message):
    await ms.answer("malumotlar")
    smg = ms.text

    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":f"{smg}","format":"json","u":"c"}

    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    date = json.loads(response.text)
    # havo = (date['current_observation']['condition']['temperature'])

    malumotlar = f"Shahar : {date['location']['city']}\
        \nTemparatura : \
         \nQuyosh chiqishi : {date['current_observation']['astronomy']['sunrise']}"
    
    await ms.answer(malumotlar)



