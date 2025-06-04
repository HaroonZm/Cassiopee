n = int(input())
books = []
for _ in range(n):
    books.append(input().split())
q = int(input())
i = 0
while i < q:
    temp = input().split()
    qt = temp[0]
    qa = temp[1]
    qdf = temp[2]
    qdt = temp[3]
    j = 0
    while j < len(books):
        title = books[j][0]
        auther = books[j][1]
        date = books[j][2]
        cond1 = (qt == "*" or qt in title)
        cond2 = (qa == "*" or qa in auther)
        cond3 = (qdf == "*" or qdf <= date)
        cond4 = (qdt == "*" or date <= qdt)
        if cond1 and cond2 and cond3 and cond4:
            print(title)
        j += 1
    if i != q - 1:
        print()
    i += 1