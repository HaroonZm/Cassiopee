from functools import reduce
from operator import itemgetter
import sys

_λ = lambda f: (lambda *a, **kw: f(f, *a, **kw))
Ω = float('inf')

def ϟ():
    n = int(sys.stdin.readline())
    Α = [list(zip(*(iter(map(int, sys.stdin.readline().split())))*2))[1:] for _ in range(n)]
    δ = [0]+[Ω]*n
    Η = [(0,0)]
    φ = lambda Δ, u, v, c: min(Δ[v], Δ[u]+c) if Δ[v]>Δ[u]+c else Δ[v]
    _λ(
        lambda self, H=Η, d=δ:
            [] if not H else (
                lambda u=__import__('heapq').heappop(H)[1]:
                    [H.extend(
                        [(
                            d[u]+cost, v
                        ) for v, cost in Α[u] if d[v]>d[u]+cost]
                    ), 
                    d.__setitem__(
                        v, d[u]+cost) if d[v]>d[u]+cost else None 
                    for v,cost in Α[u]
                    ],
                    self(self, H, d)
            )[1]
    )(_λ)
    print('\n'.join(map(lambda i: f'{i} {δ[i]}', range(n))))
ϟ()