from math import sqrt
from sys import stdin, stdout
readline = stdin.readline
write = stdout.write
while 1:
    n = int(readline())
    if n == 0:
        break
    C = [map(int, readline().split()) for i in xrange(n)]
    P = {(0, 0): C[0][:2], (n, 0): C[-1][:2]}
    # calculate intersections of the circles
    for i in xrange(n-1):
        x0, y0, r0 = C[i]
        x1, y1, r1 = C[i+1]
        rr = (x1 - x0)**2 + (y1 - y0)**2; rd = sqrt(rr)
        rc = (r0**2 + rr - r1**2) / (2 * rd); rs = sqrt(4*r0**2*rr - (r0**2 + rr - r1**2)**2) / (2 * rd)
        ex = (x1 - x0) / rd; ey = (y1 - y0) / rd
        bx = x0 + ex * rc; by = y0 + ey * rc
        P[i+1, 0] = (bx + ey * rs, by - ex * rs)
        P[i+1, 1] = (bx - ey * rs, by + ex * rs)

    def calc((x0, y0), (x1, y1)):
        return sqrt((x1 - x0)**2 + (y1 - y0)**2)
    def cross((x0, y0), (x1, y1), (x2, y2)):
        return (x1-x0) * (y2-y0) - (x2-x0) * (y1-y0)
    INF = 10**18
    dist = {(0, 0): 0}
    gp = P[n, 0]
    for i, j in sorted(P):
        pos = P[i, j]
        left = p_left = right = p_right = None
        d = dist[i, j]
        for k in xrange(i+1, n):
            lp = P[k, 0]; rp = P[k, 1]
            # update left and right
            if left is None or cross(pos, left, lp) >= 0:
                left = lp
            if right is None or cross(pos, rp, right) >= 0:
                right = rp
            # check if left <= right
            if cross(pos, left, right) < 0:
                break

            # propagate cost from P[i][j] to P[k][0] or P[k][1] if possible
            if p_left != left:
                dist[k, 0] = min(dist.get((k, 0), INF), d + calc(pos, left))
                p_left = left
            if p_right != right:
                dist[k, 1] = min(dist.get((k, 1), INF), d + calc(pos, right))
                p_right = right
        else:
            # P[i][j] -> goal
            # check if left <= goal <= right
            if (left is None and right is None) or (cross(pos, left, gp) >= 0 and cross(pos, gp, right) >= 0):
                dist[n, 0] = min(dist.get((n, 0), INF), d + calc(pos, gp))
    write("%.06f\n" % dist[n, 0])