import requests
import json


def obhavo(shahar):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":f"{shahar}","format":"json","u":"c"}

    headers = {
        "X-RapidAPI-Key": "77beb71763msh010c8f2f00621b0p1875efjsn00a73e3c7e4a",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    date = json.loads(response.text)


