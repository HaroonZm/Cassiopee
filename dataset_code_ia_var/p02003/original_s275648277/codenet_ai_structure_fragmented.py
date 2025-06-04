import sys

def input():
    return sys.stdin.readline().strip()

def list2d(a, b, c):
    return [[c] * b for _ in range(a)]

def list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def list4d(a, b, c, d, e):
    return [[[[e] * d for _ in range(c)] for _ in range(b)] for _ in range(a)]

def ceil(x, y=1):
    return int(-(-x // y))

def INT():
    return int(input())

def MAP():
    return map(int, input().split())

def LIST(N=None):
    return list(MAP()) if N is None else [INT() for _ in range(N)]

def Yes():
    print('Yes')

def No():
    print('No')

def YES():
    print('YES')

def NO():
    print('NO')

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

class Dinic:
    """ 最大流(Dinic) """

    INF = 10 ** 18

    def __init__(self, n):
        self.n = n
        self.links = [[] for _ in range(n)]
        self.depth = None
        self.progress = None

    def add_link(self, _from, to, cap):
        self.links[_from].append([cap, to, len(self.links[to])])
        self.links[to].append([0, _from, len(self.links[_from]) - 1])

    def bfs(self, s):
        from collections import deque
        self._init_depth_bfs(s)
    
    def _init_depth_bfs(self, s):
        self.depth = [-1] * self.n
        self._bfs_process(s)
    
    def _bfs_process(self, s):
        from collections import deque
        self.depth[s] = 0
        q = deque([s])
        self._bfs_queue(q)
    
    def _bfs_queue(self, q):
        while q:
            v = q.popleft()
            self._bfs_for_links(v, q)
    
    def _bfs_for_links(self, v, q):
        for cap, to, _ in self.links[v]:
            if cap > 0 and self.depth[to] < 0:
                self.depth[to] = self.depth[v] + 1
                q.append(to)

    def dfs(self, v, t, flow):
        return self._dfs_main(v, t, flow)

    def _dfs_main(self, v, t, flow):
        if self._dfs_is_sink(v, t):
            return flow
        links_v = self.links[v]
        for i in range(self.progress[v], len(links_v)):
            self.progress[v] = i
            cap, to, rev = link = links_v[i]
            if self._dfs_is_invalid(cap, v, to):
                continue
            d = self._dfs_sub(to, t, flow, cap)
            if d == 0:
                continue
            link[0] -= d
            self.links[to][rev][0] += d
            return d
        return 0

    def _dfs_is_sink(self, v, t):
        return v == t

    def _dfs_is_invalid(self, cap, v, to):
        return cap == 0 or self.depth[v] >= self.depth[to]

    def _dfs_sub(self, to, t, flow, cap):
        return self.dfs(to, t, min(flow, cap))

    def max_flow(self, s, t):
        return self._max_flow_main(s, t)

    def _max_flow_main(self, s, t):
        INF = Dinic.INF
        flow = 0
        while True:
            self.bfs(s)
            if self._is_no_path_to_sink(t):
                return flow
            self.progress = [0] * self.n
            current_flow = self._max_flow_dfs_cycle(s, t, INF)
            while current_flow > 0:
                flow += current_flow
                current_flow = self._max_flow_dfs_cycle(s, t, INF)

    def _is_no_path_to_sink(self, t):
        return self.depth[t] < 0

    def _max_flow_dfs_cycle(self, s, t, start_flow):
        return self.dfs(s, t, start_flow)

def build_grid(H, W, intv, _type, space=True, padding=False):
    _input = _build_grid_input_lambda(space)
    _list = lambda: list(map(_type, _input()))
    offset = _build_grid_padding_offset(padding)
    grid = list2d(H+offset*2, W+offset*2, intv)
    _build_grid_fill(grid, H, W, offset, _list)
    return grid

def _build_grid_input_lambda(space):
    return (lambda: input().split()) if space else (lambda: input())

def _build_grid_padding_offset(padding):
    return 1 if padding else 0

def _build_grid_fill(grid, H, W, offset, _list):
    for i in range(offset, H+offset):
        row = _list()
        for j in range(offset, W+offset):
            grid[i][j] = row[j-offset]

def main():
    H, W = _read_HW()
    grid = _make_grid(H, W)
    N, adjcnt, total = _count_grid_stats(H, W, grid)
    dinic, s, t = _construct_dinic(H, W, adjcnt)
    _add_links(dinic, grid, H, W, N, adjcnt, s, t)
    res = _calculate_max_flow(dinic, s, t)
    ans = _calculate_answer(total, adjcnt, res)
    _output_answer(ans)

def _read_HW():
    return MAP()

def _make_grid(H, W):
    return build_grid(H, W, '', str, space=0)

def _count_grid_stats(H, W, grid):
    N = H * W
    total = 0
    adjcnt = 0
    for i in range(H):
        for j in range(W):
            total, adjcnt = _process_cell_stats(i, j, H, W, grid, total, adjcnt)
    return N, adjcnt, total

def _process_cell_stats(i, j, H, W, grid, total, adjcnt):
    if grid[i][j] == '#':
        total += 1
        if _is_adjacency_down(i, H, grid, j):
            adjcnt += 1
        if _is_adjacency_right(j, W, grid, i):
            adjcnt += 1
    return total, adjcnt

def _is_adjacency_down(i, H, grid, j):
    return i+1 < H and grid[i+1][j] == '#'

def _is_adjacency_right(j, W, grid, i):
    return j+1 < W and grid[i][j+1] == '#'

def _construct_dinic(H, W, adjcnt):
    N = H * W
    dinic = Dinic(N+adjcnt+2)
    s = N + adjcnt
    t = N + adjcnt + 1
    return dinic, s, t

def _add_links(dinic, grid, H, W, N, adjcnt, s, t):
    k = N
    for i in range(H):
        for j in range(W):
            k = _maybe_add_vertical(dinic, grid, H, W, i, j, s, k)
            k = _maybe_add_horizontal(dinic, grid, H, W, i, j, t, k)

def _maybe_add_vertical(dinic, grid, H, W, i, j, s, k):
    if i+1 < H and grid[i][j] == grid[i+1][j] == '#':
        _add_vertical_links(dinic, s, k, i, j, W, H)
        k += 1
    return k

def _maybe_add_horizontal(dinic, grid, H, W, i, j, t, k):
    if j+1 < W and grid[i][j] == grid[i][j+1] == '#':
        _add_horizontal_links(dinic, t, k, i, j, W, H)
        k += 1
    return k

def _add_vertical_links(dinic, s, k, i, j, W, H):
    dinic.add_link(s, k, 1)
    dinic.add_link(k, i*W+j, INF)
    dinic.add_link(k, (i+1)*W+j, INF)

def _add_horizontal_links(dinic, t, k, i, j, W, H):
    dinic.add_link(k, t, 1)
    dinic.add_link(i*W+j, k, INF)
    dinic.add_link(i*W+j+1, k, INF)

def _calculate_max_flow(dinic, s, t):
    return dinic.max_flow(s, t)

def _calculate_answer(total, adjcnt, res):
    return total - (adjcnt - res)

def _output_answer(ans):
    print(ans)

if __name__ == '__main__':
    main()