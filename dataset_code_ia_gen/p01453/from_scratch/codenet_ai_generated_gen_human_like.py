import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

W,H=map(int,input().split())
maze=[list(input().rstrip()) for _ in range(H)]

floor_positions=[]
pos_s=None
pos_g=None

for y in range(H):
    for x in range(W):
        c=maze[y][x]
        if c=='s':
            pos_s=(y,x)
            floor_positions.append((y,x))
            maze[y][x]='.'
        elif c=='g':
            pos_g=(y,x)
            floor_positions.append((y,x))
        elif c=='.':
            floor_positions.append((y,x))

# 4-direction moves
dy=[1,-1,0,0]
dx=[0,0,1,-1]

# dp[y][x]: expected value to escape from (y,x)
# We want to solve:
# E(g)=0
# For other floor tiles:
# E(v)=1+min over moves of expected cost
# If next tile is floor or g: cost=E(next)
# If next tile is '*': cost= average E over all floor positions
# Because from '*' we jump to random floor tile (excluding g and *),
# but the problem states only floor tiles excluding g and * for random jumps.
# Note: 'g' tile is not considered a floor tile for jumps from '*'
# So floor_positions above excluded '*' and 'g', but problem states '階段、バネのタイルは除く'
# So floor_positions must exclude g and '*'
# Our floor_positions includes g, so we remove g for jump targets:
jump_positions=[(y,x) for y,x in floor_positions if maze[y][x]=='.']

# We will build a map to get the expectation values.
from collections import deque
INF = 10**18
E=[[INF]*W for _ in range(H)]
for y,x in floor_positions:
    E[y][x]=0 if (y,x)==pos_g else INF

# To accelerate convergence, use value iteration.
# Observations:
# - From a normal cell, move to four neighbors and cost is 1 + expected of next cell.
# - From a cell, among possible moves, choose minimal expectation.
# - From a cell, if move to '*', expectation is 1 + average over all jump positions.
# - From '*' cell, expectation is known via average.

# But from '*' we don't move: stepping on '*' triggers jump, but moving on '*' from other tiles counts as 1 move.
# Problem says jumping is instantaneous and no move count added for jump.

# When standing on '*', you don't move, you are immediately teleported to random floor tile.
# So E for '*' is equal to average E over all jump_positions (floor tiles except g and *).
# But actually we can handle this by treating '*' tiles as normal tiles with no walkable steps,
# because landing on '*' immediately lands you to random floor tile.

# Let's get all positions of '*'
spring_positions=[]
for y in range(H):
    for x in range(W):
        if maze[y][x]=='*':
            spring_positions.append((y,x))

# We will perform value iteration until convergence:
# For each floor tile (including s and g):
#   E = 0 if g
#   else E = min over neighbors:
#       if neighbor is '.': 1 + E[neighbor]
#       if neighbor is 'g': 1 + 0 =1
#       if neighbor is '*': 1 + avg E over jump_positions

# For tiles '*': E = avg E over jump_positions

# So first we initialize:
# For each '*' update E[y][x] = avg E over jump_positions
# Initially, E[g]=0, others large

# Iteration count: about 5000 max for accuracy, but careful with time
# We will use a threshold for convergence

jump_positions_count=len(jump_positions)

def average_E():
    s=0
    for y,x in jump_positions:
        s+=E[y][x]
    return s/jump_positions_count if jump_positions_count>0 else 0

# Initialize E for spring positions to avg_E
avgE=0
if jump_positions_count>0:
    avgE = average_E()
for y,x in spring_positions:
    E[y][x]=avgE

MAX_ITER=10000
EPS=1e-14
for _ in range(MAX_ITER):
    updated=False
    avgE = average_E() if jump_positions_count>0 else 0
    # Update springs
    for y,x in spring_positions:
        if abs(E[y][x]-avgE)>EPS:
            E[y][x]=avgE
            updated=True
    # Update floors (includes s and g)
    for y,x in floor_positions:
        if (y,x)==pos_g:
            continue
        best=INF
        for d in range(4):
            ny=y+dy[d]
            nx=x+dx[d]
            if 0<=ny<H and 0<=nx<W:
                c=maze[ny][nx]
                if c=='#':
                    continue
                if c=='.':
                    cost=1+E[ny][nx]
                elif c=='g':
                    cost=1+0
                elif c=='*':
                    cost=1+avgE
                else:
                    # s treated as '.' (converted), so never here
                    continue
                if cost<best:
                    best=cost
        if abs(E[y][x]-best)>EPS:
            E[y][x]=best
            updated=True
    if not updated:
        break

y,x=pos_s
print("{:.12f}".format(E[y][x]))