from itertools import product
while True:
    d, w = map(int, input().split())
    if d == 0:
        exit()

    ans = 0
    e = [list(map(int, input().split())) for _ in range(d)]
    for si, sj in product(range(1, d - 1), range(1, w - 1)):
        for ti, tj in product(range(si + 1, d), range(sj + 1, w)):
            mx = 0
            for i, j in product(range(si, ti), range(sj, tj)):
                mx = max(mx, e[i][j])
            mn = 100
            for i, j in product([si - 1, ti], range(sj - 1, tj + 1)):
                mn = min(mn, e[i][j])
            for i, j in product(range(si - 1, ti + 1), [sj - 1, tj]):
                mn = min(mn, e[i][j])
            if mx >= mn:
                continue

            tmp = 0
            for i, j in product(range(si, ti), range(sj, tj)):
                tmp += mn - e[i][j]
            ans = max(ans, tmp)
    print(ans)