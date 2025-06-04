from functools import lru_cache
from itertools import count, takewhile

N = 300
squares = [i * i for i in range(1, int(N**0.5) + 1)]
dp = [1] + [0] * N
for sq in squares:
    for j in range(sq, N + 1):
        dp[j] += dp[j - sq]

for n in iter(int, 1):
    n = int(input())
    if not n:
        break
    print(dp[n])