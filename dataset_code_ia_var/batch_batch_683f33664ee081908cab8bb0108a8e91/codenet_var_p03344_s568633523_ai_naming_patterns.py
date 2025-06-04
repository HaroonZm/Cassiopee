class DisjointSetUnion:
    def __init__(self, element_count=0):
        self.element_count = element_count
        self.parent_or_size_array = [-1] * element_count

    def merge_elements(self, idx_a: int, idx_b: int) -> int:
        root_a = self.find_leader(idx_a)
        root_b = self.find_leader(idx_b)
        if root_a == root_b:
            return root_a
        if self.parent_or_size_array[root_a] > self.parent_or_size_array[root_b]:
            root_a, root_b = root_b, root_a
        self.parent_or_size_array[root_a] += self.parent_or_size_array[root_b]
        self.parent_or_size_array[root_b] = root_a
        return root_a

    def are_in_same_set(self, idx_a: int, idx_b: int) -> bool:
        return self.find_leader(idx_a) == self.find_leader(idx_b)

    def find_leader(self, idx: int) -> int:
        current = idx
        while self.parent_or_size_array[current] >= 0:
            current = self.parent_or_size_array[current]
        while idx != current:
            self.parent_or_size_array[idx], idx = current, self.parent_or_size_array[idx]
        return current

    def component_size(self, idx: int) -> int:
        return -self.parent_or_size_array[self.find_leader(idx)]

    def get_groups(self):
        grouped_elements = [[] for _ in range(self.element_count)]
        for element_idx in range(self.element_count):
            grouped_elements[self.find_leader(element_idx)].append(element_idx)
        return [group for group in grouped_elements if group]

total_vertices, total_edges = map(int, input().split())
vertex_data = []
for vertex_index in range(total_vertices):
    required, gain = map(int, input().split())
    adjusted_required = max(required - gain, 0)
    vertex_data.append((adjusted_required, gain))

adjacency_list = [[] for _ in range(total_vertices)]
for edge_index in range(total_edges):
    vertex_u, vertex_v = map(int, input().split())
    vertex_u -= 1
    vertex_v -= 1
    adjacency_list[vertex_u].append(vertex_v)
    adjacency_list[vertex_v].append(vertex_u)

disjoint_set = DisjointSetUnion(total_vertices)
dynamic_state = vertex_data.copy()
vertex_processed_flag = [False] * total_vertices

sorted_vertex_indices = sorted(range(total_vertices), key=lambda i: vertex_data[i][0])
for current_vertex_idx in sorted_vertex_indices:
    cur_required, cur_gain = vertex_data[current_vertex_idx]
    connected_components = {current_vertex_idx}
    for neighbor_idx in adjacency_list[current_vertex_idx]:
        if vertex_processed_flag[neighbor_idx]:
            connected_components.add(disjoint_set.find_leader(neighbor_idx))
    minimum_extra = 10 ** 18
    for component in connected_components:
        extra_val, total_gain_val = dynamic_state[component]
        adjusted_extra = extra_val + max(cur_required - (extra_val + total_gain_val), 0)
        if adjusted_extra < minimum_extra:
            minimum_extra = adjusted_extra
            minimum_component = component
    combined_extra = minimum_extra
    combined_gain = sum(dynamic_state[component][1] for component in connected_components)
    for component in connected_components:
        disjoint_set.merge_elements(current_vertex_idx, component)
    representative = disjoint_set.find_leader(current_vertex_idx)
    dynamic_state[representative] = (combined_extra, combined_gain)
    vertex_processed_flag[current_vertex_idx] = True

final_result = sum(dynamic_state[disjoint_set.find_leader(0)])
print(final_result)