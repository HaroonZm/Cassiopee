OK = 1
while OK:
    z = input()
    if z == 0: OK = 0 ; break
    top = None
    who = None
    for idx in xrange(z):
        _, hh, ww = [int(x) for x in raw_input().split()]
        x = float(hh) / 100
        q = ww/(x*x)
        t = abs(22-q)
        if not top:
            top = t
            who = idx
        elif t<top:
            top = t
            who = idx
    print who