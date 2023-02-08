import requests
import json
from deep_translator import GoogleTranslator as trans


def get_video(search):
    url = "https://ytube-videos.p.rapidapi.com/search-video"
    querystring = {"q":f"{search}","max":"10","lang":"EN"}
    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "ytube-videos.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    try:
        if response.status_code==200:
            date = json.loads(response.text)
            send_video = (date[0]['shareLink'])
            return send_video
        else:
            return "Kechirasiz malumot topilmadi"
    except IndexError:
        return "Bu mavzuda malumot topilmadi"


def malumots(xabar):
    url = "https://ytube-videos.p.rapidapi.com/search-video"
    querystring = {"q":f"{xabar}","max":"10","lang":"EN"}
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
            send_durr = (date[0]['duration'])
            send_chanle = (date[0]['channel'])

            malumotlar = f"📜 <b>Qisqacha malumot</b> : {send_title}\n \
                \n⏸ Davomiyligi : {send_durr} minn \
                \n👁 Ko'rishlar soni : {send_views} ta \
                \n📍 Batafsil : <a href='{send_chanle}'>Youtube manzili</a>"
            
            return malumotlar
        else:
            return "Kechirasiz Malumot topilmadi"
    except IndexError:
        return "Kechirasiz malumot topilmadi"



### malumot ikki uchun
### 0 o'rniga 1 qo'yiladi xolos
## tepadagini kopiyasi



def get_video2(qidur):
    url = "https://ytube-videos.p.rapidapi.com/search-video"
    querystring = {"q":f"{qidur}","max":"10","lang":"EN"}
    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "ytube-videos.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code==200:
        date = json.loads(response.text)
        send_video = (date[1]['shareLink'])
        return send_video
    else:
        return "Kechirasiz malumot topilmadi"


def malumots2(matn):
    url = "https://ytube-videos.p.rapidapi.com/search-video"
    querystring = {"q":f"{matn}","max":"10","lang":"EN"}
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
        send_durr = (date[1]['duration'])
        send_chanle = (date[1]['channel'])

        malumotlar = f"📜 <b>Qisqacha malumot</b> : {send_title}\n \
            \n⏸ Davomiyligi : {send_durr} minn \
             \n👁 Ko'rishlar soni : {send_views} ta \
              \n📍 Batafsil : <a href='{send_chanle}'>Youtube manzili</a>"
        
        return malumotlar
    else:
        return "Kechirasiz Malumot topilmadi"




### malumot uch uchun
### 1 o'rniga 2 qo'yiladi xolos
## tepadagini kopiyasi



def get_video3(pisok):
    url = "https://ytube-videos.p.rapidapi.com/search-video"
    querystring = {"q":f"{pisok}","max":"10","lang":"EN"}
    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "ytube-videos.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code==200:
        date = json.loads(response.text)
        send_video = (date[2]['shareLink'])
        return send_video
    else:
        return "Kechirasiz malumot topilmadi"


def malumots3(tixs):
    url = "https://ytube-videos.p.rapidapi.com/search-video"
    querystring = {"q":f"{tixs}","max":"10","lang":"EN"}
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
        send_durr = (date[2]['duration'])
        send_chanle = (date[2]['channel'])

        malumotlar = f"📜 <b>Qisqacha malumot</b> : {send_title}\n \
            \n⏸ Davomiyligi : {send_durr} minn \
             \n👁 Ko'rishlar soni : {send_views} ta \
              \n📍 Batafsil : <a href='{send_chanle}'>Youtube manzili</a>"
        
        return malumotlar
    else:
        return "Kechirasiz Malumot topilmadi"

