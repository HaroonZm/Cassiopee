n = int(input())

dp = [-1] * (n+1)

# def fibonacci(n):
#     if n==0 or n==1:
#         dp[n] = 1
#         return dp[n]
#     else:
#         if dp[n]!=-1:
#             return dp[n]
#         else:
#             dp[n] = fibonacci(n-1) + fibonacci(n-2)
#             return dp[n]

# ans = fibonacci(n)
# print(ans)

dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])