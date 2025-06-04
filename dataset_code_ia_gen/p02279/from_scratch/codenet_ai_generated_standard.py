import sys
sys.setrecursionlimit(10**7)
n=int(sys.stdin.readline())
children=[[] for _ in range(n)]
parent=[-1]*n
for _ in range(n):
    data=list(map(int,sys.stdin.readline().split()))
    u,k=data[0],data[1]
    if k>0:
        children[u]=data[2:]
        for c in children[u]:
            parent[c]=u
root=parent.index(-1)
depth=[-1]*n
def dfs(u,d):
    depth[u]=d
    for c in children[u]:
        dfs(c,d+1)
dfs(root,0)
for u in range(n):
    if parent[u]==-1:
        t='root'
    elif len(children[u])==0:
        t='leaf'
    else:
        t='internal node'
    print(f'node {u}: parent = {parent[u]}, depth = {depth[u]}, {t}, [{", ".join(map(str,children[u]))}]')