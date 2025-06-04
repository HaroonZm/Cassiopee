from functools import reduce
from itertools import product, accumulate, starmap
from operator import add, itemgetter

inf = float('inf')
n, m = map(int, input().split())
mat = list(map(list, map(str, [input() for _ in range(n)])))

colors = 'WBR'
count_map = list(map(lambda row: tuple(map(row.count, colors)), mat))

sums = tuple(tuple(accumulate(map(itemgetter(col), count_map))) for col in range(3))

def count_switch(i, j):
    w1, b1, r1 = sums[1][i], sums[2][i], 0 if i < 0 else 0
    w2 = sums[0][j] - (sums[0][i] if i >= 0 else 0)
    r2 = sums[2][j] - (sums[2][i] if i >= 0 else 0)
    b3 = sums[1][n-1] - sums[1][j]
    w3 = sums[0][n-1] - sums[0][j]
    return (b1 + r1) + (w2 + r2) + (b3 + w3)

possible = (
    (
        sums[1][i] + sums[2][i]
        + sums[0][j] - (sums[0][i] if i>=0 else 0)
        + sums[2][j] - (sums[2][i] if i>=0 else 0)
        + sums[1][n-1] - sums[1][j]
        + sums[0][n-1] - sums[0][j]
    )
    for i, j in product(range(n-2), range(1, n-1)) if i < j
)
print(min(possible))