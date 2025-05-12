while 1:
    t, d, l = map(int, raw_input().split())
    if t == d == l == 0:
        break
    rest = ans = 0
    for i in xrange(t):
        x = int(raw_input())
        if l <= x:
            rest = d
        elif rest:
            rest -= 1
        if rest and i < t-1:
            ans += 1
    print ans