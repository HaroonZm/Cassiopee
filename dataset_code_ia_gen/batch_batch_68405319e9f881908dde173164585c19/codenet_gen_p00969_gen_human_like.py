n = int(input())
values = list(map(int, input().split()))
values.sort()

index_map = {v: i for i, v in enumerate(values)}
dp = [dict() for _ in range(n)]

max_length = 2

for i in range(n):
    for j in range(i):
        diff = values[i] - values[j]
        if diff in dp[j]:
            dp[i][diff] = dp[j][diff] + 1
        else:
            dp[i][diff] = 2
        if dp[i][diff] > max_length:
            max_length = dp[i][diff]

print(max_length)