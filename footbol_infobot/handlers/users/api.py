import requests
import json


def birinchi_xb(xabar):
    try:
        url = f"https://footapi7.p.rapidapi.com/api/search/{xabar}"
        headers = {
            "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
            "X-RapidAPI-Host": "footapi7.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers)

        if response.status_code==200:
            date = json.loads(response.text)
            turi = (date['results'][0]['type'])
            if turi == "player":
                result = f"💯 <b> O'yinchi haqida </b> 🏃 \n \
                \n✅ ismi : {date['results'][0]['entity']['name']}\
                    \n👕 qisqa ismi : {date['results'][0]['entity']['shortName']}\
                    \n📛 jamoasi : {date['results'][0]['entity']['team']['name']}\
                    \n📊 ball : {date['results'][0]['score']} \
                    \n🗽 davlati : {date['results'][0]['entity']['country']['name']}"
                return result
            elif turi == 'team':
                title = f"💯 <b> Jamoa haqida </b> 🏃 \n \
                    \n✅ Jamoa nomi : {date['results'][0]['entity']['name']}\
                    \n👕 Qisqa nomi : {date['results'][0]['entity']['shortName']}\
                    \n📊 Jamoa balli : {date['results'][0]['score']} \
                    \n💡 Id raqami : {date['results'][0]['entity']['id']}\
                        \n🌍 Jamoa davlati : {date['results'][0]['entity']['country']['name']}"
                return title

            else:
                return f"Kechirasiz 😞\n{xabar} haqida malumot topilmadi !"
    except KeyError:
        return "Kechirasiz malumot topilmadi 😔"
    except IndexError:
        return "So'rov bo'yicha malumot topilmadi !!"
### ikkinchi xabar uchun handler
### keyingi bosilsa chiqadigan message

def ikkinchi_xb(xbr2):
    try:
        url = f"https://footapi7.p.rapidapi.com/api/search/{xbr2}"
        headers = {
            "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
            "X-RapidAPI-Host": "footapi7.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers)

        if response.status_code==200:
            date = json.loads(response.text)
            turi = (date['results'][1]['type'])
            if turi == "player":
                result = f"💯 <b> O'yinchi haqida </b> 🏃 \n \
                \n✅ ismi : {date['results'][1]['entity']['name']}\
                    \n👕 qisqa ismi : {date['results'][1]['entity']['shortName']}\
                    \n📛 jamoasi : {date['results'][1]['entity']['team']['name']}\
                    \n📊 ball : {date['results'][1]['score']} \
                    \n🗽 davlati : {date['results'][1]['entity']['country']['name']}"
                return result
            elif turi == 'team':
                title = f"💯 <b> Jamoa haqida </b> 🏃 \n \
                    \n✅ Jamoa nomi : {date['results'][1]['entity']['name']}\
                    \n👕 Qisqa nomi : {date['results'][1]['entity']['shortName']}\
                    \n📊 Jamoa balli : {date['results'][1]['score']} \
                    \n🆔 Id raqami : {date['results'][1]['entity']['id']}\
                        \n🌍 Jamoa davlati : {date['results'][1]['entity']['country']['name']}"
                return title
            else:
                return f"Kechirasiz 😞\n{xbr2} haqida malumot topilmadi !"
    except KeyError:
        return "Kechirasiz malumot topilmadi 😔"
    except IndexError:
        return "So'rov bo'yicha malumot topilmadi !!"

### uchinchi xabar uchun message 
## hozir yozilmoqda


def uchinchi_xb(xbr3):
    try:
        url = f"https://footapi7.p.rapidapi.com/api/search/{xbr3}"
        headers = {
            "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
            "X-RapidAPI-Host": "footapi7.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers)

        if response.status_code==200:
            date = json.loads(response.text)
            turi = (date['results'][2]['type'])
            if turi == "player":
                result = f"💯 <b> O'yinchi haqida </b> 🏃 \n \
                \n✅ ismi : {date['results'][2]['entity']['name']}\
                    \n👕 qisqa ismi : {date['results'][2]['entity']['shortName']}\
                    \n📛 jamoasi : {date['results'][2]['entity']['team']['name']}\
                    \n📊 ball : {date['results'][2]['score']} \
                    \n🗽 davlati : {date['results'][2]['entity']['country']['name']}"
                return result
            elif turi == 'team':
                title = f"💯 <b> Jamoa haqida </b> 🏃 \n \
                    \n✅ Jamoa nomi : {date['results'][2]['entity']['name']}\
                    \n👕 Qisqa nomi : {date['results'][2]['entity']['shortName']}\
                    \n📊 Jamoa balli : {date['results'][2]['score']} \
                    \n💡 Id raqami : {date['results'][2]['entity']['id']}\
                        \n🌍 Mamlakati : {date['results'][2]['entity']['country']['name']}"
                return title

            else:
                return f"Kechirasiz 😞\n{xbr3} haqida malumot topilmadi !"
    except KeyError:
        return "Kechirasiz malumot topilmadi 😔"
    except IndexError:
        return "So'rov bo'yicha malumot topilmadi !!"





# import json
# import requests

# def namangan(xabar):

#         url = f"https://footapi7.p.rapidapi.com/api/search/{xabar}"

#         headers = {
#             "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
#             "X-RapidAPI-Host": "footapi7.p.rapidapi.com"
#         }
        
#         response = requests.request("GET", url, headers=headers)

#         date = json.loads(response.text)
#         vaqt = (date['items'][0]['fajr'])

#         malumot =  f"Viloyat Namangan\n {vaqt}"
#         return malumot


