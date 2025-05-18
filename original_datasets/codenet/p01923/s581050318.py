while 1:
    n, m = map(int, input().split())
    if n == 0:
        break
    s = [0]*(m+1)
    for _ in range(n):
        d, v = map(int, input().split())
        if s[d] < v:
            s[d] = v
    print(sum(s))