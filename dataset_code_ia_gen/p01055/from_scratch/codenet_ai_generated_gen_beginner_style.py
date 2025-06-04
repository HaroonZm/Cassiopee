from collections import deque

W, H, N = map(int, input().split())
sx, sy = map(int, input().split())

paths = []
lengths = []
for _ in range(N):
    data = list(map(int, input().split()))
    L = data[0]
    path = [(data[i], data[i+1]) for i in range(1, 2*L, 2)]
    lengths.append(L)
    paths.append(path)

# Create a map of fire positions by time for each wick
# fire_positions[i][t] = position of fire i at time t, or None if fire finished
max_time = 0
fire_positions = []
for i in range(N):
    pos_list = paths[i]
    L = lengths[i]
    # Fire moves forward 1 step per second, starting at t=0 at pos_list[0]
    # Fire stays at positions until it reaches the bomb
    # At time t, if t < L, fire is at pos_list[t], else None
    fire_positions.append(pos_list)
    if L > max_time:
        max_time = L

# Directions robot can move: 8 directions + staying
dirs = []
for dx in [-1,0,1]:
    for dy in [-1,0,1]:
        dirs.append((dx,dy))

# Check if a position is inside grid
def in_grid(x,y):
    return 1 <= x <= W and 1 <= y <= H

# Check if bomb exists at position
bomb_positions = set()
for i in range(N):
    bomb_positions.add(paths[i][-1])

# BFS state: (x,y,time,fires_bitmask)
# fires_bitmask bit i means fire i still exists (not extinguished)
from collections import deque

start_fire_mask = (1 << N) -1

# At time=0 robot at (sx,sy)
# At time=0, if robot on any fire position, extinguish those fires
def fires_at(time, x, y):
    exist = []
    for i in range(N):
        # Fire i at time t is at position paths[i][t] if t < lengths[i]
        if time < lengths[i]:
            if paths[i][time] == (x,y):
                exist.append(i)
    return exist

init_fires = set()
for i in range(N):
    if 0 < lengths[i] and paths[i][0] == (sx,sy):
        init_fires.add(i)
fire_mask = start_fire_mask
for i in init_fires:
    fire_mask &= ~(1 << i)

visited = set()
q = deque()
q.append( (sx, sy, 0, fire_mask) )
visited.add( (sx, sy, 0, fire_mask) )

while q:
    x,y,t,f_mask = q.popleft()
    # If all fires extinguished
    if f_mask == 0:
        print(t)
        break

    # Check if any fire reaches bomb at next time t+1 => bomb explodes => fail
    bomb_will_explode = False
    for i in range(N):
        if (f_mask & (1 << i)) != 0:
            # Fire i position at t+1
            next_time = t + 1
            if next_time == lengths[i] - 1:
                # At the last position but will move to bomb at next step, bomb explodes
                # Actually fire at last position length-1 is the bomb position
                # The problem states bomb explodes when fire arrives at bomb cell,
                # So at time t = lengths[i]-1, fire is at bomb position, explosion immediately
                # So bomb explodes at t = lengths[i]-1
                bomb_will_explode = True
            elif next_time >= lengths[i]:
                # Fire gone (exploded or finished), no problem
                continue
            else:
                # fire not at bomb yet
                continue
    if bomb_will_explode:
        # This state is invalid, skip
        continue

    # Robot moves or stays (dirs)
    for dx,dy in dirs:
        nx = x + dx
        ny = y + dy
        nt = t +1

        if not in_grid(nx, ny):
            continue
        if (nx, ny) in bomb_positions:
            continue

        # Check bomb explosion at time nt due to fire nt == lengths[i]-1 ?
        bomb_explode = False
        for i in range(N):
            if f_mask & (1 << i):
                # If fire at time nt is at bomb position => explode
                if nt == lengths[i]-1:
                    bomb_explode = True
                    break
        if bomb_explode:
            continue

        # Check fires at nt on robot position => extinguish those fires
        extinguished = []
        for i in range(N):
            if f_mask & (1 << i):
                if nt < lengths[i]:
                    if paths[i][nt] == (nx,ny):
                        extinguished.append(i)
        nf_mask = f_mask
        for i in extinguished:
            nf_mask &= ~(1 << i)

        state = (nx, ny, nt, nf_mask)
        if state in visited:
            continue
        visited.add(state)
        q.append(state)
else:
    print(-1)