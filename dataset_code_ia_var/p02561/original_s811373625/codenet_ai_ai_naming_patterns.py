import sys
from collections import deque
from copy import deepcopy

sys.setrecursionlimit(10**7)

def input_map_int():
    return map(int, sys.stdin.readline().rstrip().split())

def input_list_str_no_space():
    return list(sys.stdin.readline().rstrip())

class DinicAlgo:
    def __init__(self, node_cnt):
        self.node_cnt = node_cnt
        self.graph_adj = [[] for _ in range(node_cnt)]

    def add_edge(self, from_node, to_node, capacity):
        edge_fwd = [to_node, capacity, None]
        edge_fwd[2] = edge_bwd = [from_node, 0, edge_fwd]
        self.graph_adj[from_node].append(edge_fwd)
        self.graph_adj[to_node].append(edge_bwd)

    def add_bidirectional_edge(self, node_u, node_v, cap_uv, cap_vu):
        edge_uv = [node_v, cap_uv, None]
        edge_uv[2] = edge_vu = [node_u, cap_vu, edge_uv]
        self.graph_adj[node_u].append(edge_uv)
        self.graph_adj[node_v].append(edge_vu)

    def bfs_level(self, src, dst):
        self.level_arr = level_arr = [None] * self.node_cnt
        node_queue = deque([src])
        level_arr[src] = 0
        while node_queue:
            cur_node = node_queue.popleft()
            next_level = level_arr[cur_node] + 1
            for neighbor, capacity, _ in self.graph_adj[cur_node]:
                if capacity and level_arr[neighbor] is None:
                    level_arr[neighbor] = next_level
                    node_queue.append(neighbor)
        return level_arr[dst] is not None

    def dfs_flow(self, cur, dst, flow_limit):
        if cur == dst:
            return flow_limit
        for edge in self.current_iter[cur]:
            neighbor, capacity, rev_edge = edge
            if capacity and self.level_arr[cur] < self.level_arr[neighbor]:
                pushed = self.dfs_flow(neighbor, dst, min(flow_limit, capacity))
                if pushed:
                    edge[1] -= pushed
                    rev_edge[1] += pushed
                    return pushed
        return 0

    def max_flow(self, src, dst):
        flow_result = 0
        INF_CAP = 10 ** 9 + 7
        while self.bfs_level(src, dst):
            self.current_iter = list(map(iter, self.graph_adj))
            while True:
                pushed_flow = self.dfs_flow(src, dst, INF_CAP)
                if not pushed_flow:
                    break
                flow_result += pushed_flow
        return flow_result

row_cnt, col_cnt = input_map_int()
grid_matrix = [input_list_str_no_space() for _ in range(row_cnt)]

dinic_instance = DinicAlgo(row_cnt * col_cnt + 2)
src_node = row_cnt * col_cnt
dst_node = row_cnt * col_cnt + 1

for r in range(row_cnt):
    for c in range(col_cnt):
        grid_pos = col_cnt * r + c
        if (r + c) % 2 == 0:
            dinic_instance.add_edge(src_node, grid_pos, 1)
        else:
            dinic_instance.add_edge(grid_pos, dst_node, 1)

for r in range(row_cnt - 1):
    for c in range(col_cnt):
        if grid_matrix[r][c] == grid_matrix[r + 1][c] == '.':
            pos1 = col_cnt * r + c
            pos2 = col_cnt * (r + 1) + c
            u, v = (pos2, pos1) if (r + c) % 2 == 1 else (pos1, pos2)
            dinic_instance.add_edge(u, v, 1)

for r in range(row_cnt):
    for c in range(col_cnt - 1):
        if grid_matrix[r][c] == grid_matrix[r][c + 1] == '.':
            pos1 = col_cnt * r + c
            pos2 = col_cnt * r + (c + 1)
            u, v = (pos2, pos1) if (r + c) % 2 == 1 else (pos1, pos2)
            dinic_instance.add_edge(u, v, 1)

print(dinic_instance.max_flow(src_node, dst_node))

result_grid = deepcopy(grid_matrix)
for node_idx in range(row_cnt * col_cnt):
    for neighbor, rem_capacity, _ in dinic_instance.graph_adj[node_idx]:
        if neighbor == src_node or neighbor == dst_node:
            continue
        node_r, node_c = divmod(node_idx, col_cnt)
        neighbor_r, neighbor_c = divmod(neighbor, col_cnt)
        if (node_r + node_c) % 2 == 0 and rem_capacity == 0:
            if node_r + 1 == neighbor_r:
                result_grid[node_r][node_c] = 'v'
                result_grid[neighbor_r][neighbor_c] = '^'
            elif node_r == neighbor_r + 1:
                result_grid[node_r][node_c] = '^'
                result_grid[neighbor_r][neighbor_c] = 'v'
            elif node_c + 1 == neighbor_c:
                result_grid[node_r][node_c] = '>'
                result_grid[neighbor_r][neighbor_c] = '<'
            elif node_c == neighbor_c + 1:
                result_grid[node_r][node_c] = '<'
                result_grid[neighbor_r][neighbor_c] = '>'

for r in range(row_cnt):
    print(''.join(result_grid[r]))