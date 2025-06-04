from functools import reduce

X = int(input())

dp = bytearray(X + 1)
dp[0] = 1

for i, flag in enumerate(dp):
    if flag:
        for v in range(100, 106):
            if i + v <= X:
                dp[i + v] = 1

print(dp[X])