# Your code here!

n=int(input())
c = [int(input()) for i in range(n)]

r = [-1]*n
d=dict()
for i, cc in enumerate(c):
    if cc in d:
        r[i] = d[cc]
        d[cc] = i
    else:
        d[cc] = i

#print(c)
#print(r)
dp=[1]*n
dp[0]=1
for i in range(1,n):
    if r[i] == -1:
        dp[i] = dp[i-1]
    elif r[i] == i-1:
        dp[i] = dp[i-1]
    else:
        dp[i] = (dp[i-1] + dp[r[i]])%(10**9+7)

#print(dp)
print(dp[n-1])