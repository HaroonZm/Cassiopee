n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
in_mst=[False]*n
key=[float('inf')]*n
key[0]=0
res=0
for _ in range(n):
    u=-1
    for i in range(n):
        if not in_mst[i] and (u==-1 or key[i]<key[u]):
            u=i
    in_mst[u]=True
    res+=key[u]
    for v in range(n):
        w=graph[u][v]
        if w!=-1 and not in_mst[v] and w<key[v]:
            key[v]=w
print(res)