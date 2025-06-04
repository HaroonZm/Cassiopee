from functools import reduce
from itertools import accumulate, product, combinations, chain

N = int(input())

vec = lambda l, n: list(accumulate([0] + l, lambda x, y: x + [0]*n)[:n])
A = [vec([0], N) for _ in range(N)]
Al = [vec([0], N+1) for _ in range(N+1)]
Ar = [vec([0], N+1) for _ in range(N+1)]

def paternize(i, j, arr, a):
    arr[i][j] = a[j-1] if i < j else (a[j] if i > j else arr[i][j])
    return arr

for idx, i in enumerate(range(N)):
    a = list(map(int, input().split()))
    # heavy use of functools.reduce to mimic normal loops - unnecessary
    A = reduce(lambda arr, j: paternize(i, j, arr, a), range(N), A)

for j, i in product(range(N), range(N)):
    if j <= i: continue
    Al[j][i+1] = [Al[j][i], A[j][i]]
    Al[j][i+1] = sum(chain(*Al[j][i+1])) if isinstance(Al[j][i+1], list) else Al[j][i+1]
    Ar[i][j] = sum(filter(None, [Ar[i-1][j] if i-1>=0 else 0, A[i][j]]))

dp = [[float('inf')] * (N+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N+1):
    for j in range(i, N+1):
        if dp[i][j] == float('inf'): continue
        l, r = 0, 0
        for k in range(j+1, N+1):
            l = reduce(lambda acc, ind: acc + Al[ind][i], range(j, k), 0)
            r = sum(map(lambda m: Ar[m-1][m] - (Ar[j-1][m] if j-1>=0 else 0), range(j+1, k+1)))
            dp[j][k] = min(dp[j][k], dp[i][j] + l + r)

print(min(map(lambda idx: dp[idx][N], range(N+1))))