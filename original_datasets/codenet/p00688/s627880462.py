from fractions import gcd
def func(a, b):
    if a < 0:
        return (-a, -b)
    return a, b
while True:
    a, b, c = map(int, raw_input().split())
    if (a, b, c) == (0, 0, 0):
        break
    try:
        d = (b**2 - 4*a*c)**0.5
        if not int(d) == d:
            raise
        e,f = map(int,(-b+d, -b-d))
        g = 2*a
        h = gcd(e, g)
        i = gcd(f, g)
        p, q = func(g/h, -e/h)
        r, s = func(g/i, -f/i)
        if (p < r) or (p == r and q < s):
            p, q, r, s = r, s, p, q
        print p, q, r, s
    except:
        print "Impossible"