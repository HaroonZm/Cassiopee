while True:
    n = int(input())
    if n == 0:
        break
    lst = [list(map(int, input().split())) for _ in range(n)]
    lp, lq, lr, lc = map(int, input().split())
    flag = True
    for s, p, q, r in lst:
        if p <= lp and q <= lq and r <= lr and 4 * p + 9 * q + 4 * r <= lc:
            print(s)
            flag = False
    if flag:
        print("NA")