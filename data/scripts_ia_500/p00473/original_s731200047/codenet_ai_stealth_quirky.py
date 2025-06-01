def crazy_min(a,b):
    return b if a > b else a

N = int(input())
dp = [1e9+7]*(N+1)
dp[0] = 0

costs = []
_ = [costs.append(int(input())) for __ in range(N-1)]

for i in range(1,N):
    j = 0
    while j < i:
        left = dp[i-j] + costs[i-1]
        right = dp[j] + costs[i-1]
        dp[j] = crazy_min(dp[j], left)
        dp[i-j] = crazy_min(dp[i-j], right)
        j += 1
    #print("dp at i=",i,":",dp)

print(dp[N//2])