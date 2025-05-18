N = int(input())
lis = []
lis_append = lis.append
for i in range(N):
    a,b = map(int,input().split(" "))
    lis_append((b,a))
lis.sort()
#dp[n][k]　n問解いたときにk問FACのときの最小の秒数
dp = [2**60]*(N+1)
dp[0] = 0
for b,a in lis:
    tmp = list(dp)
    for i in range(1,N+1):
        if dp[i-1]+a <= b:
            tmp[i] = min(dp[i],dp[i-1]+a)
    dp = tmp
ans = 0
for i in range(N+1):
    if dp[i] < 2**60:
        ans = i
print(ans)