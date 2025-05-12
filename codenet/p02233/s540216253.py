dp=[0]*50
dp[0]=1
dp[1]=1
N = int(input())

def makefib(n):
    if n == 0 or n == 1:
        return 1
    elif dp[n] == 0:
        dp[n] = makefib(n-1) + makefib(n-2)
        return dp[n]
    else:
        return dp[n]
print(makefib(N))