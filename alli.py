import requests
from bs4 import BeautifulSoup
def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException,ValueError):
        return False

def get_python_news():
    session = requests.Session()
    data = {"login_username":"zhogolevpv@gmail.com", "login_password":"Gfdtk2105"}
    url = "https://track.aliexpress.com/logisticsdetail.htm?spm=a2g0s.9042647.4.4.59664c4d4YRFkt&tradeId=8010764834264263"
    response = session.post(url, data=data)
    print (response)
    html = get_html("https://aliexpress.ru/af/%25D1%2587%25D0%25BF%25D1%2583-%25D0%25BA%25D0%25BE%25D0%25BC%25D0%25BF%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2582%25D1%2583%25D1%258E%25D1%2589%25D0%25B8%25D0%25B5.html?d=y&origin=n&SearchText=%D1%87%D0%BF%D1%83+%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%82%D1%83%D1%8E%D1%89%D0%B8%D0%B5&catId=0&initiative_id=AS_20200530032424")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find_all()
        print(all_news)
        result_news = []
        # for news in all_news:
        #     title = news.find('a').text
        #     # print(title)
        #     url = news.find('a')['href']
        #     publeshd = news.find('time').text
        #     # print(url)
        #     # print(publeshd)
        #     result_news.append({'title': title , 'url':url, 'publeshd':publeshd})
        return result_news
        # all_news = all_news.find_all('li')
        # print(all_news)
    return False

if __name__ == "__main__":
    html = get_html("https://aliexpress.ru/af/%25D1%2587%25D0%25BF%25D1%2583-%25D0%25BA%25D0%25BE%25D0%25BC%25D0%25BF%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2582%25D1%2583%25D1%258E%25D1%2589%25D0%25B8%25D0%25B5.html?d=y&origin=n&SearchText=%D1%87%D0%BF%D1%83+%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%82%D1%83%D1%8E%D1%89%D0%B8%D0%B5&catId=0&initiative_id=AS_20200530032424")
    if html:
        with open ("alli.html",'w',encoding='utf-8') as file:
            file.write(html)
    c = get_python_news()
    print(c)
