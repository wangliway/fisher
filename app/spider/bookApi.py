from app.libs.myHttp import Http
from flask import current_app

class Book:
    # isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    per_page = 15
    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        return Http.get(url)

    @classmethod
    def search_by_keyword(cls, key, page):
        url = cls.keyword_url.format(key, current_app.config['PER_PAGE'], (page-1)*cls.per_page)
        return Http.get(url)
