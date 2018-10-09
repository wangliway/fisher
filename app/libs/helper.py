def is_isbn_or_key(q):
    bn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        bn_or_key = 'isbn'
    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 10 and short_q.isdigit:
        bn_or_key = 'isbn'
    return bn_or_key
