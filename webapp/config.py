import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
base = os.path.join(basedir,'..','webapp.db')
print(base)
WEATHER_DEFAULT_CITY = 'Riga,Latvia'
WEATHER_API_KEY = 'f9141aba3524472aac3195633202505'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ base
SECRET_KEY = "asjdlkajsdklj3423mn9i0-2;lk31;m.msdm.a,"
REMEMBER_CUCIES_SAVE = timedelta(days=5)
SQLALCHEMY_TRACK_MODIFICATIONS = False