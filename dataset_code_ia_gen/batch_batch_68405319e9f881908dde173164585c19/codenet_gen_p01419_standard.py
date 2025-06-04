import sys
import heapq
sys.setrecursionlimit(10**7)
R,C,M=map(int,sys.stdin.readline().split())
office=[list(sys.stdin.readline().rstrip()) for _ in range(R)]
ptime=[list(map(int,sys.stdin.readline().split())) for _ in range(R)]
oncost=[list(map(int,sys.stdin.readline().split())) for _ in range(R)]
offcost=[list(map(int,sys.stdin.readline().split())) for _ in range(R)]
tasks=[tuple(map(int,sys.stdin.readline().split())) for _ in range(M)]
rooms=[(r,c) for r in range(R) for c in range(C) if office[r][c]=='.']
pos_id={ (r,c):i for i,(r,c) in enumerate(rooms)}
N=len(rooms)
adj=[[] for _ in range(N)]
dir4=[(1,0),(-1,0),(0,1),(0,-1)]
for r,c in rooms:
    i=pos_id[(r,c)]
    for dr,dc in dir4:
        nr,nc=r+dr,c+dc
        if 0<=nr<R and 0<=nc<C and office[nr][nc]=='.':
            j=pos_id[(nr,nc)]
            adj[i].append(j)
all_ids=[pos_id[t] for t in tasks]
# Precompute dist, path on tree using BFS
def bfs(start):
    dist=[-1]*N
    dist[start]=0
    q=[start]
    for u in q:
        for w in adj[u]:
            if dist[w]<0:
                dist[w]=dist[u]+1
                q.append(w)
    return dist
dists=[bfs(i) for i in range(N)]
# Path reconstruction on tree
parents=[[-1]*N for _ in range(N)]
for i in range(N):
    q=[i]
    parents[i][i]=-2
    for u in q:
        for w in adj[u]:
            if parents[i][w]<0:
                parents[i][w]=u
                q.append(w)
def get_path(s,t):
    path=[]
    cur=t
    while cur!=s:
        path.append(cur)
        cur=parents[s][cur]
    path.append(s)
    path.reverse()
    return path
# DP state: pos, light_status per room (only the rooms in current path)
# but memory for all rooms is impossible
# Plan: DP through tasks only, dp[pos][light_on?]
# but for minimal cost including turning on/off and duration, we consider:
# For each task transition: from prev to next task, we move on unique path.
# On each room on path, we decide on/off, so total per room cost.
# Since only one path between rooms, path rooms are linear.
# For each task segment, process minimal cost to go from prev task to next.
# Light on/off decisions:
# We must have light on when entering room, and at leaving choice: on/off
# Try DP on path rooms:
# state: index in path, light on/off
# Transitions:
# at position i, if light is off:
#   need to turn on light: cost oncost+ptime until next step
# at position i, if light is on:
#   cost ptime
# exiting last room: must turn off light, cost offcost
# Implement segment DP
def segment_cost(path):
    L=len(path)
    dp=[[10**15]*2 for _ in range(L+1)]
    # At position 0, entering first room must switch on light, cost oncost
    r,c=rooms[path[0]]
    dp[1][1]=oncost[r][c]+ptime[r][c]
    for i in range(1,L):
        r,c=rooms[path[i]]
        for l in range(2):
            if dp[i][l]>=10**15:
                continue
            # keep light on
            cost1=dp[i][l]+ptime[r][c]
            dp[i+1][1]=min(dp[i+1][1],cost1)
            # if light on, can turn off then on again=> but that would add cost, no reason to off here except last room
            # if light off at i+1:
            cost2=dp[i][l]+oncost[r][c]+ptime[r][c]
            dp[i+1][1]=min(dp[i+1][1],cost2)
    # last room must end with light off: so turn off light
    r,c=rooms[path[-1]]
    res=10**15
    for l in range(2):
        v=dp[L][l]
        if l==1:
            v+=offcost[r][c]
        res=min(res,v)
    return res
total=0
for i in range(M-1):
    s=all_ids[i]
    t=all_ids[i+1]
    path=get_path(s,t)
    total+=segment_cost(path)
# For first task:
r,c=rooms[all_ids[0]]
total+=oncost[r][c]+ptime[r][c]
# For last task:
r,c=rooms[all_ids[-1]]
total+=offcost[r][c]
print(total)