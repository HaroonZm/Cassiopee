def find(x):
    if parents[x]==x:
        return x
    return find(parents[x])

def unite(x,y):
    px=find(x)
    py=find(y)
    if deepth[px]>deepth[py]:
        parents[py]=px
        deepth[px]=max(deepth[px],deepth[py]+1)
    else:
        parents[px]=py
        deepth[py]=max(deepth[py],deepth[px]+1)

def same(x,y):
    if find(x)==find(y):
        return True
    else:
        return False

N,M=map(int,input().split())
Graph=[]
for _ in range(M):
    a,b=map(int,input().split())
    Graph.append((a-1,b-1))

cnt=0
for i in range(M):
    flag=True
    parents=[i for i in range(N)]
    deepth=[0 for _ in range(N)]
    for k in range(M):
        if i!=k:
            unite(Graph[k][0],Graph[k][1])
    for l in range(N-1):
        if find(l)!=find(l+1):
            flag=False
    if not flag:
        cnt+=1
print(cnt)