X = int(input())

dp = [0 for _ in range(X+1)]
dp[0] = 1

for i in range(X):
    if dp[i] == 1:
        for v in range(100, 105 + 1):
            if i+v <= X:
                dp[i+v] = 1
print(dp[X])