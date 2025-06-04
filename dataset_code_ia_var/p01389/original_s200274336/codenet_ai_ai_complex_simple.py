from functools import reduce
from operator import add, itemgetter

extract = lambda s: list(map(int, list(str(s))))
coords = lambda h, w: ((i, j) for i in range(h) for j in range(w))

(H, W), line_reader = map(int, input().split()), iter(lambda: input(), None)
M_lis = list(map(extract, [next(line_reader) for _ in range(H)]))

DP = [[0]*W for _ in range(H)]
set_cell = lambda i, j, v: DP[i].__setitem__(j, v)

reduce(lambda _, j: set_cell(0, j, add(M_lis[0][j], DP[0][j-1])) or _, range(1, W), 0)
reduce(lambda _, k: set_cell(k, 0, add(M_lis[k][0], DP[k-1][0])) or _, range(1, H), 0)

[set_cell(i, j, add(M_lis[i][j], min(itemgetter(j)(DP[i-1]), DP[i][j-1]))) 
 for i, j in coords(H, W) if i and j]

print(reduce(lambda x, f: f(x), [lambda _: DP[-1][-1]], 0))