import os
import sys

import numpy as np

def grid_pairing_maxflow(row_count, col_count, grid_mask):
    COORD_SHIFT = 9
    COORD_MASK = (1 << COORD_SHIFT) - 1

    def encode_coords(row, col):
        return (row << COORD_SHIFT) | col

    def decode_coords(encoded):
        return encoded >> COORD_SHIFT, encoded & COORD_MASK

    mf_graphs = []

    def mf_graph_init(vertex_count):
        base = [[0, 0, 0]]
        base.clear()
        mf_graphs.append([base.copy() for _ in range(vertex_count)])
        return len(mf_graphs) - 1

    def mf_add_edge(graph_id, from_v, to_v, cap):
        adj = mf_graphs[graph_id]
        adj[from_v].append([to_v, cap, len(adj[to_v])])
        adj[to_v].append([from_v, 0, len(adj[from_v]) - 1])

    def mf_bfs(graph_id, vertex_count, source):
        adj = mf_graphs[graph_id]
        levels = np.full(vertex_count, -1, dtype=np.int64)
        levels[source] = 0
        queue = np.zeros(vertex_count + 5, dtype=np.int64)
        l, r = 0, 1
        queue[0] = source
        while l < r:
            u = queue[l]
            l += 1
            for edge in adj[u]:
                if edge[1] > 0 and levels[edge[0]] == -1:
                    levels[edge[0]] = levels[u] + 1
                    queue[r] = edge[0]
                    r += 1
        return levels

    def mf_dfs(graph_id, levels, next_ptr, s, t):
        adj = mf_graphs[graph_id]
        stack = [(s, 10 ** 18)]
        block_flow = 0
        while stack:
            v, pushed = stack.pop()
            if v == t:
                block_flow = pushed
                continue
            if block_flow == 0:
                i = next_ptr[v]
                if i == len(adj[v]):
                    continue
                next_ptr[v] += 1
                stack.append((v, pushed))
                to, cap, rev = adj[v][i]
                if cap == 0 or levels[v] >= levels[to]:
                    continue
                stack.append((to, min(pushed, cap)))
            else:
                i = next_ptr[v] - 1
                edge = adj[v][i]
                edge[1] -= block_flow
                adj[edge[0]][edge[2]][1] += block_flow
        return block_flow

    def mf_max_flow(graph_id, vertex_count, source, sink):
        total_flow = 0
        while True:
            levels = mf_bfs(graph_id, vertex_count, source)
            if levels[sink] == -1:
                return total_flow
            next_ptr = np.zeros(vertex_count, dtype=np.int64)
            pushed = mf_dfs(graph_id, levels, next_ptr, source, sink)
            while pushed != 0:
                total_flow += pushed
                pushed = mf_dfs(graph_id, levels, next_ptr, source, sink)

    left_nodes = []
    right_nodes = []
    right_node_idx = {}

    for row in range(1, row_count + 1):
        for col in range(1, col_count + 1):
            if grid_mask[row, col]:
                continue
            coord_enc = encode_coords(row, col)
            if (row ^ col) & 1:
                left_nodes.append(coord_enc)
            else:
                right_node_idx[coord_enc] = len(right_nodes)
                right_nodes.append(coord_enc)
    left_n = len(left_nodes)
    right_n = len(right_nodes)
    v_source = left_n + right_n
    v_sink = v_source + 1
    v_count = v_sink + 1

    mf_id = mf_graph_init(v_count)

    DELTAS = (-(1 << COORD_SHIFT), -1, 1, 1 << COORD_SHIFT)

    for i in range(left_n):
        coord = left_nodes[i]
        for delta in DELTAS:
            neighbor = coord + delta
            if neighbor in right_node_idx:
                mf_add_edge(mf_id, i, right_node_idx[neighbor] + left_n, 1)
        mf_add_edge(mf_id, v_source, i, 1)
    for j in range(right_n):
        mf_add_edge(mf_id, j + left_n, v_sink, 1)

    pair_flow = mf_max_flow(mf_id, v_count, v_source, v_sink)
    adj = mf_graphs[mf_id]

    for i in range(left_n):
        for edge in adj[i]:
            if edge[0] == v_source or edge[1] == 1:
                continue
            j = edge[0] - left_n
            r1, c1 = decode_coords(left_nodes[i])
            r2, c2 = decode_coords(right_nodes[j])
            if r1 == r2:
                if c1 > c2:
                    c1, c2 = c2, c1
                grid_mask[r1, c1] = 4
                grid_mask[r2, c2] = 5
            else:
                if r1 > r2:
                    r1, r2 = r2, r1
                grid_mask[r1, c1] = 2
                grid_mask[r2, c2] = 3
            break

    return pair_flow

CALL_SIG = '(i8,i8,i1[:,:],)'
if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    pycc_obj = CC('my_module')
    pycc_obj.export('grid_pairing_maxflow', CALL_SIG)(grid_pairing_maxflow)
    pycc_obj.compile()
    exit()

if os.name == 'posix':
    from my_module import grid_pairing_maxflow
else:
    from numba import njit

    grid_pairing_maxflow = njit(CALL_SIG, cache=True)(grid_pairing_maxflow)
    print('compiled', file=sys.stderr)

n, m = map(int, input().split())
mask_grid = np.ones((n + 2, m + 2), dtype=np.int8)
for line_idx in range(n):
    mask_grid[line_idx + 1, 1:m + 1] = list(map('.#'.index, input()))

maxflow_res = grid_pairing_maxflow(n, m, mask_grid)
print(maxflow_res)
CELL_CHARS = '.#v^><'.__getitem__
for row in range(1, n + 1):
    print(''.join(map(CELL_CHARS, mask_grid[row, 1:m + 1])))