class UnionFind:
    def __init__(self, number_of_elements):
        self.total_elements = number_of_elements
        self.parent_or_size = [-1] * number_of_elements

    def find_root(self, element_index):
        if self.parent_or_size[element_index] < 0:
            return element_index
        else:
            self.parent_or_size[element_index] = self.find_root(self.parent_or_size[element_index])
            return self.parent_or_size[element_index]

    def union_groups(self, element_index_a, element_index_b):
        root_a = self.find_root(element_index_a)
        root_b = self.find_root(element_index_b)

        if root_a == root_b:
            return

        if self.parent_or_size[root_a] > self.parent_or_size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent_or_size[root_a] += self.parent_or_size[root_b]
        self.parent_or_size[root_b] = root_a

    def group_size(self, element_index):
        root_index = self.find_root(element_index)
        return -self.parent_or_size[root_index]

    def are_in_same_group(self, element_index_a, element_index_b):
        return self.find_root(element_index_a) == self.find_root(element_index_b)

    def group_members(self, element_index):
        root_index = self.find_root(element_index)
        return [current_index for current_index in range(self.total_elements) if self.find_root(current_index) == root_index]

    def all_roots(self):
        return [current_index for current_index, parent_value in enumerate(self.parent_or_size) if parent_value < 0]

    def number_of_groups(self):
        return len(self.all_roots())

    def all_group_members(self):
        return {root_index: self.group_members(root_index) for root_index in self.all_roots()}

    def __str__(self):
        return '\n'.join(f'{root_index}: {self.group_members(root_index)}' for root_index in self.all_roots())


number_of_nodes, number_of_edges = map(int, input().split())
union_find_structure = UnionFind(number_of_nodes)

for _ in range(number_of_edges):
    node_index_a, node_index_b = map(int, input().split())
    node_index_a -= 1
    node_index_b -= 1
    union_find_structure.union_groups(node_index_a, node_index_b)

unique_root_indices = set()
for element_index in range(number_of_nodes):
    root_index = union_find_structure.find_root(element_index)
    unique_root_indices.add(root_index)

number_of_components_to_connect = len(unique_root_indices) - 1
print(number_of_components_to_connect)