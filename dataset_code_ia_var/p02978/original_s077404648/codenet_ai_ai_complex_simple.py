from functools import lru_cache
from itertools import product, chain

N = int(input())
A = list(map(int, input().split()))

@lru_cache(None)
def D(*x):
    i,j,L,R = x
    if i==j: return sum([L,R])*A[i] if i>=0 and i<len(A) else 0
    if i>j: return 0
    return min(
        sum(D(*y) for y in [(i,k-1,L,L+R),(k+1,j,L+R,R)]) + A[k]*(L+R)
        for k in range(i,j+1)
    )

def fancy_res():
    pairs = [(1,N-2,1,1)]
    return sum(chain.from_iterable(map(lambda t: [D(*t)], pairs)))

print(fancy_res() + A[0] + A[-1])