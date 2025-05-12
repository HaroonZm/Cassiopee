import sys
readline = sys.stdin.readline
write = sys.stdout.write
def dot3(p0, p1, p2):
    x0, y0 = p0; x1, y1 = p1; x2, y2 = p2
    return (x1 - x0) * (x2 - x0) + (y1 - y0) * (y2 - y0)
def cross3(p0, p1, p2):
    x0, y0 = p0; x1, y1 = p1; x2, y2 = p2
    return (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)
def dist2(p0, p1):
    x0, y0 = p0; x1, y1 = p1
    return (x0 - x1)**2 + (y0 - y1)**2
def solve():
    N = int(readline())
    P = [list(map(int, readline().split())) for i in range(N)]
    ok = 1
    for i in range(N-1):
        p0 = P[i]; p1 = P[i+1]
        d0 = dist2(p0, p1)**.5
        el0 = [-d0, d0]; el1 = [-d0, d0]
        er0 = [-d0, d0]; er1 = [-d0, d0]
        for j in range(i):
            q0 = P[j]
            d1 = dist2(p0, q0)**.5
            d2 = dist2(p1, q0)**.5
            sv = cross3(p0, p1, q0)

            cv0 = dot3(p0, p1, q0) / d1
            cv1 = dot3(p1, p0, q0) / d2
            if sv > 0:
                el0[0] = max(el0[0], cv0)
                el1[0] = max(el1[0], -cv1)
            else:
                er0[1] = min(er0[1], -cv0)
                er1[1] = min(er1[1], cv1)
        for j in range(i+2, N):
            q1 = P[j]
            d1 = dist2(p1, q1)**.5
            d2 = dist2(p0, q1)**.5
            sv = cross3(p1, p0, q1)

            cv0 = dot3(p1, p0, q1) / d1
            cv1 = dot3(p0, p1, q1) / d2
            if sv > 0:
                er1[0] = max(er1[0], cv0)
                er0[0] = max(er0[0], -cv1)
            else:
                el1[1] = min(el1[1], -cv0)
                el0[1] = min(el0[1], cv1)
        if (not max(el0[0], er0[0]) <= min(el0[1], er0[1])
         or not max(el1[0], er0[0]) <= min(el1[1], er1[1])):
            ok = 0
            break
    if ok:
        write("Possible\n")
    else:
        write("Impossible\n")
solve()