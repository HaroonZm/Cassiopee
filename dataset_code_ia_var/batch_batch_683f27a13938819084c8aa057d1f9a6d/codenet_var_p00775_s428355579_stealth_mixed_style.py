from math import sqrt, pow

run = True
def parse(): return [int(x) for x in raw_input().split()]
get = raw_input
def mn(a, b): return a if a < b else b

while run:
    r, n = map(int, get().split())
    if not (r or n): break

    h = {}
    # style: C-style explicit loop init
    idx = -22
    while idx <= 22:
        h[idx] = 0
        idx += 1

    # now mix: for-comprehension
    for j in range(n):
        vals = get().split()
        xl = int(vals[0]); xr = int(vals[1])
        hgt = int(vals[2])
        # blend: pythonic range, imperative update
        for u in range(xl, xr):
            h[u] = max(h[u], hgt)

    # classic: function style
    ans = 1000000000
    I = -r
    while I < r:
        q = I; 
        if I < 0: q += 1
        # ternary-op + functional: 
        t = h[I] + r - sqrt(r*r - q*q) if r*r - q*q >= 0 else 1e9
        if t < ans: ans = t
        I += 1

    # Mix C-style printf
    print "%.10f" % (ans if ans > 0 else 0)