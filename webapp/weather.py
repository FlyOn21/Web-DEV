import requests
from flask import current_app

"""http://api.worldweatheronline.com/premium/v1/weather.ashx?
key=f9141aba3524472aac3195633202505&q=Riga,
latvia&format=json&num_of_days=5&fx24=yes&showlocaltime=yes&lang=ru"""


def weather_city(city_name):
    global city, weather_city
    weather_url = current_app.config ['WEATHER_URL']
    params = {'key': current_app.config ['WEATHER_API_KEY'],
              'q': city_name,
              'format': 'json',
              'num_of_days': 5,
              'fx24': 'yes',
              'showlocaltime': 'yes',
              'lang': 'ru'
              }
    try:
        result = requests.get(weather_url, params=params)
        weather = result.json()
        if 'data' in weather:
            try:
                if 'request' in weather['data']:
                    city = weather['data']['request'][0]
                if 'current_condition' in weather['data']:
                    weather_city = weather['data']['current_condition'][0]
                # print(city,weather_city)
                return city, weather_city
            except(IndexError, TypeError):
                return False
        return False
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False


if __name__ == "__main__":
    weather = weather_city("Riga,latvia")
