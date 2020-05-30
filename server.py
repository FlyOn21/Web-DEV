from flask import Flask,render_template
import locale
from weather import weather_city
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    title = "Прогноз погоды"
    locale.setlocale(locale.LC_ALL, "ru")
    weather_1 = weather_city("Riga,latvia")
    # if weather_1 == False:
    #     weather_2 = "Sorry,something went wrong"
    # else:
    #     city_now = weather_1[0]["query"]
    #     weather_now = weather_1[1]["temp_C"]
    #     date = datetime.now().strftime('%a %d/%m/%Y')
    #     weather_2 =  f"Погода на дату {date}, Город {city_now} Температура воздуха {weather_now}C "
    return render_template('index.html',page_title = title, weather_1 = weather_1 )
        




if __name__ == '__main__':
    app.run(debug=True)
