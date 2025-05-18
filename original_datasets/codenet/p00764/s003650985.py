from math import sqrt
while 1:
    n = input()
    if n == 0:
        break
    C = [map(int, raw_input().split()) for i in xrange(n)]
    P = [[C[0][:2]]]
    for i in xrange(n-1):
        x0, y0, r0 = C[i]
        x1, y1, r1 = C[i+1]
        rr = (x1 - x0)**2 + (y1 - y0)**2; rd = sqrt(rr)
        rc = (r0**2 + rr - r1**2) / (2 * rd); rs = sqrt(4*r0**2*rr - (r0**2 + rr - r1**2)**2) / (2 * rd)
        ex = (x1 - x0) / rd; ey = (y1 - y0) / rd
        bx = x0 + ex * rc; by = y0 + ey * rc
        P.append([(bx + ey * rs, by - ex * rs), (bx - ey * rs, by + ex * rs)])
        #for x, y in P[-1]:
        #    assert (x - x1)**2 + (y - y1)**2 <= r1**2 + 10**-6, "%f, %f" % ((x - x1)**2 + (y - y1)**2, r1**2)
    P.append([C[-1][:2]])
    #print "\n".join(str(e) for e in P)
    #print

    def calc((x0, y0), (x1, y1)):
        return sqrt((x1 - x0)**2 + (y1 - y0)**2)
    def cross((x0, y0), (x1, y1), (x2, y2)):
        return (x1-x0) * (y2-y0) - (x2-x0) * (y1-y0)
    INF = 10**18
    dist = {(0, 0): 0}
    for i in xrange(n):
        #print i
        for j, (x, y) in enumerate(P[i]):
            left = p_left = None; right = p_right = None
            d = dist[i, j]
            for k in xrange(i+1, n):
                lp, rp = P[k]
                # left
                if left is None or cross((x, y), left, lp) >= 0:
                    left = lp
                if right is None or cross((x, y), rp, right) >= 0:
                    right = rp
                if cross((x, y), left, right) < 0:
                    break
                #print k, left, right, cross((x, y), left, right)
                if p_left != left:
                    #G.setdefault((i, j), set()).add((k, 0))
                    dist[k, 0] = min(dist.get((k, 0), INF), d + calc((x, y), left))
                    p_left = left
                if p_right != right:
                    #G.setdefault((i, j), set()).add((k, 1))
                    dist[k, 1] = min(dist.get((k, 1), INF), d + calc((x, y), right))
                    p_right = right
            else:
                # (x, y) -> goal
                gp = P[-1][0]
                if (left is None and right is None) or (cross((x, y), left, gp) >= 0 and cross((x, y), gp, right) >= 0):
                    #G.setdefault((i, j), set()).add((len(P)-1, 0))
                    dist[len(P)-1, 0] = min(dist.get((len(P)-1, 0), INF), d + calc((x, y), gp))
    print "%.06f" % dist[len(P)-1, 0]