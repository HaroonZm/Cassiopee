from collections import deque
import sys

def read_input_dimensions():
    readline = sys.stdin.readline
    W, H = map(int, readline().split())
    return W, H, readline

def build_initial_maps(W, H, readline):
    MP = [readline() for _ in range(H)]
    return MP

def prepare_data_structures(W, H):
    A = [[-1]*W for _ in range(H)]
    B = [[-1]*W for _ in range(H)]
    C = [[0]*W for _ in range(H)]
    return A, B, C

def fill_A_B(MP, A, B, SW0, SW1):
    sx = sy = gx = gy = -1
    for i, mp in enumerate(MP):
        Ai, Bi = A[i], B[i]
        for j, c in enumerate(mp):
            if c == '#':
                continue
            if c in '^' or c in SW0:
                Ai[j] = 1
                if c != '^':
                    Bi[j] = SW0.index(c)+1
            elif c in '_%&' or c in SW1:
                Ai[j] = 0
                if c == '%':
                    sx, sy = j, i
                elif c == '&':
                    gx, gy = j, i
                elif c != '_':
                    Bi[j] = SW1.index(c)+1
            elif c == '|':
                Bi[j] = 0
                Ai[j] = 2
    return sx, sy, gx, gy

def read_switch_maps(S, H, W, readline):
    return [[readline() for _ in range(H)] for _ in range(S)]

def update_C_with_switches(switch_maps, C, S, H, W):
    for k, MP in enumerate(switch_maps):
        for i, mp in enumerate(MP):
            Ci = C[i]
            for j, c in enumerate(mp):
                if c == '*':
                    Ci[j] |= (2 << k)

def prepare_bitcount(S):
    bc = [0]*(2 << S)
    for i in range(1, 2 << S):
        bc[i] = bc[i ^ (i & -i)] ^ 1
    return bc

def prepare_distance_struct(W, H):
    return [[{} for _ in range(W)] for _ in range(H)]

def bfs(W, H, A, B, C, sx, sy, gx, gy, S, bc, write):
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    dist = prepare_distance_struct(W, H)
    dist[sy][sx][0] = 0
    que = deque([(0, sx, sy, 0)])
    while que:
        state, x, y, d = que.popleft()
        handle_cell_switch(B, state, x, y, d, dist, que, C, A, bc)
        explore_neighbors(W, H, A, dist, que, state, x, y, d, C, bc)
    if dist[gy][gx]:
        write("%d\n" % min(dist[gy][gx].values()))
    else:
        write("-1\n")

def handle_cell_switch(B, state, x, y, d, dist, que, C, A, bc):
    if B[y][x] == 0:
        try_switch_zero(dist, y, x, state, d, que)
    elif B[y][x] != -1:
        try_switch_nonzero(B, y, x, state, d, dist, que, C, A, bc)

def try_switch_zero(dist, y, x, state, d, que):
    new_state = state^1
    if new_state not in dist[y][x]:
        dist[y][x][new_state] = d+1
        que.append((new_state, x, y, d+1))

def try_switch_nonzero(B, y, x, state, d, dist, que, C, A, bc):
    bxy = B[y][x]
    n_state = state ^ (1 << bxy) ^ (state & 1)
    n_state ^= bc[n_state & C[y][x]] ^ A[y][x]
    if n_state not in dist[y][x]:
        dist[y][x][n_state] = d+1
        que.append((n_state, x, y, d+1))

def explore_neighbors(W, H, A, dist, que, state, x, y, d, C, bc):
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    for dx, dy in dd:
        nx, ny = x + dx, y + dy
        if is_invalid_neighbor(nx, ny, W, H, A):
            continue
        if A[ny][nx] == 2:
            try_pipe(dist, ny, nx, state, d, que)
        else:
            try_normal(A, dist, que, state, nx, ny, d, C, bc)

def is_invalid_neighbor(nx, ny, W, H, A):
    return not (0 <= nx < W and 0 <= ny < H) or A[ny][nx] == -1

def try_pipe(dist, ny, nx, state, d, que):
    if state not in dist[ny][nx]:
        dist[ny][nx][state] = d+1
        que.append((state, nx, ny, d+1))

def try_normal(A, dist, que, state, nx, ny, d, C, bc):
    np = bc[state & C[ny][nx]] ^ A[ny][nx]
    if state&1 == np and state not in dist[ny][nx]:
        dist[ny][nx][state] = d+1
        que.append((state, nx, ny, d+1))

def main():
    W, H, readline = read_input_dimensions()
    MP = build_initial_maps(W, H, readline)
    A, B, C = prepare_data_structures(W, H)
    SW0, SW1 = 'ABCDEFGHIJ', 'abcdefghij'
    sx, sy, gx, gy = fill_A_B(MP, A, B, SW0, SW1)
    S = int(readline())
    switch_maps = [build_initial_maps(W, H, readline) for _ in range(S)]
    update_C_with_switches(switch_maps, C, S, H, W)
    bc = prepare_bitcount(S)
    write = sys.stdout.write
    bfs(W, H, A, B, C, sx, sy, gx, gy, S, bc, write)

main()