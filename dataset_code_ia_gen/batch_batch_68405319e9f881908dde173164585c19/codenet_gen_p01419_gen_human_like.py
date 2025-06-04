import sys
from collections import deque
sys.setrecursionlimit(10**7)

R, C, M = map(int, sys.stdin.readline().split())
office = [list(sys.stdin.readline().strip()) for _ in range(R)]

time_cost = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
on_cost = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
off_cost = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

tasks = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

# We'll treat rooms as nodes in a tree (since exactly one route exists between any pair)
# First, recognize all positions of rooms and create an adjacency list
# We'll connect each room to adjacent rooms (up/down/left/right) if not wall

adj = {}
rooms = []
pos_to_id = {}

id_counter = 0
for r in range(R):
    for c in range(C):
        if office[r][c] == '.':
            pos_to_id[(r,c)] = id_counter
            rooms.append((r,c))
            id_counter += 1

for r,c in rooms:
    nid = pos_to_id[(r,c)]
    adj[nid] = []
    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and office[nr][nc] == '.':
            adj[nid].append(pos_to_id[(nr,nc)])

# Precompute parent and depth for each node to find paths efficiently and cost of travel on path
# Root arbitrarily at tasks[0]

root = pos_to_id[tasks[0]]

parent = [-1]*id_counter
depth = [-1]*id_counter
parent[root] = root
depth[root] = 0

q = deque([root])
while q:
    u = q.popleft()
    for v in adj[u]:
        if depth[v] == -1:
            depth[v] = depth[u] + 1
            parent[v] = u
            q.append(v)

# Precompute 2^k parent for LCA queries
LOG = 16
ancestor = [[-1]*id_counter for _ in range(LOG)]
for i in range(id_counter):
    ancestor[0][i] = parent[i]

for k in range(1, LOG):
    for i in range(id_counter):
        ancestor[k][i] = ancestor[k-1][ancestor[k-1][i]]

def lca(u,v):
    if depth[u] < depth[v]:
        u, v = v, u
    # Lift u up to depth[v]
    diff = depth[u]-depth[v]
    for k in range(LOG):
        if diff & (1<<k):
            u = ancestor[k][u]
    if u == v:
        return u
    for k in reversed(range(LOG)):
        if ancestor[k][u] != ancestor[k][v]:
            u = ancestor[k][u]
            v = ancestor[k][v]
    return parent[u]

# Compute path from u to v as list of nodes
def path_nodes(u,v):
    a = lca(u,v)
    res = []
    # u to a (excluding a)
    x = u
    tmp = []
    while x != a:
        tmp.append(x)
        x = parent[x]
    res.extend(tmp)
    res.append(a)
    # v to a (excluding a), reversed
    tmp = []
    x = v
    while x != a:
        tmp.append(x)
        x = parent[x]
    res.extend(reversed(tmp))
    return res

# For each room index, get coordinates
def idx_to_r_c(i):
    return rooms[i]

# The problem is about minimizing electric power consumption consisting of:
# - for each unit of time in a room with light ON, pay time_cost
# - for each on/off switch in that room, pay on_cost or off_cost

# We move along the paths between tasks in order:
# from tasks[i-1] to tasks[i], we have a path
# moving from one room to adjacent room takes 1 unit time
# When entering a room, light must be switched ON if off.
# When leaving, can switch off or leave on.

# Since it's a tree with unique path between any two rooms, to minimize power consumption we will consider:
# For each room in the path, how many times do we enter/leave, when switch on/off to minimize total cost.

# Key observation:
# For each edge in the path between tasks, we walk it forward once.

# But light management cost depends on when to switch on/off in each room.

# Since tasks order is linear, and no revisiting tasks before finishing them, path is concatenation of paths between tasks.

# Plan:
# Build full route by concatenating paths between each pair of consecutive tasks.
# Then, for the entire route, consider the light switching strategy.

# Because the graph is a tree and the route is unique and simple path:
# The entire route is a sequence of rooms visited in order.

# Important: we want minimal total power consumed.
# We must switch ON when entering a room (unless already ON from previous stay).
# We can leave light ON if we return to the room soon.
# Finally, after finishing all tasks, all lights OFF.

# Because tasks can revisit rooms (allowed), for the problem as described, the route is a concatenation of paths, rooms can repeat.

# Idea:
# We want to minimize summation over rooms of:
# - number of ON/OFF switches * corresponding costs
# - total time spent with light ON * per unit time cost

# Since the problem size is large, we cannot try all combinations per room.

# But given route as sequence of rooms visited, with times spent (1 unit per move), we can group consecutive visits to a room into intervals where light can stay ON.

# Because switching on/off costs are significant, it's better to turn on light at first visit to a room and turn off at last visit in a continuous interval.

# But if the room is not visited continuously (separated by visits to other rooms), we must turn off and later on again.

# The route is a path: repeated visits can happen if paths between tasks overlap.

# Let's build the sequence of rooms visited on the full route.

route = []
for i in range(M-1):
    u = pos_to_id[tasks[i]]
    v = pos_to_id[tasks[i+1]]
    if i == 0:
        # full path
        p = path_nodes(u, v)
    else:
        # exclude first node of path to avoid duplication, because last of previous path = first of next
        p = path_nodes(u, v)[1:]
    route.extend(p)
# Add last task if not included
if M == 1:
    route = [pos_to_id[tasks[0]]]
else:
    if route[-1] != pos_to_id[tasks[-1]]:
        route.append(pos_to_id[tasks[-1]])

# Now we have a list of rooms as indices.

# For each step:
# we spend 1 time unit at room route[i] (since moving from previous room)
# except the first room, where we start - the problem states switching on light when entering (we start inside that room and need the light ON)
# Actually, the first room costs at least one ON operation at start.

# Time spent per room can be counted:
# We'll consider the time spent in a room as number of consecutive visits in a run.

# Let's collapse route into segments of consecutive rooms that are the same:
# But since moving each step costs 1 time unit and we move to adjacent room:
# So time spent in each room is number of transitions ending in it? No,
# Actually we spend 1 unit of time moving from room i-1 to room i, so for each room except the first, we spend 1 unit time inside it.
# The first room is start, so does it cost time? No movement to it, but the problem states you must switch ON when entering a room (so for first room the light is ON from start), and the time in that room is zero before moving out

# For simplicity:
# For each index i in route:
# time spent in room route[i] = 1 if i>0 else 0 (because moving into this room takes 1 unit)
# So total time in room = number of times room appears except at index 0

# But this is path moving room-to-room, each move costs 1 time unit inside the destination room.

# Actually, the problem states moving to next room costs 1 unit time, the light in that room is ON => pay per unit time cost.

# For the first room, no time spent before any move, so 0 time cost but must pay ON cost.

# For the last room, no move after, so no time cost after visit, but must turn light off at end if ON.

# So plan:
# For each room in the route at i>0, add 1 unit time with light ON.

# Next, find intervals where the room light can stay ON continuously.

# The sequence of visits may have gaps (non consecutive visits to same room).

# For each room, find all visit indices in route.

visits = [[] for _ in range(id_counter)]
for i, r in enumerate(route):
    visits[r].append(i)

# For each room, we can split its visits into consecutive intervals separated by 1 apart indices

intervals = []
for r in range(id_counter):
    if not visits[r]:
        continue
    inds = visits[r]
    start = inds[0]
    end = inds[0]
    for i in inds[1:]:
        if i == end + 1:
            end = i
        else:
            intervals.append((r, start, end))
            start = i
            end = i
    intervals.append((r, start, end))

# Each interval represents a continuous segment of visits in the route for room r.

# For each interval, light must be switched ON at start, switched OFF at end+1 or later if next interval

# For time cost:
# time inside room r = number of steps in interval where i>0

# i>0 means all indices > 0, the first position in route corresponds to i=0.

# Calculate time units in interval:
# time units = count of indices > 0 in [start, end]

def time_units_in_interval(start, end):
    cnt = 0
    for x in range(start, end+1):
        if x > 0:
            cnt += 1
    return cnt

# Total cost per interval:
# cost = ON cost at room r + OFF cost at room r + time_cost * time units

# We'll sum over all intervals of all rooms
# Finally, output sum

total = 0
for r, start, end in intervals:
    t_units = time_units_in_interval(start, end)
    total += on_cost[rooms[r][0]][rooms[r][1]]
    total += off_cost[rooms[r][0]][rooms[r][1]]
    total += time_cost[rooms[r][0]][rooms[r][1]] * t_units

print(total)