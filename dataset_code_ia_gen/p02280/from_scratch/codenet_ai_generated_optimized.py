n=int(input())
nodes=[None]*n
parent=[-1]*n
lefts=[-1]*n
rights=[-1]*n

for _ in range(n):
    id,l,r=map(int,input().split())
    lefts[id]=l
    rights[id]=r
    nodes[id]=(l,r)
    if l!=-1:
        parent[l]=id
    if r!=-1:
        parent[r]=id

root=parent.index(-1)

depth=[-1]*n
def set_depth(u,d):
    depth[u]=d
    if lefts[u]!=-1:
        set_depth(lefts[u],d+1)
    if rights[u]!=-1:
        set_depth(rights[u],d+1)
set_depth(root,0)

height=[-1]*n
def set_height(u):
    h1 = set_height(lefts[u]) if lefts[u]!=-1 else 0
    h2 = set_height(rights[u]) if rights[u]!=-1 else 0
    height[u]=max(h1,h2)
    return height[u]+1
set_height(root)

for u in range(n):
    p=parent[u]
    deg=0
    if lefts[u]!=-1:
        deg+=1
    if rights[u]!=-1:
        deg+=1
    if p==-1:
        s=-1
    else:
        l,r=nodes[p]
        if l==u:
            s=r
        else:
            s=l
    d=depth[u]
    h=height[u]
    if p==-1:
        t="root"
    elif deg==0:
        t="leaf"
    else:
        t="internal node"
    print(f"node {u}: parent = {p}, sibling = {s}, degree = {deg}, depth = {d}, height = {h}, {t}")