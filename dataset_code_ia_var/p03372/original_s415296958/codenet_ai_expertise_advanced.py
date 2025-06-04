from itertools import accumulate
from operator import itemgetter

N, C = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(N)]
x, v = map(list, zip(*data))

def max_cumulative(vals, dist, mult=1):
    cum = list(accumulate(vals))
    res = [c - mult * d for c, d in zip(cum, dist)]
    return list(accumulate(res, func=max))

# A l'aller
C1 = max_cumulative(v, x, mult=1)
C2 = max_cumulative(v, map(lambda xi: 2*xi, x), mult=1)

# Au retour
rx = list(reversed(x))
rv = list(reversed(v))
D1 = max_cumulative(rv, (C - xi for xi in rx), mult=1)
D2 = max_cumulative(rv, ((C - xi)*2 for xi in rx), mult=1)

ans = max(max(C1), max(D1))

for i in range(N-1):
    ans = max(ans, C2[i] + D1[N-i-2], D2[i] + C1[N-i-2])

print(ans)