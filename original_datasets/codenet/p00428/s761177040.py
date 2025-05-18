while True:
    n, m = map(int, raw_input().split())
    if (n, m) == (0, 0):
        break
    r = [0] * m
    for i in range(n):
        q = map(int, raw_input().split())
        for j in range(m):
            r[j] -= q[j]
    r = sorted([(r[i],i+1)for i in range(m)])
    print ' '.join(map(str, [rr[1] for rr in r]))