from flask import jsonify, request

from app.forms.book import SearchForm
from app.view_models.book import BookViewModel
from app.web import web
from app.spider.bookApi import Book
from app.libs.helper import is_isbn_or_key


@web.route('/book/search')
def search():
    res = {}
    form = SearchForm(request.args)
    if  form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            res = Book.search_by_isbn(q)
            res = BookViewModel.package_single(res,q)
        if isbn_or_key == 'key':
            res = Book.search_by_keyword(q,page)
            res = BookViewModel.package_collection(res,q)
        return jsonify(res)
    else:
        return jsonify({'msg':'参数有误'})
