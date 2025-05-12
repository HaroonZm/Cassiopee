while 1:
    n, m = map(int, input().split())
    if n == 0:
        break

    data = []
    for _ in range(n):
        d, p = map(int, input().split())
        data.append([d, p])

    data = sorted(data, key=lambda x: -x[1])
    for d in data:
        if m <= 0:
            break
        if d[0] <= m:
            m -= d[0]
            d[0] = 0
        else:
            d[0] -= m
            m = 0

    ans = 0
    for d in data:
        ans += d[0] * d[1]

    print(ans)