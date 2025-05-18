t=int(input())
arr=[]
for x in range(t):
    a=list(map(int,input().split()))
    arr.append(a)
dp=[[0 for x in range(3)]for y in range(t)]
dp[0][0]=arr[0][0]
dp[0][1]=arr[0][1]
dp[0][2]=arr[0][2]
for x in range(1,t):
    dp[x][0]=arr[x][0]+max(dp[x-1][1],dp[x-1][2])
    dp[x][1]=arr[x][1]+max(dp[x-1][0],dp[x-1][2])
    dp[x][2]=arr[x][2]+max(dp[x-1][0],dp[x-1][1])

print(max(dp[t-1]))