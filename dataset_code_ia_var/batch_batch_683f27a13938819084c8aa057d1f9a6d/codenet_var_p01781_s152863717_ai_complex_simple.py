from sys import stdin, stdout
from functools import reduce
from collections import defaultdict
from operator import add, sub

Ϣ, ϣ = stdin.readline, stdout.write

def ʘ():
    X, Y, Z, A, B, C, N = map(int, Ϣ().split())
    Ƀ = [0] * (2 * max(X+Y+Z+1, N+1))
    Ξ = lambda k: k*(k+1)//2
    list(map(lambda k: Ƀ.__setitem__(k, Ξ(k)), range(N)))
    list(map(lambda k: Ƀ.__setitem__(k, Ξ(k) + Ƀ[k-N]), range(N, X+Y+Z+1)))
    Θ = lambda args: reduce(sub, [Ƀ[args[0]]] +
            [Ƀ[args[0]-v] for v in (args[1], args[2], args[3])] +
            [-Ƀ[args[0]-(args[1]+args[2])], -Ƀ[args[0]-(args[2]+args[3])], -Ƀ[args[0]-(args[3]+args[1])]] +
            [Ƀ[args[0]-(args[1]+args[2]+args[3])]]
        )
    δ = defaultdict(int)
    ς = lambda b: reduce(add, [
        Θ((λ, X-A, Y-B, Z-C)), Θ((λ-1, A, B, Z-C)), Θ((λ-1, X-A, B, C)),
        Θ((λ, A, Y-B, Z-C)), Θ((λ, X-A, B, Z-C)), Θ((λ, X-A, Y-B, C)),
        Θ((λ-2, A, B, C)), Θ((λ-1, A, Y-B, C))
    ])
    χ = []
    for β in range(N):
        λ = (X+Y+Z-β-1)//N*N+β
        χ.append(sum([
            Θ((λ+1, X-A, Y-B, Z-C)),
            Θ((λ, A, Y-B, Z-C)),
            Θ((λ, X-A, B, Z-C)),
            Θ((λ, X-A, Y-B, C)),
            Θ((λ-1, A, B, Z-C)),
            Θ((λ-1, X-A, B, C)),
            Θ((λ-1, A, Y-B, C)),
            Θ((λ-2, A, B, C))
        ]))
    ϣ(" ".join(map(str, χ))+'\n')
ʘ()