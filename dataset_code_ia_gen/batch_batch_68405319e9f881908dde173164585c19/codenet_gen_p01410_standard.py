n=int(input())
blocks=[tuple(sorted(map(int,input().split()))) for _ in range(n)]
blocks.sort(key=lambda x:(x[0],x[1]))
dp=[0]*n
for i in range(n):
    dp[i]=blocks[i][1]
    for j in range(i):
        if blocks[j][0]<blocks[i][0] and blocks[j][1]<blocks[i][1]:
            dp[i]=max(dp[i],dp[j]+blocks[i][1])
print(max(dp))