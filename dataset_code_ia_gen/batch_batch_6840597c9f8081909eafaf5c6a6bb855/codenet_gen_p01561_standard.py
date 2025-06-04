from collections import deque

W, H = map(int, input().split())
grid = [list(input()) for _ in range(H)]
S = int(input())
switch_maps = [ [list(input()) for _ in range(H)] for _ in range(S)]

# Map switch letters to index 0-based
def switch_idx(c):
    if c >= 'a' and c <= 'j':
        return ord(c) - ord('a')
    elif c >= 'A' and c <= 'J':
        return ord(c) - ord('A')
    return -1

# Find start and goal positions and floor states
start = None
goal = None
initial_floor = [[-1]*W for _ in range(H)]  # 0:first, 1:second, -1 wall
for y in range(H):
    for x in range(W):
        c = grid[y][x]
        if c == '#':
            initial_floor[y][x] = -1
        elif c == '_':
            initial_floor[y][x] = 0
        elif c == '^':
            initial_floor[y][x] = 1
        elif c == '%':
            initial_floor[y][x] = 0
            start = (x,y)
        elif c == '&':
            initial_floor[y][x] = 0
            goal = (x,y)
        elif c == '|':
            initial_floor[y][x] = 2  # stairs special
        elif c.islower():
            initial_floor[y][x] = 0
        elif c.isupper():
            initial_floor[y][x] = 1

# For each grid, determine switches controlling it (bitmask)
controlled_by = [[0]*W for _ in range(H)]
for k in range(S):
    for y in range(H):
        for x in range(W):
            if switch_maps[k][y][x] == '*':
                controlled_by[y][x] |= (1<<k)

def is_wall(x,y):
    return initial_floor[y][x]==-1

def is_stairs(x,y):
    return initial_floor[y][x]==2

def floor_after_flip(floor, mask, x, y):
    # If floor is stairs (2), it we treat as on both floors (you can switch there)
    # Otherwise flip floor if controlled_by[y][x] is set and corresponding switch is on
    if initial_floor[y][x]==-1:
        return -1
    if initial_floor[y][x]==2:
        return 2
    flips = bin(controlled_by[y][x] & mask).count('1')
    # Each active switch affecting tile flips its floor
    res = floor ^ (flips % 2)
    return res

from sys import setrecursionlimit
setrecursionlimit(10**7)

visited = [[[False]*(1<<S) for _ in range(H)] for __ in range(W)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# Initial floor of start is 0 first floor
q = deque()
q.append((start[0],start[1],0,0))  # x,y,switch_mask,steps
visited[start[0]][start[1]][0] = True

while q:
    x,y,m,steps = q.popleft()
    cf = floor_after_flip(0,m,x,y)
    # If currently on stairs, floor 2 means stairs floor
    # but floor_after_flip returns 2 if stairs: treat stairs as both floors
    # So current floor can be 0 or 1 or stairs(2)
    # But floor_after_flip return 2 only for stairs
    # Original floor is fixed as 0, so flips apply
    # The floor we are currently on is 0 or 1, floor_after_flip gives actual floor of tile

    # To check if we can stand here, find actual floor state of tile
    # The problem states moves only on same floor, stairs can move floors

    # We track floor as separate state to move, but since floor_after_flip encodes real floor of tile,
    # we need to find current floor of tile (0 or 1) after flips to check if standable

    # We stored floor as 0 always in floor_after_flip, so we need a binary floor state to track in BFS.
    # Because floor_after_flip returns final floor (0/1) or 2(stairs)
    # So we should keep track of player's current floor and check if tile matches

    # But here floor is not tracked directly, fix: add floor state to BFS state

# Fix approach: track current floor in state as well

# Reset and redo with floor in state

visited = [[[[False]*(1<<S) for _ in range(2)] for _ in range(H)] for __ in range(W)]

# Determine initial floor at start tile after flips=0; actual floor for tile at that mask
def floor_tile(mask, x, y):
    if is_wall(x,y):
        return -1
    if is_stairs(x,y):
        # stairs tile can be accessed on both floors
        return 2
    f0 = initial_floor[y][x]
    flips = bin(controlled_by[y][x] & mask).count('1')
    return f0 ^ (flips%2)

q = deque()
start_floor = floor_tile(0,start[0],start[1])
if start_floor == 2:
    # stairs means player can be on floor 0 or 1 here, check start floor=0 first
    start_floor = 0
q.append((start[0],start[1],start_floor,0,0))  # x,y,floor,switch_mask,steps
visited[start[0]][start[1]][start_floor][0] = True

while q:
    x,y,f,m,steps = q.popleft()
    if (x,y) == goal:
        # check if player is on same floor as goal floor
        gf = floor_tile(m,x,y)
        if gf == 2 or gf == f:
            print(steps)
            exit()
    # Move to adjacent same floor tiles (including stairs)
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0<=nx<W and 0<=ny<H:
            if is_wall(nx,ny):
                continue
            tf = floor_tile(m,nx,ny)
            if tf==-1:
                continue
            # can move only if tile floor matches player's current floor or stairs (2)
            if tf==f or tf==2:
                if not visited[nx][ny][f][m]:
                    visited[nx][ny][f][m] = True
                    q.append((nx,ny,f,m,steps+1))
    # If on stairs, can change floor by one step
    if is_stairs(x,y):
        nf = 1-f
        if not visited[x][y][nf][m]:
            visited[x][y][nf][m] = True
            q.append((x,y,nf,m,steps+1))
    # If on switch tile, can operate switch (flip one bit)
    c = grid[y][x]
    si = switch_idx(c)
    if si >= 0:
        nm = m^(1<<si)
        # After operating switch, check if current tile floor flips accordingly for player
        # Player on floor f, but tile may move under player and floor can flip if tile controlled
        nf = floor_tile(nm,x,y)
        # if nf == 2 stairs, player can be on floor f or nf == player floor after flips
        # need to keep player's floor same unless tile changes floor - but player moves with tile if controlled by switch
        # If tile containing switch is moved by that switch, player moves with it (floor flips)
        # So if tile's floor flips, player's floor flips, else player's floor stays the same
        # Check if current tile is controlled by this switch (bit si)
        if (controlled_by[y][x] & (1<<si)) != 0:
            # tile flips floor, so player's floor also flips
            pf = 1 - f
        else:
            # tile floor unchanged, player's floor unchanged
            pf = f
        if not visited[x][y][pf][nm]:
            visited[x][y][pf][nm]=True
            q.append((x,y,pf,nm,steps+1))

print(-1)