N = int(input())
books = []
i = 0
while i < N:
    parts = input().split()
    title = parts[0]
    author = parts[1]
    date = parts[2]
    date = list(map(int, date.split('/')))
    books.append((title, author, date))
    i += 1

Q = int(input())
i = 0
while i < Q:
    parts = input().split()
    title = parts[0]
    author = parts[1]
    date_from = parts[2]
    date_to = parts[3]

    use_date_from = True
    use_date_to = True
    if date_from != '*':
        date_from_v = list(map(int, date_from.split('/')))
    else:
        use_date_from = False
    if date_to != '*':
        date_to_v = list(map(int, date_to.split('/')))
    else:
        use_date_to = False

    resp = []
    j = 0
    while j < len(books):
        book = books[j]
        title_ok = (title == '*' or title in book[0])
        author_ok = (author == '*' or author in book[1])
        date_from_ok = True
        if use_date_from:
            if book[2] < date_from_v:
                date_from_ok = False
        date_to_ok = True
        if use_date_to:
            if book[2] > date_to_v:
                date_to_ok = False
        if title_ok and author_ok and date_from_ok and date_to_ok:
            resp.append(book)
        j += 1

    k = 0
    while k < len(resp):
        print(resp[k][0])
        k += 1

    if i + 1 < Q:
        print()
    i += 1