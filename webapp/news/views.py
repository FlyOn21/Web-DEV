from flask import Blueprint,render_template,current_app
import locale
from datetime import datetime
from webapp import weather_city
from webapp.news.models import News




blueprint= Blueprint('news',__name__)

@blueprint.route('/')
def index():
    title = "Новости Python"
    locale.setlocale(locale.LC_ALL,"ru_RU.UTF-8")
    news_list = News.query.order_by(News.published.desc()).all()
    weather_c = weather_city(current_app.config['WEATHER_DEFAULT_CITY'])
    if weather_c == False:
        return "Sorry,something went wrong"
    else:
        city_now = weather_c[0]["query"]
        weather_now = weather_c[1]["temp_C"]
        date = datetime.now().strftime('%a %d/%m/%Y')
    return render_template('news/index.html', page_title=title, city=city_now, weather_c=weather_now, date=date,
                           news_list=news_list)