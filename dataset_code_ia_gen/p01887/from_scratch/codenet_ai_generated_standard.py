import sys
import heapq

input=sys.stdin.readline

W,H,K=map(int,input().split())
N=int(input())
dogs=set()
for _ in range(N):
    x,y=map(int,input().split())
    dogs.add((x,y))

w=(W+1)//2
h=(H+1)//2

if K>h:
    print(-1)
    sys.exit()

dist=[float('inf')]*(w*h)
used_special=[float('inf')]*(w*h)

def idx(x,y):
    return (y-1)*w+(x-1)

adj=[[] for _ in range(w*h)]

# directions for edges: from house (x,y) to (x-1,y+1),(x,y+1),(x+1,y+1) in house coord
dx=[-1,0,1]
dy=[1,1,1]

for y in range(1,h+1):
    for x in range(1,w+1):
        u=idx(x,y)
        # special pipe to this house from "water source"
        # cost 0, used_special=1
        adj[-1 if y==1 else None]=[] # no water source node; we handle special pipes directly in dijkstra
        # edges to next row
        if y<h:
            for d in range(3):
                nx=x+dx[d]
                ny=y+dy[d]
                if 1<=nx<=w and 1<=ny<=h:
                    v=idx(nx,ny)
                    cx=( (x+nx)*2 -1 )//2
                    cy=( (y+ny)*2 -1 )//2
                    block_x=cx*2-1
                    block_y=cy*2-1
                    # block between houses (u,v) is at ((x1+x2),(y1+y2))/2 in block coords
                    bx= x*2-1 + (nx - x)
                    by= y*2-1 + (ny - y)
                    cost=2 if (bx,by) in dogs else 1
                    # now add edge from u to v with cost, no special pipe
                    # also, special pipe to v costs 0 and uses one special pipe
                    adj[u].append((v,cost,0)) # common pipe
# Dijkstra with state: (cost, used_special, node)
# start nodes: all houses in y=1 (first row)
hq=[]
for x in range(1,w+1):
    i=idx(x,1)
    dist[i]=0
    used_special[i]=1
    heapq.heappush(hq,(0,1,i))

while hq:
    c,s,u=heapq.heappop(hq)
    if dist[u]<c or used_special[u]<s:
        continue
    for v,w_cost,special_cost in adj[u]:
        ns=s+special_cost
        nc=c+w_cost
        if ns<=K:
            if dist[v]>nc or (dist[v]==nc and used_special[v]>ns):
                dist[v]=nc
                used_special[v]=ns
                heapq.heappush(hq,(nc,ns,v))

if any(dist[idx(x,h)]==float('inf') for x in range(1,w+1)):
    # cannot reach all houses in last row
    print(-1)
    sys.exit()

# ensure all houses reachable
# We need all houses connected in a single network each connected to source with special pipe
# Our dijkstra approach builds the shortest paths from top row houses connected by special pipes
# but we must connect all houses. Is it enough to check dist for all houses?
# Actually, only path from top row to bottom row houses. But we must ensure all houses connected.

# Check connectivity by BFS/DSU or verify all dist known
if any(dist[i]==float('inf') for i in range(w*h)):
    print(-1)
    sys.exit()

print(min(dist[idx(x,h)] for x in range(1,w+1)))