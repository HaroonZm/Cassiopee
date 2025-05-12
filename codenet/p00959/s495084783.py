n, t = map(int, raw_input().split())

mx = 0
s = 0
for i in xrange(n):
    x = input()
    mx = max(mx, x)
    r = t - s
    if r < 0:
        print 1
    else:
        ans = r / mx + 1
        if r % mx >= x:
            ans += 1
        print ans
    s += x