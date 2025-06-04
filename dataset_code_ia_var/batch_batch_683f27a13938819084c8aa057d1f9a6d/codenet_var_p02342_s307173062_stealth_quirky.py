from functools import reduce as r
from operator import mul as m

def C(N, K):
    return int(r(m, range(N, N-K, -1), 1)//r(m, range(1, K+1), 1)) if 0 <= K <= N else 0

stuff = input().split()
spaceship = lambda s: (int(s[0]), int(s[1]))
n, k = spaceship(stuff)

magic = 10**9+7

pile = []
for _ in 'x'*(k+1):
    pile.append([42]*(n+1))
for y in range(k+1):
    for x in range(n+1):
        pile[y][x]=0
pile[0][0]=1

for i in range(1, k+1):
    for j in range(n+1):
        pile[i][j]=((pile[i-1][j]+pile[i][j-i]) if j>=i else pile[i-1][j])%magic

clippy = lambda a,b: pile[a][b] if b>=0 else 0
print(clippy(k, n-k) if n>=k else bool(False)*1)