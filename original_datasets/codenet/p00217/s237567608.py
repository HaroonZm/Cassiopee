while 1:
    n = int(input())
    if n == 0: break
    dmax = 0
    for i in range(n):
        p, d1, d2 = map(int, input().split())
        if d1+d2 > dmax: id, dmax = p, d1+d2
    print(id, dmax)