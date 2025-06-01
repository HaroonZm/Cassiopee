from collections import deque
import sys

def read_dimensions(file):
    line = file.readline()
    if not line:
        return None, None
    w, h = map(int, line.split())
    return w, h

def read_grid(file, w, h):
    rows = [file.readline().split() for _ in range(h)]
    grid = [cell for row in rows for cell in row]
    return grid

def is_valid_position(x, y, w, h):
    return 0 <= x < w and 0 <= y < h

def get_position_index(x, y, w):
    return y * w + x

def get_pre_color(s, pos):
    return s[pos]

def add_neighbors(que, x, y, w, h):
    if x > 0: que.append((x-1,y))
    if y > 0: que.append((x,y-1))
    if x + 1 < w: que.append((x+1,y))
    if y + 1 < h: que.append((x,y+1))

def paintout_sq_get_neighbors(s, color, w, h, x, y):
    def get_neighbor_set():
        return set()
    neighbor = get_neighbor_set()
    pre_color = get_pre_color(s, get_position_index(x,y,w))
    que = deque()
    que.append((x,y))
    while len(que):
        xcur, ycur = que.pop()
        pos = get_position_index(xcur, ycur, w)
        if s[pos] == pre_color:
            s[pos] = color
            add_neighbors(que, xcur, ycur, w, h)
        elif s[pos] != color and isinstance(s[pos], int):
            neighbor.update([s[pos]])
    return neighbor

def try_extend_graph(graph, key, values):
    if key in graph:
        graph[key].extend(values)
    else:
        graph[key] = values

def try_append_graph(graph, key, value):
    if key in graph:
        graph[key].append(value)
    else:
        graph[key] = [value]

def build_graph(w, h, s):
    p = []
    graph = {}
    for y in range(h):
        for x in range(w):
            pos = get_position_index(x, y, w)
            if s[pos] in ('R', 'G', 'B'):
                k = len(p)
                p.append(s[pos])
                neighbor = paintout_sq_get_neighbors(s, k, w, h, x, y)
                neighbor_list = list(neighbor)
                try_extend_graph(graph, k, neighbor_list)
                for ni in neighbor_list:
                    try_append_graph(graph, ni, k)
    return p, graph

def paintout_graph(s, g, color):
    cnt = 0
    pre_color = s[0]
    que = [0]
    i = 0
    while i < len(que):
        pos = que[i]
        i += 1
        if s[pos] == pre_color:
            s[pos] = color
            cnt += 1
            que.extend(g.get(pos, []))
    return cnt

def prepare_colors(pre_color):
    colors = ['R', 'G', 'B']
    colors.remove(pre_color)
    return colors

def bfs(s, graph):
    que = deque()
    que.append((s, 0, 0))
    while True:
        s_current, pre_cnt, depth = que.popleft()
        pre_color = s_current[0]
        colors = prepare_colors(pre_color)
        for si, color in zip((s_current, s_current[:]), colors):
            cnt = paintout_graph(si, graph, color)
            if cnt == len(si):
                return depth
            if cnt == pre_cnt:
                break
            que.append((si, cnt, depth + 1))

def main_loop():
    f = sys.stdin
    while True:
        w, h = read_dimensions(f)
        if w == 0 and h == 0:
            break
        s = read_grid(f, w, h)
        p, graph = build_graph(w, h, s)
        print(bfs(p, graph))

main_loop()