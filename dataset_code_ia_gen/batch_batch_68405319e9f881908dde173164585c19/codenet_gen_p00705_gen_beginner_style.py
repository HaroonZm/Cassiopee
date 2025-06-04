while True:
    line = input()
    if line == '0 0':
        break
    N, Q = map(int, line.split())
    date_count = {}
    for _ in range(N):
        data = input().split()
        M = int(data[0])
        if M > 0:
            dates = list(map(int, data[1:]))
            for d in dates:
                if d in date_count:
                    date_count[d] += 1
                else:
                    date_count[d] = 1
    best_date = 0
    max_count = 0
    for d in date_count:
        if date_count[d] >= Q:
            if date_count[d] > max_count or (date_count[d] == max_count and d < best_date):
                max_count = date_count[d]
                best_date = d
    print(best_date)