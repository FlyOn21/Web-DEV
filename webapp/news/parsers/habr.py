from bs4 import BeautifulSoup
from webapp.db import db
from webapp.news.models import News

from webapp.news.parsers.utils import get_html,save_news,parse_habr_date

def get_news_snippets():
    html = get_html("https://habr.com/ru/search/?target_type=posts&q=python&order_by=date")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='content-list_posts').find_all('li', class_='content-list__item_post')
        print(all_news)
        for news in all_news:
            title = news.find('a', class_='post__title_link').text
            print('------------',title)
            url = news.find('a', class_='post__title_link')['href']
            published = news.find('span', class_='post__time').text
            published = parse_habr_date(published)
            print(title, url, published)
            save_news(title=title,url=url,published=published)

def get_news_content():
    news_without_text = News.query.filter(News.text.is_(None))
    for news in news_without_text:
        html = get_html(news.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            article = soup.find('div', class_='post__text-html').decode_contents()
            if article:
                news.text = article
                db.session.add(news)
                db.session.commit()


if __name__ =="__main__":
    get_news_snippets()