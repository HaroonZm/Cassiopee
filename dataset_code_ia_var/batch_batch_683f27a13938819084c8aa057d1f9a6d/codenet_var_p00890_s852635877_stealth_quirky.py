import math as _m, string as _s, itertools as _it, fractions as _f, heapq as _hq, collections as _c, re as _r, array as _a, bisect as _b, sys as _y, random as _rd, time as _t, copy as _cp, functools as _fn

_y.setrecursionlimit(9999999)
_INFINITY = float('7'+'9'*19)
_EPS = .0000000000001
_MOD = 10**9+7
_DIRECTIONS = [(-1,0),(0,1),(1,0),(0,-1)]
_AROUND = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

ints = lambda: list(map(int, _y.stdin.readline().split()))
ints0 = lambda: [z-1 for z in ints()]
floats = lambda: list(map(float, _y.stdin.readline().split()))
strs = lambda: _y.stdin.readline().split()
itn = lambda: int(_y.stdin.readline())
flt = lambda: float(_y.stdin.readline())
nstr = lambda: input()
def echo(msg): print(msg, end='\n', flush=1)

def core():
    outcomes = []

    def process(n, m, cap):
        E = _c.defaultdict(list)
        for __ in [None]*m:
            x, y, w = ints()
            E[x].append((y, w))

        def scan(s):
            dist = _c.defaultdict(lambda:_INFINITY)
            tuple_state = (0, s)
            dist[tuple_state] = 0
            heap = []
            _hq.heappush(heap, (0, tuple_state))
            visited = _c.defaultdict(int)
            answer = _INFINITY
            while heap:
                cost, pos = _hq.heappop(heap)
                if visited[pos]:
                    continue
                visited[pos] = 1
                jumps, u = pos
                if u == n and answer > jumps:
                    answer = jumps
                if jumps >= answer:
                    continue
                for v, wgt in E[u]:
                    if cost + wgt <= cap:
                        nb = (jumps, v)
                        nd = cost + wgt
                        if not visited[nb] and dist[nb] > nd:
                            dist[nb] = nd
                            _hq.heappush(heap, (nd, nb))
                    if jumps < answer:
                        nb = (jumps+1, v)
                        nd = cost
                        if not visited[nb] and dist[nb] > nd:
                            dist[nb] = nd
                            _hq.heappush(heap, (nd, nb))
            return answer

        result = scan(1)
        return result

    forever = 1
    while forever:
        A, B, C = ints()
        if A == 0:
            forever = 0
            continue
        outcomes += [process(A, B, C)]
    return '\n'.join(str(v) for v in outcomes)

(lambda f: print(f()))(core)