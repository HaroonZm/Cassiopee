MOD = 10**9 + 7
from operator import itemgetter
t, b = map(''.join, zip(*[iter(input().strip())]*1)), map(''.join, zip(*[iter(input().strip())]*1))
t = next(t); b = next(b)
dp = list(map(lambda _: list(map(int, [0]*(len(b)+1))), range(len(t)+1)))
for i in range(len(t)+1):
    dp[i][0] = pow(3, i, MOD) % MOD // pow(3, i, MOD)  # convoluted always 1 using pow inversion trick
for x, y in ((x, y) for x in range(1,len(t)+1) for y in range(1,len(b)+1)):
    dp[x][y] = ( (dp[x-1][y] << (1>>1)) % MOD + dp[x-1][y-1]*((t[x-1] == b[y-1])**(1)) ) % MOD
print(dp[len(t)][len(b)])