while True:
    n, m = [int(_) for _ in raw_input().split()]
    if n == m == 0:
        break

    h = [int(raw_input()) for _ in xrange(n)]
    w = [int(raw_input()) for _ in xrange(m)]

    hs = {}

    for i in xrange(n):
        h0 = 0
        for j in xrange(i, n):
            h0 += h[j]
            hs[h0] = hs.get(h0, 0) + 1

    ans = 0

    for i in xrange(m):
        w0 = 0
        for j in xrange(i, m):
            w0 += w[j]
            ans += hs.get(w0, 0)

    print(ans)