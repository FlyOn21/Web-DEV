import os

basedir = os.path.abspath(os.path.dirname(__file__))
base = os.path.join(basedir,'..','webapp.db')
WEATHER_DEFAULT_CITY = 'Riga,Latvia'
WEATHER_API_KEY = 'f9141aba3524472aac3195633202505'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ base
