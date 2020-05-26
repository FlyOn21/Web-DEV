from flask import Flask
import locale
from weather import weather_city
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    locale.setlocale(locale.LC_ALL, "ru")
    weather_1 = weather_city("Riga,latvia")
    city_now = weather_1[0]["query"]
    weather_now = weather_1[1]["temp_C"]
    date = datetime.now().strftime('%a %d/%m/%Y')
    return f"Погода на дуту {date}, Город {city_now} Температура воздуха {weather_now}C "


if __name__ == '__main__':
    app.run(debug=True)
