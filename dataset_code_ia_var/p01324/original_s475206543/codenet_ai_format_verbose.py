class WeightedUnionFind:
    __slots__ = ["parent_or_size", "relative_weight"]

    def __init__(self, number_of_elements: int) -> None:
        self.parent_or_size = [-1] * number_of_elements  # Negative value means root and its absolute value is size
        self.relative_weight = [0] * number_of_elements  # Weight difference between node and its parent

    def find_root(self, node_index: int) -> int:
        if node_index < 0:
            raise ValueError("Node index cannot be negative.")

        if self.parent_or_size[node_index] < 0:
            return node_index
        else:
            root_index = self.find_root(self.parent_or_size[node_index])
            self.relative_weight[node_index] += self.relative_weight[self.parent_or_size[node_index]]
            self.parent_or_size[node_index] = root_index
            return root_index

    def unite_with_weight(self, node_index_a: int, node_index_b: int, weight_difference_from_a_to_b: int) -> None:
        if node_index_a < 0 or node_index_b < 0:
            raise ValueError("Node indices must be non-negative.")

        root_index_a = self.find_root(node_index_a)
        root_index_b = self.find_root(node_index_b)

        computed_weight_difference = weight_difference_from_a_to_b + self.relative_weight[node_index_a] - self.relative_weight[node_index_b]

        if root_index_a == root_index_b:
            if self.relative_weight[node_index_a] + weight_difference_from_a_to_b == self.relative_weight[node_index_b]:
                return  # Already consistent, do nothing
            raise ValueError("Inconsistency detected during unite_with_weight operation.")

        if self.parent_or_size[root_index_a] > self.parent_or_size[root_index_b]:
            root_index_a, root_index_b = root_index_b, root_index_a
            computed_weight_difference = -computed_weight_difference

        self.parent_or_size[root_index_a] += self.parent_or_size[root_index_b]
        self.parent_or_size[root_index_b] = root_index_a
        self.relative_weight[root_index_b] = computed_weight_difference

    def get_weight_difference(self, node_index_x: int, node_index_y: int) -> int:
        root_x = self.find_root(node_index_x)
        root_y = self.find_root(node_index_y)
        if root_x != root_y:
            return None
        return self.relative_weight[node_index_y] - self.relative_weight[node_index_x]

while True:
    number_of_equations = int(input())
    if not number_of_equations:
        break

    disjoint_set_structure = WeightedUnionFind(number_of_equations * 2)
    variable_name_to_index = dict()
    list_of_constraints = [input().split() for _ in range(number_of_equations)]

    try:
        for _, name_a, _, equation_value, name_b in list_of_constraints:
            numeric_difference = int(equation_value[3:])

            if name_a not in variable_name_to_index:
                variable_name_to_index[name_a] = len(variable_name_to_index)
            if name_b not in variable_name_to_index:
                variable_name_to_index[name_b] = len(variable_name_to_index)

            index_a = variable_name_to_index[name_a]
            index_b = variable_name_to_index[name_b]

            disjoint_set_structure.unite_with_weight(index_a, index_b, numeric_difference)

        print("Yes")
    except ValueError:
        print("No")