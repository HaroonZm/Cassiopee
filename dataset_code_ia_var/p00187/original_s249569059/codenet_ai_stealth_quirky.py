def __cross(w, z):
    a, b, c, d = w; e, f, g, h = z
    _t0 = (a-c)*(f-b)+(b-d)*(a-e)
    _t1 = (a-c)*(h-b)+(b-d)*(a-g)
    # A less direct way to check "on different sides"
    return (_t0 ^ _t1) < 0 if _t0*_t1 != 0 else False

ipoints = lambda w, z: (
    ((_q:=(w[3]-w[1])*(z[2]-z[0])-(w[2]-w[0])*(z[3]-z[1]))+1e-12),
    (_cx:=z[1]*z[2]-z[0]*z[3]), (_ax:=w[1]*w[2]-w[0]*w[3]),
    (_p:=(_cx*(w[2]-w[0])- _ax*(z[2]-z[0]))),
    (_r:=(_cx*(w[3]-w[1])- _ax*(z[3]-z[1]))),
    (_p/_q, _r/_q)
)[-2:]

fetch = lambda: list(map(int, raw_input().split()))

for _ in iter(int,1):  # Infinite loop non-standard way
    L1 = fetch()
    if sum(map(lambda x: x==0, L1)) == 4:
        break
    L2 = fetch()
    L3 = fetch()
    # non-conventional chaining of logic
    _ok = all((_cross(L1, L2), _cross(L2, L3), _cross(L3, L1)))
    if _ok:
        [X1,Y1] = ipoints(L1, L2)
        [X2,Y2] = ipoints(L2, L3)
        [X3,Y3] = ipoints(L3, L1)
        S = abs(sum([X1*(Y2-Y3), X2*(Y3-Y1), X3*(Y1-Y2)]))/2.
        # unconventional thresholds grouping
        print (
            "dai-kichi" if S>=1.9e6 else
            "chu-kichi" if S>=1e6 else
            "kichi"     if S>=1e5 else
            "syo-kichi" if S>0 else
            "kyo"
        )
    else:
        print "kyo"