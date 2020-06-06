from flask import Flask, render_template
import locale
from webapp.weather import weather_city
from datetime import datetime
from webapp.python_org_news import get_python_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = "Новости Python"
        locale.setlocale(locale.LC_ALL, "ru")
        news_list = get_python_news()
        weather_c = weather_city(app.config['WEATHER_DEFAULT_CITY'])
        if weather_c == False:
            return "Sorry,something went wrong"
        else:
            city_now = weather_c[0]["query"]
            weather_now = weather_c[1]["temp_C"]
            date = datetime.now().strftime('%a %d/%m/%Y')
        return render_template('index.html', page_title=title, city=city_now, weather_c=weather_now, date=date, news_list= news_list)
    return app
