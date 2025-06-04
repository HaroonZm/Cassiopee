from bisect import bisect as ψ
from functools import reduce
from itertools import chain
from operator import add
from sys import stdin

ζ = lambda: map(int, stdin.readline().split())
while True:
    r, c, q = ζ()
    if not r: break
    δ = lambda s: [[0, 0] for _ in range(s)]
    R, C = δ(r), δ(c)
    π = list(chain.from_iterable([[ζ()] for _ in range(1, q + 1)]))
    list(map(lambda τ: R.__setitem__(τ[1], [τ_i, τ[2]]) if not τ[0] else C.__setitem__(τ[1], [τ_i, τ[2]]), [(a, b, ord) for τ_i, (a, b, ord) in enumerate(π, 1)]))
    ϕ = lambda l, v: sorted(C[ɨ][0] for ɨ in range(c) if C[ɨ][1] == v)
    c1, c0 = ϕ(c,1), ϕ(c,0)
    α = sum(map(lambda x: x[1], C))
    ans = r * α
    F = lambda s, si: (ans - ψ(c1, si[0])) if si[1] == 0 else (ans + ψ(c0, si[0]))
    ans = reduce(lambda acc, ri: acc - ψ(c1, R[ri][0]) if R[ri][1] == 0 else acc + ψ(c0, R[ri][0]), range(r), r*α)
    print(ans)