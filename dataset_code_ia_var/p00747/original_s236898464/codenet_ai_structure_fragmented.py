from collections import deque

def create_grid(w, h):
    return [[10 ** 6 for _ in range(w)] for _ in range(h)]

def read_w_h():
    w, h = map(int, input().split())
    return w, h

def is_end(w, h):
    return (w, h) == (0, 0)

def read_vertical_horizantal(h):
    vertical = []
    horizantal = []
    for i in range(2 * h - 1):
        line = list(map(int, input().split()))
        if i % 2 == 0:
            vertical.append(line)
        else:
            horizantal.append(line)
    return vertical, horizantal

def initialize_queue():
    return deque([(0, 0)])

def initialize_g(G):
    G[0][0] = 0

def valid_horizontal(nexte, w):
    return 0 <= nexte[1] < w

def valid_vertical(nexte, h):
    return 0 <= nexte[0] < h

def should_move_vertical(move_1, vertical, now, nexte):
    if move_1 == 1:
        return vertical[now[0]][now[1]] == 0
    elif move_1 == -1:
        return vertical[nexte[0]][nexte[1]] == 0
    return False

def should_move_horizantal(move_0, horizantal, now, nexte):
    if move_0 == 1:
        return horizantal[now[0]][now[1]] == 0
    elif move_0 == -1:
        return horizantal[nexte[0]][nexte[1]] == 0
    return False

def should_update(G, nexte, now):
    return G[nexte[0]][nexte[1]] > G[now[0]][now[1]] + 1

def update_queue_g(G, queue, nexte, now):
    G[nexte[0]][nexte[1]] = G[now[0]][now[1]] + 1
    queue.append((nexte[0], nexte[1]))

def process_horizontal_moves(now, w, G, vertical, queue):
    dw = [(0, -1), (0, 1)]
    for move in dw:
        nexte = (now[0], now[1] + move[1])
        if not valid_horizontal(nexte, w):
            continue
        if should_move_vertical(move[1], vertical, now, nexte):
            if should_update(G, nexte, now):
                update_queue_g(G, queue, nexte, now)

def process_vertical_moves(now, h, G, horizantal, queue):
    dh = [(1, 0), (-1, 0)]
    for move in dh:
        nexte = (now[0] + move[0], now[1])
        if not valid_vertical(nexte, h):
            continue
        if should_move_horizantal(move[0], horizantal, now, nexte):
            if should_update(G, nexte, now):
                update_queue_g(G, queue, nexte, now)

def bfs(w, h, G, vertical, horizantal):
    queue = initialize_queue()
    initialize_g(G)
    while queue:
        now = queue.popleft()
        process_horizontal_moves(now, w, G, vertical, queue)
        process_vertical_moves(now, h, G, horizantal, queue)

def print_output(G, h, w):
    if G[h - 1][w - 1] == 10 ** 6:
        print(0)
    else:
        print(G[h - 1][w - 1] + 1)

def solve_once():
    w, h = read_w_h()
    if is_end(w, h):
        return False
    G = create_grid(w, h)
    vertical, horizantal = read_vertical_horizantal(h)
    bfs(w, h, G, vertical, horizantal)
    print_output(G, h, w)
    return True

def main():
    while solve_once():
        pass

main()