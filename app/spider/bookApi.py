from app.libs.myHttp import Http
from flask import current_app


class Book:
    # isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    per_page = 15

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        res = Http.get(url)
        self.__fill_single(res)

    def search_by_keyword(self, key, page):
        url = self.keyword_url.format(key, current_app.config['PER_PAGE'], (page - 1) * self.per_page)
        res = Http.get(url)
        self.__fill_collection(res)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']
