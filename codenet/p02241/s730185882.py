n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
weight=[]
for x in range(n):
    for y in range(x,n):
        if matrix[x][y]>=0: weight.append((x,y,matrix[x][y]))
weight.sort(key=lambda x:x[2])
ans=0
p=[i for i in range(n)]

def root(x):
    path_to_root=[]
    while p[x]!=x:
        path_to_root.append(x)
        x=p[x]
    for node in path_to_root:
        p[node]=x
    return x
    
def is_same_set(x,y):
    return root(x)==root(y)
    
def unite(x,y):
    p[root(x)]=root(y)
        
for x,y,w in weight:
    if not is_same_set(x,y):
        unite(x,y)
        ans+=w
print(ans)