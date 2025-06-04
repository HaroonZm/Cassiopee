n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if A[j] < A[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))