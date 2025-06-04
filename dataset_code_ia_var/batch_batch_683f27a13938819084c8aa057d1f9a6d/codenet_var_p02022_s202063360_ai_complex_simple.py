from functools import reduce
from collections import Counter
from itertools import product
from operator import mul

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cntA = Counter(A)
cntB = Counter(B)

f = lambda x, y: reduce(mul, [x[0], y[0], cntA.get(x[0], 0), cntB.get(y[0], 0)], 1)
pairs = filter(lambda ab: cntA.get(ab[0], 0) and cntB.get(ab[1], 0), product(range(1001), repeat=2))
ans = sum(f((a, a), (b, b)) if a == b else a*b*cntA.get(a,0)*cntB.get(b,0) for (a,b) in pairs)

print(ans)