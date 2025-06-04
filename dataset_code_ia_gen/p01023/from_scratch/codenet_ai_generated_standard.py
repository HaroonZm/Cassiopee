from collections import deque

H, W, N = map(int, input().split())
area = [list(input()) for _ in range(H)]

# Find positions of worm parts and sort by 'S','a','b','c','d','e'
worm_chars = ['S','a','b','c','d','e']
worm_pos = [None]*6
for r in range(H):
    for c in range(W):
        ch = area[r][c]
        if ch in worm_chars:
            worm_pos[worm_chars.index(ch)] = (r,c)

# Find food positions indexed by their number 1..N
food_pos = [None]*N
for r in range(H):
    for c in range(W):
        ch = area[r][c]
        if ch.isdigit():
            idx = int(ch)-1
            if 0 <= idx < N:
                food_pos[idx] = (r,c)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def in_area(r,c):
    return 0 <= r < H and 0 <= c < W

def can_move(head_next, body):
    r,c = head_next
    if not in_area(r,c):
        return False
    if area[r][c] == '#':
        return False
    # Check if new head position coincides with any body after moving
    # After moving: new_body = [old_head]+body[:-1]
    # We must ensure new head does not collide with new body positions
    new_body = [worm_pos[0]]+body[:-1]
    if (r,c) in new_body:
        return False
    return True

# State: (head_r,head_c, b1_r,b1_c, ..., b5_r,b5_c, next_food_idx)
start_body = worm_pos[1:]
visited = set()
start = (*worm_pos[0], *(pos for p in start_body for pos in p), 0)
visited.add(start)
q = deque()
q.append( (start,0) )

while q:
    state, dist = q.popleft()
    head = (state[0],state[1])
    body = [(state[2*i+2], state[2*i+3]) for i in range(5)]
    food_i = state[12]

    if food_i == N:
        print(dist)
        break

    for d in range(4):
        nr = head[0]+dr[d]
        nc = head[1]+dc[d]
        if not in_area(nr,nc):
            continue
        if area[nr][nc] == '#':
            continue

        # The new body positions after move
        new_body = [head]+body[:-1]
        # Head must not move into any of current body positions (except tail)
        # Because tail vacates its cell, we allow head to step on tail's current pos
        # So check collision with body except last segment
        if (nr,nc) in new_body:
            continue

        # After move, head at (nr,nc), if there is food at that cell and food_i matches, eat it
        n_food_i = food_i
        if food_i < N and (nr,nc) == food_pos[food_i]:
            n_food_i +=1

        new_state = (nr,nc) + tuple(pos for p in new_body for pos in p) + (n_food_i,)
        if new_state not in visited:
            visited.add(new_state)
            q.append( (new_state, dist+1) )
else:
    print(-1)