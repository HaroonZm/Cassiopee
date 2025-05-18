import sys
readline = sys.stdin.readline
write = sys.stdout.write

def common_tangent_lines(x1, y1, r1, x2, y2, r2):
    result = []
    xd = x2 - x1; yd = y2 - y1

    rr0 = xd**2 + yd**2
    if (r1 - r2)**2 <= rr0:
        cv = r1 - r2
        if rr0 == (r1 - r2)**2:
            bx = r1*cv*xd/rr0
            by = r1*cv*yd/rr0
            result.append([
                (x1 + bx, y1 + by),
                (x1 - yd + bx, y1 + xd + by),
            ])
        else:
            sv = (rr0 - cv**2)**.5
            px = (cv*xd - sv*yd); py = (sv*xd + cv*yd)
            result.append([
                (x1 + r1*px/rr0, y1 + r1*py/rr0),
                (x2 + r2*px/rr0, y2 + r2*py/rr0),
            ])
            qx = (cv*xd + sv*yd); qy = (-sv*xd + cv*yd)
            result.append([
                (x1 + r1*qx/rr0, y1 + r1*qy/rr0),
                (x2 + r2*qx/rr0, y2 + r2*qy/rr0),
            ])
    if (r1 + r2)**2 <= rr0:
        cv = r1 + r2
        if rr0 == (r1 + r2)**2:
            bx = r1*cv*xd/rr0
            by = r1*cv*yd/rr0
            result.append([
                (x1 + bx, y1 + by),
                (x1 - yd + bx, y1 + xd + by),
            ])
        else:
            sv = (rr0 - cv**2)**.5
            px = (cv*xd - sv*yd); py = (sv*xd + cv*yd)
            result.append([
                (x1 + r1*px/rr0, y1 + r1*py/rr0),
                (x2 - r2*px/rr0, y2 - r2*py/rr0),
            ])
            qx = (cv*xd + sv*yd); qy = (-sv*xd + cv*yd)
            result.append([
                (x1 + r1*qx/rr0, y1 + r1*qy/rr0),
                (x2 - r2*qx/rr0, y2 - r2*qy/rr0),
            ])
    return result

def solve():
    N = int(readline())
    if N == 0:
        return False
    P = [list(map(int, readline().split())) for i in range(N)]
    if N == 1:
        write("1\n")
        return True
    LL = [(r, r+m) for x, y, r, m in P]
    EPS = 1e-9
    ans = 0
    for i in range(N):
        xi, yi, ri, mi = P[i]
        LLi = LL[i]
        for j in range(i):
            xj, yj, rj, mj = P[j]
            LLj = LL[j]
            for pi in LLi:
                for pj in LLj:
                    lines = common_tangent_lines(xi, yi, pi, xj, yj, pj)
                    for p0, p1 in lines:
                        x0, y0 = p0; x1, y1 = p1
                        dx = x1 - x0; dy = y1 - y0
                        q = (dx**2 + dy**2)**.5
                        cnt = 0
                        for xk, yk, rk, mk in P:
                            zx = xk - x0; zy = yk - y0
                            p = abs(dx*zy - dy*zx)
                            if rk*q - EPS <= p <= (rk+mk)*q + EPS:
                                cnt += 1
                        ans = max(ans, cnt)
    write("%d\n" % ans)
    return True
while solve():
    ...