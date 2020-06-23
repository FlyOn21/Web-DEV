import requests
from datetime import datetime
from bs4 import BeautifulSoup
from webapp.db import db
from webapp.news.models import News


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False


def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')

        all_news = soup.find('ul', class_='list-recent-posts menu').find_all('li')

        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            publeshd = news.find('time').text
            try:
                publeshd = datetime.strptime(publeshd,'%B %d, %Y')
            except:
                publeshd = datetime.now()
            save_news(title = title, url=url, published=publeshd)


def save_news(title, url, published):
    news_exists =  News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        news_n = News(title = title, url = url, published = published)
        db.session.add(news_n)
        db.session.commit()


if __name__ == "__main__":
    c = get_python_news()
    print(c)
