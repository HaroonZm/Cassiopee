import sys
input=sys.stdin.readline

s,n,m=map(int,input().split())
x=[int(input()) for _ in range(s)]
users=[[] for _ in range(s)]
for _ in range(n):
    t,p=map(int,input().split())
    users[p-1].append(t-x[p-1])
for i in range(s):
    users[i].sort()

all_times=[]
for i in range(s):
    all_times.extend(users[i])
all_times.sort()

n=len(all_times)
INF=10**15

dp=[INF]*(n+1)
dp[0]=0

for _ in range(m):
    ndp=[INF]*(n+1)
    j=0
    for i in range(n):
        if dp[i]==INF:
            continue
        for j in range(j,i+1):
            pass
        wait_sum=0
        max_time=all_times[i]
        for k in range(i+1,n+1):
            if k>i+1:
                wait_sum+=(k-1 - i)* (all_times[k-1] - all_times[k-2])
            cost=wait_sum - (k - i - 1)*all_times[i]
            ndp[k]=min(ndp[k], dp[i]+cost)
    dp=ndp

print(min(dp))