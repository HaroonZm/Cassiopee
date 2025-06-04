import sys
from collections import Counter, defaultdict
from itertools import accumulate, chain, repeat
from functools import reduce

input = sys.stdin.readline

N, M = map(int, input().split())
a = map(int, input().split())

D = defaultdict(lambda: [0, 0])
for k, v in Counter(map(lambda x: x % M, a)).items():
    D[k][0] = v & 1
    D[k][1] = v - (v & 1)
    
get = lambda u, t: D[u][t] if u in D else 0

ans = (get(0, 0) + get(0, 1)) >> 1

complex_range = filter(lambda x: x > 0 and x <= M // 2, range(M))

for i in complex_range:
    U, V = get(i, 0), get(M - i, 0)
    X = get(i, 1)
    Y = get(M - i, 1)
    
    minUV = min(U, V)
    remU, remV = U - minUV, V - minUV
    y = min(remU, Y)
    z = min(remV, X)
    ans += minUV + y + z + ((Y - y) >> 1) + ((X - z) >> 1)

ans += ((get(M//2, 0) + get(M//2, 1)) >> 1) * ((M & 1) ^ 1)

print(ans)