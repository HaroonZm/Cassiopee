import sys
from string import ascii_lowercase, ascii_uppercase
from collections import deque

readline = sys.stdin.readline
write = sys.stdout.write
dd = ((1, 0), (0, 1))

def input_hw():
    return map(int, readline().split())

def is_end_case(H, W):
    return H == W == 0

def read_grid(H):
    return [readline().strip() for _ in range(H)]

def init_INF():
    return 10**9

def init_used(H, W):
    return [[0]*W for _ in range(H)]

def mark_used(used, y, x):
    used[y][x] = 1

def should_enqueue(C, used, y, x, H, W):
    return (x < W and y < H and C[y][x] != '#' and not used[y][x])

def gather_neighbors(x, y, H, W):
    neighbors = []
    if x+1 < W:
        neighbors.append((x+1, y))
    if y+1 < H:
        neighbors.append((x, y+1))
    return neighbors

def in_bounds(x, y, W, H):
    return 0 <= x < W and 0 <= y < H

def search(C, x0, y0, c):
    H = len(C)
    W = len(C[0])
    que = deque([(x0, y0)])
    used = init_used(H, W)
    mark_used(used, y0, x0)
    r = []
    while que:
        x, y = que.popleft()
        if c is None or C[y][x] == c:
            r.append((x, y))
        for nx, ny in gather_neighbors(x, y, H, W):
            if in_bounds(nx, ny, W, H) and C[ny][nx] != '#' and not used[ny][nx]:
                que.append((nx, ny))
                mark_used(used, ny, nx)
    return r, used

def is_reachable(U, H, W):
    return U[H-1][W-1]

def write_fail():
    write("-1\n")

def create_empty(H, W, fill):
    return [[fill for _ in range(W)] for _ in range(H)]

def find_lowercase_index(ch):
    return ascii_lowercase.find(ch)

def uppercase_from_index(k):
    return ascii_uppercase[k] if k != -1 else None

def preprocess(C, H, W):
    D = create_empty(H, W, None)
    U = create_empty(H, W, None)
    K = create_empty(H, W, -1)
    for i in range(H):
        for j in range(W):
            d = C[i][j]
            if d == '#':
                continue
            k = find_lowercase_index(C[i][j])
            c = uppercase_from_index(k)
            D[i][j], U[i][j] = search(C, j, i, c)
            K[i][j] = k
    return D, U, K

def create_4d(H, W, fill):
    return [[[[fill for _ in range(W)] for _ in range(H)] for _ in range(W)] for _ in range(H)]

def get_dp_transition(dp, i0, j0, i1, j1, C):
    vals = []
    if i0+1 <= i1 and C[i0+1][j0] != '#':
        vals.append(dp[i0+1][j0][i1][j1])
    else:
        vals.append(0)
    if j0+1 <= j1 and C[i0][j0+1] != '#':
        vals.append(dp[i0][j0+1][i1][j1])
    else:
        vals.append(0)
    return max(vals)

def can_use(U, i0, j0, i1, j1):
    return U[i0][j0][i1][j1]

def calc_A(i0, j0, y, x, dp, C):
    if (x-j0)+(y-i0) == 1:
        return 1
    if i0 == y:
        return dp[i0][j0+1][y][x-1] + 1
    elif j0 == x:
        return dp[i0+1][j0][y-1][x] + 1
    else:
        vals = [
            dp[i0+1][j0][y][x-1],
            dp[i0][j0+1][y-1][x]
        ]
        if i0+1 <= y-1:
            vals.append(dp[i0+1][j0][y-1][x])
        else:
            vals.append(0)
        if j0+1 <= x-1:
            vals.append(dp[i0][j0+1][y][x-1])
        else:
            vals.append(0)
        return max(vals) + 1

def should_continue(D, U, i0, j0, i1, j1, x, y):
    if not (i0 <= y <= i1 and j0 <= x <= j1):
        return False
    if not U[i0][j0][y][x]:
        return False
    if not U[y][x][i1][j1]:
        return False
    return True

def process_dp(dp, D, U, K, C, H, W):
    for i0 in range(H-1, -1, -1):
        for j0 in range(W-1, -1, -1):
            if C[i0][j0] == '#':
                continue
            k = K[i0][j0]
            for i1 in range(H-1, i0-1, -1):
                for j1 in range(W-1, j0-1, -1):
                    if not can_use(U, i0, j0, i1, j1):
                        continue
                    r = get_dp_transition(dp, i0, j0, i1, j1, C)
                    if k != -1:
                        for x, y in D[i0][j0]:
                            if not should_continue(D, U, i0, j0, i1, j1, x, y):
                                continue
                            A = calc_A(i0, j0, y, x, dp, C)
                            r = max(r, A + dp[y][x][i1][j1])
                    dp[i0][j0][i1][j1] = r

def output_result(dp, H, W):
    write("%d\n" % dp[0][0][H-1][W-1])

def solve():
    H, W = input_hw()
    if is_end_case(H, W):
        return False
    C = read_grid(H)
    INF = init_INF()
    D0, U0 = search(C, 0, 0, None)
    if not is_reachable(U0, H, W):
        write_fail()
        return True
    D, U, K = preprocess(C, H, W)
    dp = create_4d(H, W, 0)
    process_dp(dp, D, U, K, C, H, W)
    output_result(dp, H, W)
    return True

while solve():
    ...