while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    p = sorted(list(map(int, input().split())))
    flag = 0 if p[0]==1 else 1
    print('{:.10f}'.format(n/2 if flag else 0))