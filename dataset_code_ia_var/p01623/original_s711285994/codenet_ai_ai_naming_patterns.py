import sys
from collections import defaultdict
from heapq import heappush as hp_push, heappop as hp_pop, heapify as hp_heapify

io_readline = sys.stdin.readline
io_write = sys.stdout.write

def algo_solve():
    constant_inf = 10**9
    var_node_count, var_edge_count = map(int, io_readline().split())
    if var_node_count == 0 and var_edge_count == 0:
        return False
    
    list_heights = [int(io_readline()) for idx_node in range(var_node_count)]
    list_edges = []
    adj_graph = [[] for idx_node in range(var_node_count)]
    for idx_edge in range(var_edge_count):
        val_a, val_b, val_cost = map(int, io_readline().split())
        list_edges.append((val_cost, val_a-1, val_b-1))
        adj_graph[val_a-1].append((val_b-1, val_cost))
        adj_graph[val_b-1].append((val_a-1, val_cost))
    list_edges.sort()
    
    dict_height_nodes = defaultdict(list)
    for idx_node in range(var_node_count):
        dict_height_nodes[list_heights[idx_node]].append(idx_node)
    
    def pufind_root(idx):
        if idx == array_parent[idx]:
            return idx
        array_parent[idx] = found_idx = pufind_root(array_parent[idx])
        return found_idx
    
    def pufind_unite(idx_x, idx_y):
        root_x = pufind_root(idx_x)
        root_y = pufind_root(idx_y)
        if root_x == root_y:
            return False
        if array_size[root_x] > array_size[root_y]:
            array_parent[root_y] = root_x
            array_size[root_x] += array_size[root_y]
        else:
            array_parent[root_x] = root_y
            array_size[root_y] += array_size[root_x]
        return True
    
    array_parent = list(range(var_node_count))
    array_size = [1] * var_node_count
    
    list_unique_heights = sorted(dict_height_nodes.keys(), reverse=True)
    available_nodes = [0] * var_node_count
    total_connected = 0
    break_height = -1
    break_index = -1
    for idx_height, current_height in enumerate(list_unique_heights):
        current_nodes = dict_height_nodes[current_height]
        for idx_node in current_nodes:
            for adj_node, _ in adj_graph[idx_node]:
                if not available_nodes[adj_node]:
                    continue
                pufind_unite(idx_node, adj_node)
            available_nodes[idx_node] = 1
            total_connected += 1
        group_root = pufind_root(current_nodes[0])
        if array_size[group_root] != total_connected:
            break_height = current_height
            break_index = idx_height
    
    if break_index == len(list_unique_heights) - 1:
        io_write("0\n")
        return True
    
    total_cost = 0
    threshold_height = list_unique_heights[break_index+1]
    array_parent = list(range(var_node_count))
    array_size = [1] * var_node_count
    for edge_cost, node_a, node_b in list_edges:
        if list_heights[node_a] >= threshold_height and list_heights[node_b] >= threshold_height:
            if pufind_unite(node_a, node_b):
                total_cost += edge_cost
    
    min_connect_cost = [constant_inf] * var_node_count
    visited = [0] * var_node_count
    for idx_node in range(var_node_count):
        if list_heights[idx_node] < threshold_height:
            continue
        visited[idx_node] = 1
        for adj_idx, edge_cost in adj_graph[idx_node]:
            if list_heights[adj_idx] < threshold_height:
                min_connect_cost[adj_idx] = min(min_connect_cost[adj_idx], edge_cost)
    
    heap_candidates = []
    for idx_node in range(var_node_count):
        if list_heights[idx_node] >= threshold_height:
            continue
        heap_candidates.append((-list_heights[idx_node], min_connect_cost[idx_node], idx_node))
    hp_heapify(heap_candidates)
    while heap_candidates:
        _, node_cost, idx_node = hp_pop(heap_candidates)
        if visited[idx_node]:
            continue
        visited[idx_node] = 1
        threshold_height = list_heights[idx_node]
        total_cost += node_cost
        for adj_idx, edge_cost in adj_graph[idx_node]:
            if not visited[adj_idx] and list_heights[adj_idx] <= threshold_height and edge_cost < min_connect_cost[adj_idx]:
                min_connect_cost[adj_idx] = edge_cost
                hp_push(heap_candidates, (-list_heights[adj_idx], edge_cost, adj_idx))
    io_write(f"{total_cost}\n")
    return True

while algo_solve():
    ...