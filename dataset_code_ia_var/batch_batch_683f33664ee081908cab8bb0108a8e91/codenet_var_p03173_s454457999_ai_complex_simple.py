from functools import reduce, lru_cache
from operator import add
from itertools import accumulate, product, starmap, tee

N,*A=map(int,open(0).read().split())

DP= [[0 if i==j else None for j in range(N)] for i in range(N)]

SUM = [0]+list(accumulate(A))

for diag in range(1,N):
    for start in range(N-diag):
        i, j = start, start+diag
        slices = (reduce(add, (DP[i][k], DP[k+1][j], SUM[j+1]-SUM[i]), 0) for k in range(i,j))
        DP[i][j]=min(slices)

print(next(starmap(lambda x, y: DP[x][y], [(0,N-1)])))