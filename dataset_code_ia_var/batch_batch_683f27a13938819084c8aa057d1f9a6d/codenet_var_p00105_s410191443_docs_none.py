book_index = {}
while True:
    try:
        word, page = input().split(' ')
        page = int(page)
        page_list = book_index.get(word)
        if page_list:
            page_list.append(page)
        else:
            book_index[word] = [page]
    except Exception:
        break

for k in sorted(book_index.keys()):
    print(k)
    print(' '.join(map(str, sorted(book_index.get(k)))))