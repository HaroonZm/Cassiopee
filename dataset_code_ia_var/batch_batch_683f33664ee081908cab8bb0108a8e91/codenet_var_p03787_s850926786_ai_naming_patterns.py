class UFSystem:
    def __init__(self, node_count):
        self.parent_or_size = [-1 for _ in range(node_count)]

    def get_leader(self, node_index):
        if self.parent_or_size[node_index] < 0:
            return node_index
        self.parent_or_size[node_index] = self.get_leader(self.parent_or_size[node_index])
        return self.parent_or_size[node_index]

    def union_sets(self, node_x, node_y):
        leader_x = self.get_leader(node_x)
        leader_y = self.get_leader(node_y)
        if leader_x == leader_y:
            return
        if -self.parent_or_size[leader_x] < -self.parent_or_size[leader_y]:
            leader_x, leader_y = leader_y, leader_x
        self.parent_or_size[leader_x] += self.parent_or_size[leader_y]
        self.parent_or_size[leader_y] = leader_x

    def is_leader(self, node_index):
        return self.parent_or_size[node_index] < 0

    def are_in_same_set(self, node_x, node_y):
        return self.get_leader(node_x) == self.get_leader(node_y)

    def get_set_size(self, node_x):
        return -self.parent_or_size[self.get_leader(node_x)]

total_nodes, total_edges = map(int, input().split())
uf_structure = UFSystem(2 * total_nodes)
for _ in range(total_edges):
    edge_u, edge_v = map(int, input().split())
    edge_u -= 1
    edge_v -= 1
    uf_structure.union_sets(edge_u, total_nodes + edge_v)
    uf_structure.union_sets(total_nodes + edge_u, edge_v)

set_size_one_count = 0
set_bipartite_count = 0
set_cycle_count = 0

for node in range(total_nodes):
    if uf_structure.is_leader(node) or uf_structure.is_leader(total_nodes + node):
        if uf_structure.get_set_size(node) == 1:
            set_size_one_count += 1
        elif uf_structure.are_in_same_set(node, total_nodes + node):
            set_cycle_count += 1
        else:
            set_bipartite_count += 1

result_total = 0
result_total += set_size_one_count * total_nodes
result_total += total_nodes * set_size_one_count
result_total -= set_size_one_count * set_size_one_count
result_total += set_bipartite_count * set_bipartite_count * 2
result_total += set_bipartite_count * set_cycle_count
result_total += set_cycle_count * set_bipartite_count
result_total += set_cycle_count * set_cycle_count

print(result_total)