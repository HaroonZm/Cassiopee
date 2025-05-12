import sys
readline = sys.stdin.readline
write = sys.stdout.write
def cross3(p0, p1, q0):
    return (p1[0] - p0[0])*(q0[1] - p0[1]) - (p1[1] - p0[1])*(q0[0] - p0[0])
def cross_point(p0, p1, q0, q1):
    x0, y0 = p0; x1, y1 = p1
    x2, y2 = q0; x3, y3 = q1
    dx0 = x1 - x0
    dy0 = y1 - y0
    dx1 = x3 - x2
    dy1 = y3 - y2

    s = (y0-y2)*dx1 - (x0-x2)*dy1
    sm = dx0*dy1 - dy0*dx1
    if sm < 0:
        return -(x0*sm + s*dx0), -(y0*sm + s*dy0), -sm
    return x0*sm + s*dx0, y0*sm + s*dy0, sm
def solve():
    N, M = map(int, readline().split())
    PSS = []
    for i in range(N):
        L = int(readline())
        PS = [list(map(int, readline().split())) for i in range(L)]
        PSS.append(PS)
    QS = [list(map(int, readline().split())) for i in range(M)]
    LS = []
    for PS in PSS:
        for x0, y0 in PS:
            for x1, y1 in QS:
                LS.append(((x0, y0), (x1, y1)))
    def check(p, q, r):
        p0 = (p, q)
        res = 0
        PSS1 = [[(x*r, y*r) for x, y in PS] for PS in PSS]
        for x1, y1 in QS:
            x1 *= r; y1 *= r
            q0 = (x1, y1)
            for PS in PSS1:
                l = len(PS)
                for i in range(l):
                    p1 = PS[i-1]; q1 = PS[i]
                    C0 = cross3(p0, q0, p1)
                    C1 = cross3(p0, q0, q1)
                    D0 = cross3(p1, q1, p0)
                    D1 = cross3(p1, q1, q0)
                    if C0 * C1 < 0 and D0 * D1 < 0:
                        break
                else:
                    continue
                break
            else:
                res += 1
        return res

    ans = 0
    K = len(LS)
    for i in range(K):
        p0, p1 = LS[i]
        for j in range(i):
            q0, q1 = LS[j]
            p, q, r = cross_point(p0, p1, q0, q1)
            if r == 0:
                continue
            ans = max(ans, check(p, q, r))
    write("%d\n" % ans)
solve()