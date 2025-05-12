def main():
    N = int(input())
    books = []
    for i in range(N):
        title, author, date = input().split()
        date = list(map(int, date.split('/')))
        books.append((title, author, date))

    Q = int(input())
    for i in range(Q):
        title, author, date_from, date_to = input().split()
        if date_from != '*':
            date_from = list(map(int, date_from.split('/')))
        if date_to != '*':
            date_to = list(map(int, date_to.split('/')))

        resp = books[:]
        resp = [book for book in resp if title == '*' or title in book[0]]
        resp = [book for book in resp if author == '*' or author in book[1]]
        resp = [book for book in resp if date_from == '*' or date_from <= book[2]]
        resp = [book for book in resp if date_to == '*' or date_to >= book[2]]

        for book in resp:
            print(book[0])

        if i+1 < Q:
            print()

main()