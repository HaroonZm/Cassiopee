from bisect import *
while 1:
    n, lmt = map(int, raw_input().split())
    if n == 0: break
    p = [input() for i in range(n)] + [0]
    p = sorted(set(i + j for i in p for j in p))
    s = bisect(p, lmt)
    print max(i + p[bisect(p, lmt - i) - 1] for i in p[:s])