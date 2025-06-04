from functools import reduce
from operator import mul

N, K = map(int, input().split())
S = [0] * N
for _ in range(K):
    a, b = map(int, input().split())
    S[a - 1] = b

dp = [0] * 9
st, nd = S[:2]

if st:
    if nd:
        dp[(st - 1) * 3 + (nd - 1)] = 1
    else:
        dp[(st - 1) * 3 : st * 3] = [1] * 3
elif nd:
    for i in range(3):
        dp[i * 3 + (nd - 1)] = 1
else:
    dp = [1] * 9

for val in S[2:]:
    next_dp = [0] * 9
    if val:
        idx = val - 1
        for pre in range(3):
            total = sum(dp[pre * 3 + j] for j in range(3))
            next_dp[pre * 3 + idx] = total - dp[idx * 4] if pre == idx else total
    else:
        for cur in range(3):
            for pre in range(3):
                total = sum(dp[pre * 3 + j] for j in range(3))
                next_dp[pre * 3 + cur] = total - dp[cur * 4] if pre == cur else total
    dp = next_dp

print(sum(dp) % 10000)