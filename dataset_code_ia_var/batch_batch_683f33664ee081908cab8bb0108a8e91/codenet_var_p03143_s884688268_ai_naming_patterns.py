import sys

class DisjointSetManager:
    def __init__(self, node_count):
        self.parent_table = [-1] * node_count

    def _find_root(self, node_index):
        if self.parent_table[node_index] < 0:
            return node_index
        else:
            self.parent_table[node_index] = self._find_root(self.parent_table[node_index])
            return self.parent_table[node_index]

    def are_in_same_set(self, node_x, node_y):
        return self._find_root(node_x) == self._find_root(node_y)

    def unite_sets(self, node_x, node_y):
        root_x = self._find_root(node_x)
        root_y = self._find_root(node_y)
        if root_x == root_y:
            return
        size_x = self.parent_table[root_x]
        size_y = self.parent_table[root_y]
        if size_x <= size_y:
            self.parent_table[root_y] = root_x
            if size_x == size_y:
                self.parent_table[root_x] -= 1
        else:
            self.parent_table[root_x] = root_y

def depth_first_search(start_index, max_year):
    stack_nodes = [start_index]
    node_visited[start_index] = True
    while stack_nodes:
        current_node = stack_nodes.pop()
        for edge_year, neighbor_node, edge_index in edge_connections[current_node]:
            if edge_year > max_year:
                continue
            edge_status[edge_index] = 2
            if node_visited[neighbor_node]:
                continue
            node_visited[neighbor_node] = True
            stack_nodes.append(neighbor_node)

node_count, edge_count = map(int, input().split())
node_values = list(map(int, input().split()))
edge_connections = [set() for _ in range(node_count)]
all_edges = []
for edge_index, input_line in enumerate(sys.stdin.readlines()):
    node_a, node_b, edge_year = map(int, input_line.split())
    node_a -= 1
    node_b -= 1
    edge_connections[node_a].add((edge_year, node_b, edge_index))
    edge_connections[node_b].add((edge_year, node_a, edge_index))
    all_edges.append((edge_year, node_a, node_b, edge_index))

all_edges_sorted = sorted(all_edges)

disjoint_set = DisjointSetManager(node_count)
accumulated_values = node_values[:]
edge_status = [0] * edge_count  # 0: unknown, 1: valid, 2: fixed

for edge_year, node_a, node_b, edge_index in all_edges_sorted:
    if disjoint_set.are_in_same_set(node_a, node_b):
        root_node = disjoint_set._find_root(node_a)
    else:
        root_a = disjoint_set._find_root(node_a)
        root_b = disjoint_set._find_root(node_b)
        disjoint_set.unite_sets(node_a, node_b)
        root_node = disjoint_set._find_root(node_a)
        accumulated_values[root_node] += accumulated_values[root_b if root_node == root_a else root_a]
    if accumulated_values[root_node] >= edge_year:
        edge_status[edge_index] = 1

ambiguous_edge_count = 0
node_visited = [False] * node_count
for edge_year, node_a, node_b, edge_index in reversed(all_edges_sorted):
    if edge_status[edge_index] == 2:
        continue
    if edge_status[edge_index] == 0:
        ambiguous_edge_count += 1
        continue
    depth_first_search(node_a, edge_year)

print(ambiguous_edge_count)