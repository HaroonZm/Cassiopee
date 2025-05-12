while 1:
    n,m=map(int, input().split())
    if n == 0:
        break
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        c += min(m//n, a[i])
    print(c)