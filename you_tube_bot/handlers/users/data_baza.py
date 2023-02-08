from aiogram.types import Message
from loader import dp
from states.poisk import Turlar
from .start import Data_Baza


@dp.message_handler(text="baza_haqida",state=Turlar.all_states_names,user_id=1173831936)
@dp.message_handler(text="baza_haqida",user_id=1173831936)
async def malumot(ms:Message):
    tr = 0
    malumotlar = ""
    for name,userid, in Data_Baza.items():
        tr += 1
        malumotlar += f"{tr}) <b>{name}</b>  -  <code>{userid}</code>\n"
    await ms.answer(malumotlar)