import functools
import operator
import collections
import itertools

def φ(α,β):
    return list(map(chr,range(α,β)))
Φ = functools.reduce(operator.add, [φ(97,123),φ(65,91)])[::-1]*2
while functools.reduce(operator.or_,[int(input())]):
    λ = itertools.cycle(map(lambda x: int(x), input().split()))
    σ = input()
    ψ = (c for c in σ)
    ζ = (Φ[functools.reduce(operator.add, [Φ.index(ι), κ])] for ι,κ in zip(ψ,λ))
    print("".join(collections.deque(ζ, maxlen=0) or ζ))