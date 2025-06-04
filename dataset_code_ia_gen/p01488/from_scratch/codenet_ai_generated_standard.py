import sys
import heapq

input=sys.stdin.readline
N,T=map(int,input().split())
A,B=input().split()

station_id={}
def get_id(s):
    if s not in station_id:
        station_id[s]=len(station_id)
    return station_id[s]

lines=[]
pos_in_line=[]
offset=0
for _ in range(N):
    a=int(input())
    stations=input().split()
    times=list(map(int,input().split()))
    lines.append((stations,times))
    pos_in_line.append({})
    for i,s in enumerate(stations):
        pos_in_line[-1].setdefault(s,[]).append(i)

if A not in station_id: get_id(A)
if B not in station_id: get_id(B)
for stations,_ in lines:
    for s in stations:
        get_id(s)

# Build graph: states are (line index, position)
# transitions:
# - move on the same line to adjacent positions
# - transfer at the same station (including same station different positions in the same line)
inf=10**15
# For each line and position, create a node index
node_idx=[]
count=0
for i,(stations,times) in enumerate(lines):
    node_idx.append([0]*len(stations))
    for j in range(len(stations)):
        node_idx[i][j]=count
        count+=1

# Graph edges: adjacency list: node->(neighbor,cost,time_change)
# time_change=1 if transfer else 0
graph=[[] for _ in range(count)]

for i,(stations,times) in enumerate(lines):
    l=len(stations)
    for j in range(l):
        if j>0:
            c=times[j-1]
            graph[node_idx[i][j]].append((node_idx[i][j-1],c,0))
            graph[node_idx[i][j-1]].append((node_idx[i][j],c,0))

# Add transfer edges between all nodes representing the same station but different line/pos
# Including different positions on the same line but requiring transfer
station_nodes={}
for i,(stations,_) in enumerate(lines):
    for j,s in enumerate(stations):
        sid=station_id[s]
        station_nodes.setdefault(sid,[]).append((i,j))

for sid,nlist in station_nodes.items():
    for idx1 in range(len(nlist)):
        i1,j1=nlist[idx1]
        n1=node_idx[i1][j1]
        for idx2 in range(idx1+1,len(nlist)):
            i2,j2=nlist[idx2]
            n2=node_idx[i2][j2]
            # If same line and same station position, skip (same node)
            # If same line but different positions, must transfer
            if i1==i2 and j1==j2:
                continue
            # Transfer edge with cost T and +1 transfer count
            graph[n1].append((n2,T,1))
            graph[n2].append((n1,T,1))

start_nodes=[node_idx[i][j] for i,(stations,_) in enumerate(lines) for j,s in enumerate(stations) if s==A]
goal_nodes={node_idx[i][j] for i,(stations,_) in enumerate(lines) for j,s in enumerate(stations) if s==B}

# Dijkstra with state: (time, transfer, node)
dist=[[inf,inf] for _ in range(count)] # [time, transfer]
h=[]
for s in start_nodes:
    dist[s]=[0,0]
    heapq.heappush(h,(0,0,s))

while h:
    t,curr_tr,n=heapq.heappop(h)
    if dist[n][0]<t or (dist[n][0]==t and dist[n][1]<curr_tr):
        continue
    if n in goal_nodes:
        print(t,curr_tr)
        break
    for nxt,dt,tc in graph[n]:
        nt=t+dt
        nc=curr_tr+tc
        if dist[nxt][0]>nt or (dist[nxt][0]==nt and dist[nxt][1]>nc):
            dist[nxt]=[nt,nc]
            heapq.heappush(h,(nt,nc,nxt))
else:
    print(-1)