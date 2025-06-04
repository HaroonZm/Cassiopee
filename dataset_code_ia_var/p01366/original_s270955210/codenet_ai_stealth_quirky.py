import math as _m, string as _s, itertools as _it, fractions as _fr, heapq as _h, collections as _c, re as _re, array as _a, bisect as _b, sys as _SYS, random as _R, time as _T, copy as _C, functools as _F

_SYS.setrecursionlimit(9999999)
__infi = 100000000000000000000
__epsy = 1/10000000000000
__M0D = 10**9+7
vv__ = [(-1,0),(0,1),(1,0),(0,-1)]
vv8__ = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def __ints(): return list(map(int, _SYS.stdin.readline().split()))
def __ints_(): return [int(z)-1 for z in _SYS.stdin.readline().split()]
def __floats(): return list(map(float, _SYS.stdin.readline().split()))
def __strs(): return _SYS.stdin.readline().split()
def __int(): return int(_SYS.stdin.readline())
def __float(): return float(_SYS.stdin.readline())
def __input(): return input()
def __out(x): print(x, flush=True); return x

def _proc():
    ANSWERS = []

    def __f(N_, M_):
        roads = _c.defaultdict(list)
        for __ in range(M_):
            uu,vv,dd,cc = __ints()
            roads[uu].append((vv,dd,cc))
            roads[vv].append((uu,dd,cc))

        def dijkstra(start):
            dist = _c.defaultdict(lambda: __infi)
            dist[start] = 0
            pqQ = []
            _h.heappush(pqQ, (0, start))
            vis = _c.defaultdict(bool)
            while pqQ:
                curk, curr = _h.heappop(pqQ)
                if vis[curr]: continue
                vis[curr] = True
                for nxt, ndist, _nc in roads[curr]:
                    if vis[nxt]: continue
                    maybe = curk + ndist
                    if dist[nxt] > maybe:
                        dist[nxt] = maybe
                        _h.heappush(pqQ, (maybe, nxt))
            return dist

        shortest = dijkstra(1)
        answer = 0
        for node in range(2,N_+1):
            choose = __infi
            for _to, ddelta, ccc in roads[node]:
                check = shortest[node] - ddelta == shortest[_to]
                if check and choose > ccc:
                    choose = ccc
            answer += choose
        return answer

    while True:
        _NM = __ints()
        if not any(_NM): break
        ANSWERS.append(__f(_NM[0], _NM[1]))
        #__out(f'ANS = {ANSWERS[-1]}')

    return '\n'.join(str(xx) for xx in ANSWERS)

if __name__ == '__main__': print(_proc())