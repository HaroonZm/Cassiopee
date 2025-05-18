from math import sqrt
while 1:
    n = input()
    if n == 0:
        break
    C = [map(int, raw_input().split()) for i in xrange(n)]
    P = [[C[0][:2]]]
    # calculate intersections of the circles
    for i in xrange(n-1):
        x0, y0, r0 = C[i]
        x1, y1, r1 = C[i+1]
        rr = (x1 - x0)**2 + (y1 - y0)**2; rd = sqrt(rr)
        rc = (r0**2 + rr - r1**2) / (2 * rd); rs = sqrt(4*r0**2*rr - (r0**2 + rr - r1**2)**2) / (2 * rd)
        ex = (x1 - x0) / rd; ey = (y1 - y0) / rd
        bx = x0 + ex * rc; by = y0 + ey * rc
        P.append([(bx + ey * rs, by - ex * rs), (bx - ey * rs, by + ex * rs)])
    P.append([C[-1][:2]])

    def calc((x0, y0), (x1, y1)):
        return sqrt((x1 - x0)**2 + (y1 - y0)**2)
    def cross((x0, y0), (x1, y1), (x2, y2)):
        return (x1-x0) * (y2-y0) - (x2-x0) * (y1-y0)
    INF = 10**18
    dist = {(0, 0): 0}
    for i in xrange(n):
        for j, (x, y) in enumerate(P[i]):
            left = p_left = None; right = p_right = None
            d = dist[i, j]
            for k in xrange(i+1, n):
                lp, rp = P[k]
                # update left and right
                if left is None or cross((x, y), left, lp) >= 0:
                    left = lp
                if right is None or cross((x, y), rp, right) >= 0:
                    right = rp
                # check if left <= right
                if cross((x, y), left, right) < 0:
                    break

                # propagate cost from P[i][j] to P[k][0] or P[k][1] if possible
                if p_left != left:
                    dist[k, 0] = min(dist.get((k, 0), INF), d + calc((x, y), left))
                    p_left = left
                if p_right != right:
                    dist[k, 1] = min(dist.get((k, 1), INF), d + calc((x, y), right))
                    p_right = right
            else:
                # P[i][j] -> goal

                gp = P[-1][0]
                # check if left <= goal <= right
                if (left is None and right is None) or (cross((x, y), left, gp) >= 0 and cross((x, y), gp, right) >= 0):
                    dist[len(P)-1, 0] = min(dist.get((len(P)-1, 0), INF), d + calc((x, y), gp))
    print "%.06f" % dist[len(P)-1, 0]