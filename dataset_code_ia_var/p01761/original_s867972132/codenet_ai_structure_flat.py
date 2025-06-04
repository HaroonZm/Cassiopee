N = int(input())
books = [input().split(" ") for i in range(N)]
Q = int(input())
query = [input().split(" ") for i in range(Q)]
dates = []
for _, _, date in books:
    dates.append(list(map(int, date.split("/"))))
for i in range(Q):
    Q_title = query[i][0]
    Q_author = query[i][1]
    Q_date_from = query[i][2]
    Q_date_to = query[i][3]
    if Q_title == "*":
        bit_title = (1<<(N+1))-1
    else:
        bit_title = 0
        for j in range(N):
            if Q_title in books[j][0]:
                bit_title |= 1 << j
    if Q_author == "*":
        bit_author = (1<<(N+1))-1
    else:
        bit_author = 0
        for j in range(N):
            if Q_author in books[j][1]:
                bit_author |= 1 << j
    if Q_date_from == "*":
        bit_date_from = (1<<(N+1))-1
    else:
        bit_date_from = 0
        Qf_y, Qf_m, Qf_d = map(int, Q_date_from.split("/"))
        for j in range(N):
            year, month, day = dates[j]
            if year > Qf_y:
                bit_date_from |= 1 << j
            elif year == Qf_y:
                if month > Qf_m:
                    bit_date_from |= 1 << j
                elif month == Qf_m:
                    if day >= Qf_d:
                        bit_date_from |= 1 << j
    if Q_date_to == "*":
        bit_date_to = (1<<(N+1))-1
    else:
        bit_date_to = 0
        Qt_y, Qt_m, Qt_d = map(int, Q_date_to.split("/"))
        for j in range(N):
            year, month, day = dates[j]
            if year < Qt_y:
                bit_date_to |= 1 << j
            elif year == Qt_y:
                if month < Qt_m:
                    bit_date_to |= 1 << j
                elif month == Qt_m:
                    if day <= Qt_d:
                        bit_date_to |= 1 << j
    bit = bit_title & bit_author & bit_date_from & bit_date_to
    for j in range(N):
        if bit & 1:
            print(books[j][0])
        bit >>= 1
    if i != Q-1:
        print()