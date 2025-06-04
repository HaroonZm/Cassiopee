from functools import reduce
from itertools import product, accumulate

magic = lambda s,c: sum(map(lambda x: x!=c, s))

N, M = map(int, __import__('sys').stdin.readline().split())
A, S, riddle = [], [], lambda i,j:(lambda z:magic(z,j))
total = sum(map(riddle, [(lambda:__import__('sys').stdin.readline().strip())() for _ in range(1)], 'W'))
mid, last = [(lambda:__import__('sys').stdin.readline().strip())() for _ in range(N-2)], (lambda:__import__('sys').stdin.readline().strip())()
total += magic(last,'R')
A = mid

splits = [(a,b,N-2-a-b) for a,b in product(range(N-1),range(1,N-a)) if N-2-a-b>=0]
supermin = min(
    reduce(lambda acc, q: acc + q,
      map(
        lambda ijc: magic(A[ijc[0]], ijc[1]),
        filter(
          lambda x: 0<=x[0]<N-2,
          zip(range(N-2), reduce(lambda l, e:l+e, (
            [(['W']*w + ['B']*b + ['R']*r)[:N-2]]
            for w,b,r in [bset]
          )))
        )
      ), 0)
    for bset in splits
)

print(total+supermin)