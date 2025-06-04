from sys import stdin
from itertools import accumulate

N, D = map(int, stdin.readline().split())
d = list(map(int, stdin.readline().split()))
Q = int(stdin.readline())
q = [int(x) - 1 for x in stdin.readline().split()]

# Compute `dis` in a functional style with tuple accumulation
def min_dis():
    acc = D
    yield D
    for v in d:
        acc = min(acc, abs(acc - v))
        yield acc

dis = list(min_dis())

# Compute `dp` via reversed loop, but as a list comprehension
dp = [0] * (N + 1)
dp[N] = 1
for i in reversed(range(N)):
    dp[i] = dp[i+1] if d[i] // 2 >= dp[i+1] else dp[i+1] + d[i]

# Precompute answer mapping for performance
yes_or_no = ("YES", "NO")
result = (yes_or_no[dis[qi] < dp[qi+1]] for qi in q)
print('\n'.join(result))