import requests
from datetime import datetime,timedelta
from bs4 import BeautifulSoup
import locale
import platform
from webapp.db import db
from webapp.news.models import News

if platform.system() == 'Windows':
    locale = locale.setlocale(locale.LC_ALL, 'russian')
else:
    locale = locale.setlocale(locale.LC_ALL,'ru_RU.utf8')

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:65.0) Gecko/20100101 Firefox/65.0'
    }
    try:
        result = requests.get(url,headers = headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False

def save_news(title, url, published):
    news_exists =  News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        news_n = News(title = title, url = url, published = published)
        db.session.add(news_n)
        db.session.commit()

def parse_habr_date(date_str):
    if 'сегодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    elif 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
    try:
        return datetime.strptime(date_str, '%d %B %Y в %H:%M')
    except ValueError:
        return datetime.now()