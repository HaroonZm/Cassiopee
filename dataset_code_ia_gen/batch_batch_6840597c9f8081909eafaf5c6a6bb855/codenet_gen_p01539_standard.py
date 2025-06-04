from collections import deque

dx = [1, 0, -1, -1, 0, 1]
dy = [0, 1, 1, 0, -1, -1]

sx, sy, gx, gy = map(int, input().split())
n = int(input())
furnitures = set(tuple(map(int, input().split())) for _ in range(n))
lx, ly = map(int, input().split())

def in_bounds(x, y):
    return -lx <= x <= lx and -ly <= y <= ly

# State: (x, y, t) t = time mod 6
# We want min ignores, so use Dijkstra-like BFS with a deque storing (ignore count, x,y,t)
# We'll use 3D dp to track minimal ignore counts
INF = 10**9
dist = [[[INF]*6 for _ in range(2*ly+1)] for __ in range(2*lx+1)]

def idx_x(x): return x+lx
def idx_y(y): return y+ly

que = deque()
t0 = 0
dist[idx_x(sx)][idx_y(sy)][t0] = 0
que.append((sx, sy, t0))

while que:
    x, y, t = que.popleft()
    c = dist[idx_x(x)][idx_y(y)][t]
    if (x, y) == (gx, gy):
        print(c)
        break
    next_t = (t+1) %6
    instructed_dir = (x*y*t) %6
    # try all 7 moves: directions 0-5 + stay
    for move_dir in range(7):
        if move_dir == 6:
            nx, ny = x, y
        else:
            nx, ny = x+dx[move_dir], y+dy[move_dir]
        if not in_bounds(nx, ny):
            continue
        if (nx, ny) in furnitures:
            continue
        ignore = 0 if (move_dir == instructed_dir) else 1
        # if stay is chosen, it never matches any dir (ignore=1), unless instructed_dir==6 (impossible)
        # so no special case needed
        nc = c + ignore
        idxnx, idxny = idx_x(nx), idx_y(ny)
        if dist[idxnx][idxny][next_t] > nc:
            dist[idxnx][idxny][next_t] = nc
            if ignore == 0:
                que.appendleft((nx, ny, next_t))
            else:
                que.append((nx, ny, next_t))
else:
    print(-1)