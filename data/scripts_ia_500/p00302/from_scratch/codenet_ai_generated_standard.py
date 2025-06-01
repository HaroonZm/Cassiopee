N,R,T=map(int,input().split())
p=[int(input()) for _ in range(N)]
containers=0
for t in range(T+1):
    locs={}
    for pi in p:
        pos=(pi*t)%R
        locs[pos]=locs.get(pos,0)+1
    containers=max(containers,max(locs.values()))
print(containers)