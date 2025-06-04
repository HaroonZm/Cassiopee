n,m=map(int,input().split())
edges=[]
for _ in range(m):
    u,v,f=map(int,input().split())
    edges.append((f,u-1,v-1))
edges.sort(reverse=True)
parent=list(range(n))
rank=[0]*n
def find(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]]
        x=parent[x]
    return x
def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return False
    if rank[a]<rank[b]:
        parent[a]=b
    else:
        parent[b]=a
        if rank[a]==rank[b]:
            rank[a]+=1
    return True
adj=[[] for _ in range(n)]
for f,u,v in edges:
    if union(u,v):
        adj[u].append((v,f))
        adj[v].append((u,f))
# For each node, find minimal friendliness edge in MST (if any)
# satisfaction for node = minimal friendliness with any other node in party (i.e. in MST)
# sum over all nodes
res=0
for lst in adj:
    if lst:
        mn=min(f for _,f in lst)
        res+=mn
print(res)