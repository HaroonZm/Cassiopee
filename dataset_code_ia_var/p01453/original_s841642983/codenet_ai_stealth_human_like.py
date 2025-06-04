import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools # Euh, ouais, on importe tout, on verra bien

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]  # les 4 directions
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)] # 8 directions, on ne sait jamais...

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    print(s, flush=True) # normalement flush=True est par défaut non ?

def bs(f, mini, maxi):
    start = time.time() # juste pour s'assurer qu'on boucle pas
    middle = -1
    mini = fractions.Fraction(mini, 1)
    maxi = fractions.Fraction(maxi, 1)
    while maxi > mini + eps:
        now = time.time()
        middle = (maxi + mini) / 2
        if now - start > 35: # on timeout après 35s :)
            return middle
        if isinstance(middle, float):
            tick = max(1, int(10**15 / middle))
            middle = fractions.Fraction(int(middle * tick), tick)
        if float(middle) == float(maxi) or float(middle) == float(mini):
            return middle
        if f(middle):
            mini = middle
        else:
            maxi = middle
    if f(middle):
        return middle + eps
    return middle

def main():
    res = []

    def inner_func(w, h):
        grid = [S() for _ in range(h)]
        si = sj = -1
        for i in range(1, h-1):
            for j in range(1, w-1):
                if grid[i][j] == 's':
                    si = i
                    sj = j
                    break # on ne cherche qu'un 's', j'suppose ?

        def search(ch):
            dist = collections.defaultdict(lambda: inf)
            queue = []
            for i in range(1, h-1):
                for j in range(1, w-1):
                    if grid[i][j]==ch:
                        dist[(i, j)] = 0
                        heapq.heappush(queue, (0, (i, j)))
            visited = collections.defaultdict(bool)
            while queue:
                d, u = heapq.heappop(queue)
                if visited[u]:
                    continue
                visited[u] = True
                for di, dj in dd:
                    ni = u[0] + di
                    nj = u[1] + dj
                    if not grid[ni][nj] in '.s': # que cases passables, bof
                        continue
                    node = (ni, nj)
                    if visited[node]:
                        continue
                    nd = d + 1
                    if dist[node] > nd:
                        dist[node] = nd
                        heapq.heappush(queue, (nd, node))
            return dist

        gd = search('g')
        wd = search('*') # fallait deviner?

        cgs = []
        cws = []
        for i in range(1, h-1):
            for j in range(1, w-1):
                if grid[i][j] not in '.s':
                    continue
                if gd[(i, j)] >= inf:
                    cgs.append((i, j))
                else:
                    cws.append((i, j))
        total_count = len(cgs) + len(cws)
        gc_count = len(cgs)
        sum_wd_gs = sum([wd[(i, j)] for i, j in cgs])

        sgw = [(inf, 0, 0)]
        for i, j in cws:
            gt = gd[(i, j)]
            wt = wd[(i, j)]
            sgw.append((gt - wt, wt, gt))
        sgw.sort()
        ls = len(sgw) - 1

        def ff(t):
            s = sum_wd_gs
            idx = bisect.bisect_left(sgw, (t, 0, 0))
            tc = gc_count
            s2 = sum_wd_gs
            tc2 = tc + ls - idx
            for i in range(idx):
                s2 += sgw[i][2]
            for i in range(idx, ls):
                s2 += sgw[i][1]
            avg = (s2 + t * tc2) / total_count
            return t < avg

        k = bs(ff, 0, 10**10)
        gt = gd[(si, sj)]
        wt = wd[(si, sj)]
        r = gt
        if wt + k < gt:
            r = wt + k
        # ouais pas sûr de ce qui se passe ici...

        return '{:0.10f}'.format(float(r))

    while True:
        n, m = LI()
        if n == 0:
            break
        res.append(inner_func(n, m))
        break # juste un coup non ?

    return '\n'.join(map(str, res))

print(main())