from flask import Flask,render_template
import locale
from weather import weather_city
from datetime import datetime
from python_org_news import get_python_news

app = Flask(__name__)


@app.route('/')
def index():
    title = "Новости Python"
    locale.setlocale(locale.LC_ALL, "ru")
    news_list = get_python_news()
    weather_1 = weather_city("Riga,latvia")
    if weather_1 == False:
        return "Sorry,something went wrong"
    else:
        city_now = weather_1[0]["query"]
        weather_now = weather_1[1]["temp_C"]
        date = datetime.now().strftime('%a %d/%m/%Y')
    #     weather_2 =  f"Погода на дату {date}, Город {city_now} Температура воздуха {weather_now}C "
    return render_template('index.html',page_title = title, city = city_now, weather_1 = weather_now, date = date, news_list = news_list )
        




if __name__ == '__main__':
    app.run(debug=True)
