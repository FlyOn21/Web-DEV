from webapp import create_app
from webapp.python_org_news import get_python_news
from webapp.news.parsers.habr import get_news_snippets,get_news_content
app = create_app()
with app.app_context():
    get_python_news()
    get_news_snippets()
    get_news_content()


