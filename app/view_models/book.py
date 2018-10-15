class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        return_data = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            return_data['total'] = 1
        return_data['books'] = [cls.__cut_book_data(data)]
        return return_data

    @classmethod
    def package_collection(cls, data, keyword):
        return_data = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            return_data['total'] = len(data['total'])
            return_data['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return data

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return  book
