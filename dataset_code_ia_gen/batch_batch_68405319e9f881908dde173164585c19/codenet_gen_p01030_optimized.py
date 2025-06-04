from collections import deque

H, W = map(int, input().split())
areas = []
start = goal = None

area0 = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if area0[i][j] == 'S':
            start = (i, j)
        elif area0[i][j] == 'G':
            goal = (i, j)
areas.append(area0)

N = int(input())
times = []
for _ in range(N):
    T = int(input())
    area = [list(input()) for _ in range(H)]
    times.append(T)
    areas.append(area)

# Prepend initial time 0
times = [0] + times
max_T = times[-1]
# For convenience, add a last time after last change to handle infinity
times.append(10**9)

# Directions: up, down, left, right, stay
dirs = [(-1,0),(1,0),(0,-1),(0,1),(0,0)]

# Function to get the area index at time t
def get_area_index(t):
    # times sorted ascending with sentinel times[-1]=large number
    # t < times[i+1] and t >= times[i]
    # binary search
    l, r = 0, len(times)-1
    while l < r:
        m = (l+r)//2
        if times[m] <= t < times[m+1]:
            return m
        if t < times[m]:
            r = m
        else:
            l = m+1
    return l

from sys import maxsize

# BFS (Dijkstra-like) to find minimal steps (walking moves)
# state: (time, x, y)
# use a dist dictionary: key=(t,x,y), but t can be large
# Optimize: since grid changes only at times in times[], we can limit search

# We can implement BFS over (t, x, y) with time increasing, 
# but t can be large. Since max T is at most 200 + movement max

# We limit max time to max allowed: max times[-2]+H*W*2 (safe upper bound)
max_time = times[-2] + H*W*4

# visited[(x,y,t)] but t huge, we store minimal walking steps to reach (x,y) at time t
# Since state space can be large, we use a dict keyed by (x,y,t)
# But t up to ~1000, and H,W max 20 -> max 20*20*1000=400k states feasible

from heapq import heappush, heappop
dist = {}

hq = []
# initial state: at time 0, position start, steps 0
# heap: (steps, time, x, y)
heappush(hq, (0,0,start[0],start[1]))
dist[(start[0],start[1],0)] = 0

res = -1

while hq:
    steps, t, x, y = heappop(hq)
    if (x,y) == goal:
        res = steps
        break
    # pruning
    if dist.get((x,y,t), maxsize) < steps:
        continue
    if t >= max_time:
        continue
    area_i = get_area_index(t)
    area_i1 = get_area_index(t+1)
    grid = areas[area_i]
    grid_next = areas[area_i1]

    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        nsteps = steps + (0 if (dx,dy) == (0,0) else 1)
        nt = t+1
        if 0 <= nx < H and 0 <= ny < W:
            # Move allowed in next grid if cell is not '#'
            if grid_next[nx][ny] != '#':
                key = (nx, ny, nt)
                if dist.get(key, maxsize) > nsteps:
                    dist[key] = nsteps
                    heappush(hq, (nsteps, nt, nx, ny))

print(res)