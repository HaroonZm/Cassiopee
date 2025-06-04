from collections import deque

H,W,N=map(int,input().split())
grid=[list(input()) for _ in range(H)]

# Directions: up, down, left, right
directions=[(-1,0),(1,0),(0,-1),(0,1)]

# Find positions of head 'S' and bodies 'a','b','c','d','e' in order, and food positions indexed by number
pos_dict={}
for i in range(H):
    for j in range(W):
        c=grid[i][j]
        if c=='S' or c in "abcde":
            pos_dict[c]=(i,j)
        elif c.isdigit():
            pos_dict[int(c)]=(i,j)

# Build worm body positions list from 'S' then 'a'.. as per input
body_chars=['S','a','b','c','d','e']
worm_body=[]
for ch in body_chars:
    if ch in pos_dict:
        worm_body.append(pos_dict[ch])

# Precompute food targets in order 1..N
foods=[pos_dict[i] for i in range(1,N+1)]

def is_valid(r,c):
    return 0<=r<H and 0<=c<W and grid[r][c]!='#'

from sys import maxsize
visited=set()
# State: (head_r, head_c, (body_r1, body_c1, ..., body_r5, body_c5), food_index)
start=(worm_body[0], tuple(worm_body[1:]), 0)
visited.add((worm_body[0], tuple(worm_body[1:]), 0))
queue=deque()
queue.append( (worm_body[0], tuple(worm_body[1:]), 0, 0) ) # head_pos, body_positions, food_index, steps

while queue:
    head, body, fi, steps=queue.popleft()
    if fi==N:
        print(steps)
        break
    for dr,dc in directions:
        nh,nc=head[0]+dr, head[1]+dc
        if not is_valid(nh,nc):
            continue
        
        # Check if nh,nc is in worm body or obstacles (before movement)
        if (nh,nc) in body:
            # The only exception is if tail moves out from this cell after movement
            # Because worm moves forward, tail leaves its cell, so moving into tail's current cell is allowed
            tail=body[-1] if body else None
            if tail!=(nh,nc):
                continue
        
        # New body positions after movement
        new_body=[head]+list(body[:-1]) if body else [head]
        new_body=tuple(new_body)
        
        # Check collision: head not on body after move
        if (nh,nc) in new_body:
            continue
        
        # Check if on current food
        new_fi=fi
        if fi<N and (nh,nc)==foods[fi]:
            new_fi=fi+1
        
        state=((nh,nc), new_body, new_fi)
        if state in visited:
            continue
        visited.add(state)
        queue.append( ((nh,nc), new_body, new_fi, steps+1) )
else:
    print(-1)