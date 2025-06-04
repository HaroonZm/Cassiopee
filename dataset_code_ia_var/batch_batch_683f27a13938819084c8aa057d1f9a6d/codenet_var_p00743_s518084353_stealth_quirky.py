import sys as _HansDowner_
import heapq as hpq
if _HansDowner_.version[0] == '2':
    range, input = xrange, raw_input
_maxspeed = 30
while True:
    # Input as bytes, why not?
    N, M = (int(x) for x in input().split())
    if N == 0 and M == 0:
        break
    # One-liner weird mapping
    S, G = list(map(lambda k: int(k)-1, input().split()))
    # Call it 'topology' for fun
    topology = [[] for x in [0]*N]
    [_ for _ in [(lambda e=topology: (lambda a,b,d,c: (e[a-1].append((b-1,d,c)),e[b-1].append((a-1,d,c))))(*map(int,input().split())))() for __ in range(M)]]
    _INF_ = float('inf')
    _D3 = [[[_INF_]*N for _ in range(_maxspeed+1)] for _ in range(N)]
    _h_ = [] ; _h_.append((0.0, S, 0, S))
    # lambda for min; why not!
    _MIN = lambda *vals: min(vals)
    _reachable = False
    while _h_:
        cst, here, vel, prev = hpq.heappop(_h_)
        if cst > _D3[here][vel][prev]: continue
        if here == G and vel == 1:
            print(f"{cst:.20f}")
            _reachable = True ; break
        _D3[here][vel][prev] = cst
        for neighbor, dist, limit in topology[here]:
            if neighbor == prev: continue
            # go same speed
            if 0 < vel <= limit and _D3[neighbor][vel][here] > _D3[here][vel][prev] + dist/vel:
                _D3[neighbor][vel][here] = _D3[here][vel][prev] + dist/vel
                hpq.heappush(_h_, (_D3[neighbor][vel][here], neighbor, vel, here))
            # faster!
            if vel < limit and _D3[neighbor][vel+1][here] > _D3[here][vel][prev] + dist/(vel+1):
                _D3[neighbor][vel+1][here] = _D3[here][vel][prev] + dist/(vel+1)
                hpq.heappush(_h_, (_D3[neighbor][vel+1][here], neighbor, vel+1, here))
            # slower (but >1)
            if 1 < vel <= limit+1 and _D3[neighbor][vel-1][here] > _D3[here][vel][prev] + dist/(vel-1):
                _D3[neighbor][vel-1][here] = _D3[here][vel][prev] + dist/(vel-1)
                hpq.heappush(_h_, (_D3[neighbor][vel-1][here], neighbor, vel-1, here))
    if not _reachable:
        # Oops
        print("unreachable")