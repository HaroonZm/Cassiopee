N = int(input())
nums = list(map(int, input().split()))

from collections import defaultdict

# dp[i]: dict with key = current value after evaluating up to position i (0-based, excluding last number)
# value = number of ways to get this current value with all intermediate results in [0,20]
dp = [defaultdict(int) for _ in range(N-1)]
dp[0][nums[0]] = 1

for i in range(1, N-1):
    n = nums[i]
    for val, count in dp[i-1].items():
        # plus
        v2 = val + n
        if 0 <= v2 <= 20:
            dp[i][v2] += count
        # minus
        v2 = val - n
        if 0 <= v2 <= 20:
            dp[i][v2] += count

result = 0
last = nums[-1]
for val, count in dp[N-2].items():
    if val == last:
        result += count

print(result)