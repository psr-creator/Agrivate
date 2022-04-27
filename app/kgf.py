import requests
import json


def get_temp_humidity(lat="9.931233",lon="76.267303"):
    key="f148895aed51ec16916d10d139f1416a"
    test=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&APPID={key}"
    V=requests.get(test)
    value=json.loads(V.text)
    humidity=value["main"]["humidity"]
    temperature=value["main"]["temp"]
    values=[]
    values.append(humidity)
    values.append(temperature)
    return values