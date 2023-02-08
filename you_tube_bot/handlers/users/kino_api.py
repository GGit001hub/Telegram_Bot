import requests
import json
from deep_translator import GoogleTranslator as trans



def movie(kinolar):
    url = "https://ytube-videos.p.rapidapi.com/search-movies"
    querystring = {"q":f"{kinolar}","max":"10","lang":"EN"}
    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "ytube-videos.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    try:
        if response.status_code==200:
            date = json.loads(response.text)
            kino_url = (date[0]['shareLink'])
            return kino_url
        else:
            return 'Malumot topilmadi 😔'
    except IndexError:
        return "Bu haqida malumot topilmadi !"

def movi_title(m_title):
    url = "https://ytube-videos.p.rapidapi.com/search-movies"
    querystring = {"q":f"{m_title}","max":"10","lang":"EN"}
    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "ytube-videos.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    try:
        if response.status_code==200:
            date = json.loads(response.text)

            mesages = (date[0]['title'])
            send_title = trans(source='auto',target='uzbek').translate(mesages)
            send_views = (date[0]['views'])
            send_id = (date[0]['id'])
            send_durr = (date[0]['duration'])
            send_chanle = (date[0]['channel'])

            malumotlar = f"<b>Kino haqida</b> : {send_title}\n \
                \n⏸ Davomiyligi : {send_durr}\
                \n👁‍🗨 Ko'rishlar soni : {send_views}\
                \n🛠 Kino id : {send_id}\
                \n📜 Batafsil : <a href='{send_chanle}'>Kino haqida</a>"
            return malumotlar
        else:
            return "Kechirasiz malumot topilmadi"
    except IndexError:
        return "Kechirasiz malumot topilmadi"



#### ikinchi kino uchun handler
## ikki yoziladi 
## birdagi 0 o'rniga 1 qo'yiladi

def movie1(kinolar1):
    url = "https://ytube-videos.p.rapidapi.com/search-movies"
    querystring = {"q":f"{kinolar1}","max":"10","lang":"EN"}
    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "ytube-videos.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code==200:
        date = json.loads(response.text)
        kino_url = (date[1]['shareLink'])
        return kino_url
    else:
        return 'Malumot topilmadi 😔'

def movi_title1(m_title1):
    url = "https://ytube-videos.p.rapidapi.com/search-movies"
    querystring = {"q":f"{m_title1}","max":"10","lang":"EN"}
    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "ytube-videos.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code==200:
        date = json.loads(response.text)

        mesages = (date[1]['title'])
        send_title = trans(source='auto',target='uzbek').translate(mesages)
        send_views = (date[1]['views'])
        send_id = (date[1]['id'])
        send_durr = (date[1]['duration'])
        send_chanle = (date[1]['channel'])

        malumotlar = f"<b>Kino haqida</b> : {send_title}\n \
            \n⏸ Davomiyligi : {send_durr}\
             \n👁‍🗨 Ko'rishlar soni : {send_views}\
              \n🛠 Kino id : {send_id}\
               \n☝ Batafsil : <a href='{send_chanle}'>Kino haqida</a>"
        return malumotlar

    else:
        return "Kechirasiz malumot topilmadi"



#### uchinchi kino uchun handler
## uch yoziladi 
## ikkidagi 1 o'rniga 2 qo'yiladi

def movie2(kinolar2):
    url = "https://ytube-videos.p.rapidapi.com/search-movies"
    querystring = {"q":f"{kinolar2}","max":"10","lang":"EN"}
    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "ytube-videos.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code==200:
        date = json.loads(response.text)
        kino_url = (date[2]['shareLink'])
        return kino_url
    else:
        return 'Malumot topilmadi 😔'

def movi_title2(m_title2):
    url = "https://ytube-videos.p.rapidapi.com/search-movies"
    querystring = {"q":f"{m_title2}","max":"10","lang":"EN"}
    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "ytube-videos.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code==200:
        date = json.loads(response.text)

        mesages = (date[2]['title'])
        send_title = trans(source='auto',target='uzbek').translate(mesages)
        send_views = (date[2]['views'])
        send_id = (date[2]['id'])
        send_durr = (date[2]['duration'])
        send_chanle = (date[2]['channel'])

        malumotlar = f"<b>Kino haqida</b> : {send_title}\n \
            \n⏸ Davomiyligi : {send_durr}\
             \n👁‍🗨 Ko'rishlar soni : {send_views}\
              \n 🆔Kino id : {send_id}\
               \n🤭 Batafsil : <a href='{send_chanle}'>Kino haqida</a>"
        return malumotlar

    else:
        return "Kechirasiz malumot topilmadi"
