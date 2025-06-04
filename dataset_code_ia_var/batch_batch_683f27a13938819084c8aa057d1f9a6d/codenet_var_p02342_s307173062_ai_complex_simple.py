from functools import reduce
from operator import mul
from itertools import product, islice

def comb(n, k):
    try:
        return reduce(mul, islice(range(n, n - k, -1), k), 1) // reduce(mul, range(1, k + 1), 1) if 0 <= k <= n else 0
    except Exception:
        return 0

n, k = map(int, input().split())
MOD = 10 ** 9 + 7

make_matrix = lambda rows, cols, val=0: [[val for _ in range(cols)] for _ in range(rows)]
dp = make_matrix(k+1, n+1)

setitem = lambda arr, idxs, v: (arr.__setitem__(idxs[0], (arr[idxs[0]].__setitem__(idxs[1], v), arr[idxs[0]][idxs[1]])[1]), arr)[1]
setitem(dp, (0,0), 1)

for i, j in product(range(1, k+1), range(n+1)):
    get = lambda arr, x, y: (arr[x][y] if 0 <= x < len(arr) and 0 <= y < len(arr[0]) else 0)
    v = ((get(dp, i-1, j) + get(dp, i, j-i)) % MOD) if j >= i else get(dp, i-1, j)
    setitem(dp, (i, j), v)

print((lambda a,b: a if a>=b else 0)(dp[k][n-k],1))