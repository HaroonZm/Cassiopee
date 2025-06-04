import heapq
import sys

def _input():
    return sys.stdin.readline()

def _output(s):
    sys.stdout.write(str(s))

def main():
    while True:
        info = list(map(int, _input().split()))
        if all(i == 0 for i in info):
            break
        N, T, R = info
        S = []
        tracks = []
        i = 0
        while i < N:
            S.append(_input().strip())
            prv, x, y = map(int, _input().split())
            arr = []
            while prv != T:
                t, vx, vy = [int(n) for n in _input().split()]
                arr.append((prv, t, x, y, vx, vy))
                x += vx * (t-prv)
                y += vy * (t-prv)
                prv = t
            tracks.append(arr)
            i += 1

        INF = float('inf')
        d = [INF]*N
        q = []
        d[0] = 0
        heapq.heappush(q, (0, 0))

        def search_segment(TA, time):
            for i, seg in enumerate(TA):
                if seg[0] <= time <= seg[1]:
                    return i
            return 0

        while q:
            t, idx = heapq.heappop(q)
            if abs(t - d[idx]) > 1e-6:
                continue
            kA = search_segment(tracks[idx], t)
            while True:
                (tA0, tA1, xA, yA, vxa, vya) = tracks[idx][kA]
                if tA0 <= t <= tA1:
                    break
                kA += 1
            for j in range(N):
                if j == idx or not d[j] > t:
                    continue
                kB = search_segment(tracks[j], t)
                while True:
                    (tB0, tB1, xB, yB, vxb, vyb) = tracks[j][kB]
                    if tB0 <= t <= tB1:
                        break
                    kB += 1
                mA, mB = kA, kB
                while True:
                    segA = tracks[idx][mA]
                    segB = tracks[j][mB]
                    p0, p1, x0, y0, vx0, vy0 = segA
                    q0, q1, x1, y1, vx1, vy1 = segB
                    t0 = max(p0, q0, t)
                    t1 = min(p1, q1)
                    if d[j] <= t0:
                        break
                    dx = vx0-vx1
                    zx = (x0-p0*vx0)-(x1-q0*vx1)
                    dy = vy0-vy1
                    zy = (y0-p0*vy0)-(y1-q0*vy1)
                    a = dx*dx + dy*dy
                    b = 2*(dx*zx + dy*zy)
                    c = zx*zx + zy*zy - R*R
                    if a == 0:
                        if c <= 0:
                            newt = t0
                            if newt < d[j]:
                                d[j] = newt
                                heapq.heappush(q, (newt, j))
                            break
                    else:
                        D = b*b-4*a*c
                        if D >= 0:
                            import math
                            sq = math.sqrt(D)
                            s0 = (-b-sq)/(2*a)
                            s1 = (-b+sq)/(2*a)
                            if t0 <= s1 and s0 <= t1:
                                newt = max(t0, s0)
                                if newt < d[j]:
                                    d[j] = newt
                                    heapq.heappush(q, (newt, j))
                                break
                    if p1 < q1:
                        mA += 1
                    elif p1 > q1:
                        mB += 1
                    elif p1 == T:
                        break
                    else:
                        mA += 1
                        mB += 1
        hits = [S[kkk] for kkk in range(N) if d[kkk] < INF]
        for s in sorted(hits):
            _output(s+'\n')

main()