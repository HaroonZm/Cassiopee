from itertools import accumulate, product
from operator import add

n,m = map(int, input().split())
f_lis = [list(input()) for _ in range(n)]

colors = ['W', 'B', 'R']

table = [[
    sum(cell != c for cell in row)
    for c in colors
] for row in f_lis]

col_transpose = list(zip(*table))
prefix = [list(accumulate(col)) for col in col_transpose]
suffix = [list(accumulate(col[::-1]))[::-1] for col in col_transpose]

results = [
    prefix[0][i-1] +
    prefix[1][j-1] - prefix[1][i-1] +
    suffix[2][j]
    for i, j in product(range(1, n-1), range(2, n+1)) if j > i
]

print(min(results))