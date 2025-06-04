from collections import deque

W,H=map(int,input().split())
lab=[list(input()) for _ in range(H)]

S=int(input())
switch_maps=[]
for _ in range(S):
    switch_maps.append([list(input()) for __ in range(H)])

# Directions for move
dx=[0,1,0,-1]
dy=[-1,0,1,0]

# Find start and goal
for y in range(H):
    for x in range(W):
        if lab[y][x]=='%':
            start=(x,y)
        if lab[y][x]=='&':
            goal=(x,y)

# Map switches to their index 0..S-1
switch_pos = {}
for y in range(H):
    for x in range(W):
        c=lab[y][x]
        if c.isalpha():
            # lowercase a-j or uppercase A-J
            ind=ord(c.lower())-ord('a')
            if ind<S:
                switch_pos[(x,y)] = ind

# For each cell, which switches move it
moved_by = [[[] for _ in range(W)] for __ in range(H)]
for k in range(S):
    for y in range(H):
        for x in range(W):
            if switch_maps[k][y][x]=='*':
                moved_by[y][x].append(k)

# initial floors per cell
# 0=first floor,1=second floor, -1=wall
floor_map = [[-1]*W for _ in range(H)]
for y in range(H):
    for x in range(W):
        c=lab[y][x]
        if c=='#':
            floor_map[y][x]=-1
        elif c=='|' :
            floor_map[y][x]=0 # stairs on first floor (stairs always exist on both floors)
        elif c=='_':
            floor_map[y][x]=0
        elif c=='^':
            floor_map[y][x]=1
        elif c=='%':
            floor_map[y][x]=0
        elif c=='&':
            floor_map[y][x]=0
        elif c.isalpha():
            if c.islower():
                floor_map[y][x]=0
            else:
                floor_map[y][x]=1
        else:
            floor_map[y][x]= -1 # safety catch, shouldn't happen

# To know if a cell moves if switch k is flipped, store bitmask for each cell
# We'll use an integer with S bits to encode which switches have been flipped (on/off)
# Actually, the problem means that each switch swaps floor for some cells
# Note, operating switch toggles the states of all cells moved by that switch.

# floor for a cell after toggling switches state:
# floor_of_cell ^ parity_of_toggles_of_switches_that_move_it

def is_accessible(x,y,f,sw_state):
    # f = current floor, sw_state bits
    # first check wall
    if x<0 or x>=W or y<0 or y>=H:
        return False
    if floor_map[y][x]<0:
        return False
    # check floor
    # get toggling parity for this cell
    parity=0
    for k in moved_by[y][x]:
        if (sw_state>>k)&1:
            parity ^=1
    cell_floor = floor_map[y][x]^parity
    return cell_floor==f

# BFS state: (x,y,floor,switch_state)
from collections import deque
visited = [[ [False]*(1<<S) for _ in range(W)] for __ in range(H)]
q = deque()

sx,sy = start
start_floor= floor_map[sy][sx]
start_state=0

visited[sy][sx][start_state]=True
q.append((sx,sy,start_floor,start_state,0))  # x,y,floor,switch_state, steps

while q:
    x,y,f,sw,step = q.popleft()
    if (x,y)==goal and f== floor_map[goal[1]][goal[0]] ^ sum(((sw>>k)&1) for k in moved_by[goal[1]][goal[0]])%2:
        print(step)
        exit()
    # Move to adjacent same floor
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if is_accessible(nx,ny,f,sw):
            if not visited[ny][nx][sw]:
                visited[ny][nx][sw]=True
                q.append((nx,ny,f,sw,step+1))
    # If on stairs, can change floor without moving position
    if lab[y][x]=='|' :
        nf = 1-f
        if is_accessible(x,y,nf,sw):
            if not visited[y][x][sw]:
                visited[y][x][sw]=True
                q.append((x,y,nf,sw,step+1))
    # If have switch here, can toggle switch
    if (x,y) in switch_pos:
        sw_i = switch_pos[(x,y)]
        nsw = sw ^ (1<<sw_i)
        if not visited[y][x][nsw]:
            visited[y][x][nsw]=True
            # Note: The current grid may move floors if it is moved by the toggled switch
            # So position may change floor automatically; but position stays the same in grid coords.
            # We keep f as current floor, but floor of cell changes due to toggling.
            # So update current f to cell's new floor:
            parity=0
            for k in moved_by[y][x]:
                if (nsw>>k)&1:
                    parity ^=1
            nf = floor_map[y][x]^parity
            q.append((x,y,nf,nsw,step+1))
print(-1)