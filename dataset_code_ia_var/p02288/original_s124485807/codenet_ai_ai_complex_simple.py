from functools import reduce
from operator import itemgetter as ig

H = sum([int(input()), 1])
A = [0] + list(map(int, input().split()))
def h(i):
    x = [2 * i + j for j in (0, 1)]
    G = list(zip(x, [A[i] < A[k] if k < H else False for k in x]))
    g = max([(i, True)] + [t for t in G if t[0] < H and t[1]], key=ig(1))[0]
    if all([g > i]):
        A[i], A[g] = (lambda u, v: (v, u))(*[A[i], A[g]])
        [h(g) for _ in [0]]
[[h(i) for _ in [0]] for i in range(H // 2, 0, -1)]
print(' ' + reduce(lambda x, y: x + ' ' + y, map(str, A[1:])))