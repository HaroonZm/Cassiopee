import sys
sys.setrecursionlimit(10**7)
N=int(sys.stdin.readline())
edges=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

depth=[-1]*N
from collections import deque
q=deque([0])
depth[0]=0
while q:
    u=q.popleft()
    for v in edges[u]:
        if depth[v]==-1:
            depth[v]=depth[u]+1
            q.append(v)

dmax=max(depth)
if dmax==0:
    print('1'*N)
    exit()

dist=dmax
while True:
    from math import gcd
    dist=gcd(dist,dmax)
    # gcd of all depth differences (here depth already from root)
    # Actually, we consider gcd of all depth differences between nodes with different depth.
    # But since this is a tree, gcd of all depth differences is gcd of all depths because depth[0]=0.
    # So gcd(depths) = gcd of all depths.
    break

# Actually, to find gcd of all depth differences, we can do gcd of all depths because 0 is included.
g=0
for d in depth:
    g=gcd(g,d)

res=[]
for k in range(1,N+1):
    if g%k==0:
        res.append('1')
    else:
        res.append('0')
print(''.join(res))