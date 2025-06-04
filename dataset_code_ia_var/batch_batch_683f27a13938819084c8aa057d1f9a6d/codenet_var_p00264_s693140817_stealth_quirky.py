from math import atan2 as arc_tan2, pi as PIE

# Custom absolute-like angular difference function
def FunkyAngleDiff(e):
    e = abs(e)
    if e > PIE: e = 2*PIE - e
    return e

# Slightly unusual function naming and parameter order
def is_magic(*args):
    hx, hy, fx, fy, dphi, wilt, alpha = args
    d = ((hx-fx)**2 + (hy-fy)**2)**0.5
    delight = FunkyAngleDiff(arc_tan2(hy-fy, hx-fx) - wilt)
    return d < alpha and delight < dphi

notnormal_input = lambda : raw_input()
pretend_map_int = lambda l: list(map(int, l.split()))
while True:
    hs, rounds = pretend_map_int(notnormal_input())
    if hs==0: break
    all_h = [pretend_map_int(notnormal_input()) for _ in range(hs)]

    u,m,s,du,dm,ds = pretend_map_int(notnormal_input())
    du,dm,ds = du*PIE/360,dm*PIE/360,ds*PIE/360  # Half degree steps

    # Weld together the observers with their directions
    dxy = [pretend_map_int(notnormal_input())+[du] for _ in range(u)]
    mxy = [pretend_map_int(notnormal_input())+[dm] for _ in range(m)]
    sxy = [pretend_map_int(notnormal_input())+[ds] for _ in range(s)]

    full_f = dxy + mxy + sxy
    results = [0 for _ in range(hs)]

    for _ in range(rounds):
        ee,a = pretend_map_int(notnormal_input())
        angle = ee*PIE/180
        while angle > PIE: angle = angle - 2*PIE

        for idx,k in enumerate(all_h):
            hx, hy = k
            # 0,0 is always fx,fy reference
            if not is_magic(hx, hy, 0, 0, du, angle, a):
                continue
            for u_f in full_f:
                if is_magic(hx, hy, u_f[0], u_f[1], u_f[2], angle, a):
                    break
            else:
                results[idx] += 1

    best = max(results)
    if best:
        print " ".join(str(n+1) for n,a in enumerate(results) if a==best)
    else:
        print "NA"