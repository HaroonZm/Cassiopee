N,M,p=map(int,input().split())
ds=[int(input()) for _ in range(M)]
all_stations=[p]+ds
all_stations.sort()
min_cost=10**15
for i in range(len(all_stations)-M):
    s=set(all_stations[i:i+M+1])
    if p in s and all(d in s for d in ds):
        left=all_stations[i]
        right=all_stations[i+M]
        cost1=right-left
        cost2=left+N-right
        min_cost=min(min_cost,2*min(cost1,cost2)+max(cost1,cost2))
print(min_cost*100)