import sys
import heapq
import collections
import bisect
import fractions
import time

sys.setrecursionlimit(10000000)
inf = 10**20
eps = 1.0 / 10**10

dd = [(-1,0),(0,1),(1,0),(0,-1)]

def read_list_int():
    return [int(x) for x in sys.stdin.readline().split()]

def read_list_str():
    return sys.stdin.readline().split()

def read_int():
    return int(sys.stdin.readline())

def read_str():
    return input()

def binary_search(f, mi, ma):
    start_time = time.time()
    mi = fractions.Fraction(mi, 1)
    ma = fractions.Fraction(ma, 1)
    while ma > mi + eps:
        now = time.time()
        mid = (ma + mi) / 2
        if now - start_time > 35:
            return mid
        if isinstance(mid, float):
            tk = max(1, int(10**15 / mid))
            mid = fractions.Fraction(int(mid*tk), tk)
        if float(mid) == float(ma) or float(mid) == float(mi):
            return mid
        if f(mid):
            mi = mid
        else:
            ma = mid
    if f(mid):
        return mid + eps
    return mid

def main():
    result = []

    def solve(w, h):
        a = []
        for i in range(h):
            a.append(read_str())

        si = -1
        sj = -1
        for i in range(1, h-1):
            for j in range(1, w-1):
                if a[i][j] == 's':
                    si = i
                    sj = j

        def dijkstra(char_find):
            dist = {}
            visited = {}
            for i in range(h):
                for j in range(w):
                    dist[(i, j)] = inf
                    visited[(i, j)] = False
            q = []
            for i in range(1, h-1):
                for j in range(1, w-1):
                    if a[i][j] == char_find:
                        dist[(i, j)] = 0
                        heapq.heappush(q, (0, (i, j)))
            while q:
                k, u = heapq.heappop(q)
                if visited[u]:
                    continue
                visited[u] = True
                for di, dj in dd:
                    ni = u[0] + di
                    nj = u[1] + dj
                    if a[ni][nj] not in ['.', 's']:
                        continue
                    uv = (ni, nj)
                    if visited[uv]:
                        continue
                    vd = k + 1
                    if dist[uv] > vd:
                        dist[uv] = vd
                        heapq.heappush(q, (vd, uv))
            return dist

        gd = dijkstra('g')
        wd = dijkstra('*')

        cgs = []
        cws = []
        for i in range(1, h-1):
            for j in range(1, w-1):
                if a[i][j] not in ['.', 's']:
                    continue
                if gd[(i, j)] >= inf:
                    cgs.append((i, j))
                else:
                    cws.append((i, j))
        cc = len(cgs) + len(cws)
        cgc = len(cgs)
        cgw = 0
        for pos in cgs:
            cgw += wd[pos]

        sgw = []
        sgw.append((inf, 0, 0))
        for pos in cws:
            gt = gd[pos]
            wt = wd[pos]
            sgw.append((gt-wt, wt, gt))
        sgw.sort()
        ls = len(sgw) - 1

        def check(t):
            s2 = cgw
            tc2 = cgc + ls
            si = bisect.bisect_left(sgw, (t, 0, 0))
            tc2 = cgc + ls - si
            for idx in range(si):
                s2 += sgw[idx][2]
            for idx in range(si, ls):
                s2 += sgw[idx][1]
            av = (s2 + t * tc2) / cc
            return t < av

        k = binary_search(check, 0, 10**10)
        gt = gd[(si, sj)]
        wt = wd[(si, sj)]
        r = gt
        if wt + k < gt:
            r = wt + k
        return '{:0.10f}'.format(float(r))

    while True:
        n, m = read_list_int()
        if n == 0:
            break
        result.append(solve(n, m))
        break

    return '\n'.join(result)

print(main())