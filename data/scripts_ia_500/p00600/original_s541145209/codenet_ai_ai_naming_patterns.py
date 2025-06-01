class UnionFindStructure:
    def __init__(self, total_elements):
        self.parent_table = [-1 for _ in range(total_elements)]

    def find_root(self, element_index):
        while self.parent_table[element_index] >= 0:
            element_index = self.parent_table[element_index]
        return element_index

    def union_sets(self, element_a, element_b):
        root_a = self.find_root(element_a)
        root_b = self.find_root(element_b)
        if root_a != root_b:
            if self.parent_table[root_a] >= self.parent_table[root_b]:
                self.parent_table[root_a] += self.parent_table[root_b]
                self.parent_table[root_b] = root_a
            else:
                self.parent_table[root_b] += self.parent_table[root_a]
                self.parent_table[root_a] = root_b
            return True
        return False

def encode_edge(total_nodes, node_start, node_end):
    return total_nodes * node_start + node_end

def decode_edge(total_nodes, encoded_value):
    return [(encoded_value - encoded_value % total_nodes) // total_nodes, encoded_value % total_nodes]

def kruskal_algorithm(total_nodes, edges_dictionary):
    sorted_edges = sorted(edges_dictionary.items(), key=lambda edge_item: edge_item[1])
    union_find = UnionFindStructure(total_nodes)
    selected_edges = {}
    for encoded_edge_value, cost in sorted_edges:
        node_start, node_end = decode_edge(total_nodes, encoded_edge_value)
        if union_find.union_sets(node_start, node_end):
            selected_edges[encoded_edge_value] = cost
    return selected_edges

while True:
    springs_count, districts_count = map(int, input().split())
    if springs_count == 0 and districts_count == 0:
        break

    total_nodes = 1 + districts_count
    edges = {}

    # Distances between springs and districts
    for spring_index in range(springs_count):
        distances_str = input().split()
        for district_index in range(districts_count):
            distance_value = distances_str[district_index]
            if distance_value != "0":
                edge_key = encode_edge(total_nodes, 0, 1 + district_index)
                distance_int = int(distance_value)
                if edge_key in edges:
                    edges[edge_key] = min(edges[edge_key], distance_int)
                else:
                    edges[edge_key] = distance_int

    # Distances between districts
    for dist_index in range(districts_count - 1):
        distances_str = input().split()
        for offset in range(districts_count - dist_index - 1):
            distance_value = distances_str[offset]
            if distance_value != "0":
                edge_key = encode_edge(total_nodes, 1 + dist_index, dist_index + offset + 2)
                edges[edge_key] = int(distance_value)

    mst_edges = kruskal_algorithm(total_nodes, edges)
    total_cost = sum(mst_edges.values())
    print(total_cost)