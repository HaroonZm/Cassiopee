class WeightedPotentialUnionFind:
    def __init__(self, total_elements):
        self.parent_or_size = [-1 for element_index in range(total_elements)]  # Negative value: group size, non-negative: parent index
        self.relative_potential_to_parent = [0 for element_index in range(total_elements)]  # Potential relative to direct parent

    def find_root(self, node_index):
        if self.parent_or_size[node_index] < 0:
            return node_index
        else:
            root_index = self.find_root(self.parent_or_size[node_index])
            self.relative_potential_to_parent[node_index] += self.relative_potential_to_parent[self.parent_or_size[node_index]]
            self.parent_or_size[node_index] = root_index
            return root_index

    def union_with_potential(self, node_index_a, node_index_b, potential_difference_ab):
        adjusted_potential_difference = (
            self.relative_potential_to_parent[node_index_a] +
            potential_difference_ab -
            self.relative_potential_to_parent[node_index_b]
        )

        root_a = self.find_root(node_index_a)
        root_b = self.find_root(node_index_b)

        if root_a == root_b:
            return False

        if self.parent_or_size[root_a] > self.parent_or_size[root_b]:
            root_a, root_b = root_b, root_a
            adjusted_potential_difference = -adjusted_potential_difference

        self.parent_or_size[root_a] += self.parent_or_size[root_b]
        self.parent_or_size[root_b] = root_a
        self.relative_potential_to_parent[root_b] = adjusted_potential_difference

        return True

    def are_in_same_group(self, node_index_a, node_index_b):
        return self.find_root(node_index_a) == self.find_root(node_index_b)

    def compute_potential_difference(self, node_index_a, node_index_b):
        if self.find_root(node_index_a) == self.find_root(node_index_b):
            return self.relative_potential_to_parent[node_index_b] - self.relative_potential_to_parent[node_index_a]
        else:
            return None

    def group_size(self, node_index):
        return -self.parent_or_size[self.find_root(node_index)]

number_of_nodes, number_of_queries = map(int, input().split())
union_find_structure = WeightedPotentialUnionFind(number_of_nodes)
is_constraints_possible = True

for query_index in range(number_of_queries):
    left_index, right_index, specified_difference = map(int, input().split())
    left_index -= 1
    right_index -= 1

    if union_find_structure.are_in_same_group(left_index, right_index):
        is_constraints_possible = (specified_difference == union_find_structure.compute_potential_difference(left_index, right_index))
    else:
        union_find_structure.union_with_potential(left_index, right_index, specified_difference)

    if not is_constraints_possible:
        break

if not is_constraints_possible:
    print('No')
else:
    print('Yes')