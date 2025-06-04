from collections import deque

N=int(input())
stamps=[tuple(map(int,input().split())) for _ in range(N)]
target=[input() for _ in range(4)]

color_map={'R':0,'G':1,'B':2}
target_colors=[color_map[c] for row in target for c in row]

# Precompute all possible stamp applications:
# Each stamp can be placed at positions (r,c), r in [-H_i+1,4), c in [-W_i+1,4) to allow partial overlap
# For each possible placement and color, create a mask that covers affected cells with that color

def inside(r,c):
    return 0<=r<4 and 0<=c<4

actions=[]
for i,(h,w) in enumerate(stamps):
    for top in range(-h+1,4):
        for left in range(-w+1,4):
            # For each position, determine affected cells inside 4x4
            covered=[]
            for dr in range(h):
                for dc in range(w):
                    rr=top+dr
                    cc=left+dc
                    if inside(rr,cc):
                        covered.append(rr*4+cc)
            if not covered:
                continue
            # For each color
            for color in range(3):
                # Prepare a list representing the color per cell after stamping
                # We'll store as a tuple of length 16 where each entry is 0,1,2 or -1 meaning no change
                # But to optimize, we use a mask of changed cells and the color they have after stamping
                # For BFS, we can simulate the stamping by overwriting these cells with this color

                actions.append( (covered,color) )

# BFS over color states
# Represent a state as a tuple of length 16, each 0(R)/1(G)/2(B)/-1(initial)
# Initial state all -1 (meaning no color)
# Goal is target_colors

start=tuple([-1]*16)
goal=tuple(target_colors)

from collections import deque
visited={start:0}
q=deque([start])
while q:
    state=q.popleft()
    if state==goal:
        print(visited[state])
        break
    dist=visited[state]
    for covered,color in actions:
        # Apply action
        new_state=list(state)
        changed=False
        for pos in covered:
            if new_state[pos]!=color:
                new_state[pos]=color
                changed=True
        if not changed:
            continue
        new_state_t=tuple(new_state)
        if new_state_t not in visited:
            visited[new_state_t]=dist+1
            q.append(new_state_t)