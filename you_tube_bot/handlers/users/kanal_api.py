import requests
import json

def kanal_name(kiriting):
    url = "https://ytube-videos.p.rapidapi.com/search-channel"
    querystring = {"q":f"{kiriting}","max":"10","lang":"EN"}
    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "ytube-videos.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    try:
        if response.status_code==200:
                date = json.loads(response.text)
                k_link = (date[0]['link'])
                k_name = (date[0]['name'])

                k_link1 = (date[1]['link'])
                k_name1 = (date[1]['name'])

                k_link2 = (date[-1]['link'])
                k_name2 = (date[-1]['name'])

                malumotlar = f"<b>Malumot bo'yicha</b>\n \
                    \n1 - <a href = '{k_link}'>{k_name}</a>\
                    \n2 - <a href = '{k_link1}'>{k_name1}</a>\
                    \n3 - <a href = '{k_link2}'>{k_name2}</a>\n \
                    \n👆 Shular topildi ☝"
                return malumotlar
        else:
            return "Kechirasi malumot topilmadi !!!"
    except IndexError:
        return "Malumotlar tomilmadi 😔"
