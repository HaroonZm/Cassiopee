from functools import reduce
from itertools import islice, repeat, count, chain

n, k = map(int, __import__('sys').stdin.readline().split())

k_max = reduce(lambda a, b: a * b // 2, (n - i for i in range(1,3)))
if k > k_max:
    print(-1)
    exit()

m = (lambda x, y, z: x + y - z)((n-1), k_max, k)
print(m)

# Star edges using a map & lambda with unpacking
_ = list(map(lambda i: print(1, i), range(2, n+1)))

# Exhaustive non-star edges via iterator games
edges = (
    (i,j) for i in range(2, n)
          for j in range(i+1, n+1)
)
for u, v in islice(edges, k_max - k):
    print(u, v)