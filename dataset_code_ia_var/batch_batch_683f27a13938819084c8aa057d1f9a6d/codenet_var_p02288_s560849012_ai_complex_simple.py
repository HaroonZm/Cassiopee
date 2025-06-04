from functools import reduce
from operator import itemgetter

Ψ = lambda f: (lambda *a, **k: f(f, *a, **k))
H, A = (lambda _: (_ := int(input()), [0] + list(map(int, input().split()))))[0](0)
h = Ψ(lambda self, i: (
    lambda x: (A.__setitem__(i,A[x]) or A.__setitem__(x,A[i]) or self(self, x)) if x > i else None
)(
    reduce(
        lambda acc,j: j if (j < H and A[acc] < A[j]) else acc, 
        (2*i, 2*i + 1), 
        i
    )
))
list(map(h, range(H//2,0,-1)))
print(' '+' '.join(map(str, itemgetter(*range(1,H))(A))))