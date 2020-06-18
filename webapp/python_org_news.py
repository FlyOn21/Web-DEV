import requests
from datetime import datetime
from bs4 import BeautifulSoup
from webapp.model import db,News


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
        # b = soup.stripped_strings
        # for soup_b in b:
        #     print(repr(soup_b))
        all_news = soup.find('ul', class_='list-recent-posts menu').find_all('li')
        # result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            publeshd = news.find('time').text
            # print(publeshd)
            try:
                publeshd = datetime.strptime(publeshd,'%B %d, %Y')
            except:
                publeshd = datetime.now()
            save_news(title = title, url=url, published=publeshd)
        #     result_news.append({'title': title, 'url': url, 'publeshd': publeshd})
        # return result_news
        # all_news = all_news.find_all('li')
        # print(all_news)
    # return False

def save_news(title, url, published):
    news_exists =  News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        news_n = News(title = title, url = url, published = published)
        db.session.add(news_n)
        db.session.commit()


if __name__ == "__main__":
    # html = get_html("https://www.python.org/blogs/")
    # if html:
    #     with open ("python_org.html",'w',encoding='utf-8') as file:
    #         file.write(html)
    c = get_python_news()
    print(c)
