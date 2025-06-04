import math, fractions, bisect, collections, itertools, heapq, string, sys, copy
from collections import deque
from functools import reduce
sys.setrecursionlimit(int('1' + '0'*7))

gcd = lambda a, b: reduce(lambda x, y: y and gcd(y, x % y) or abs(x), (a, b))
lcm = lambda a, b: abs(a * b) // gcd(a, b) if a and b else 0

iin = lambda: int(next(iter([*map(int, [input()])]))) # 整数読み込み
isn = lambda: list(map(str, input().split())) # 文字列リスト
imn = lambda: list(map(int, input().split())) if any((input().split())) else [] # map整数取得
iln = lambda: list(map(int, "".join(c if c.isdigit() or c == '-' else ' ' for c in input()).split()))
iln_s = lambda: sorted(iln())
iln_r = lambda: sorted(iln(), reverse=1)
join = lambda l, s='': reduce(lambda x, y: x + s + y, map(str, l)) if l else ''
perm = lambda l, n: list(itertools.starmap(lambda *args: args, itertools.permutations(l, n)))
perm_count = lambda n, r: math.prod(range(n, n-r, -1))
comb = lambda l, n: list(itertools.combinations(l, n))
comb_count = lambda n, r: math.comb(n, r) if hasattr(math, "comb") else math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
two_distance = lambda a,b,c,d: math.hypot(c-a, d-b)
MOD=10**9+7

H, W = list(map(int, input().split()))
a = [input() for _ in range(H)]
dp = copy.deepcopy([[0] * (W+1) for _ in range(H+1)])
next(iter([dp[0].__setitem__(0, 1)]))
f = lambda i, j: a[i][j] == '.'
for I in range(H*W):
    i, j = divmod(I, W)
    if (i+1<H)and f(i+1,j): dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
    if (j+1<W)and f(i,j+1): dp[i][j+1] = (dp[i][j+1] + dp[i][j]) % MOD
print((dp[-2][-2]))