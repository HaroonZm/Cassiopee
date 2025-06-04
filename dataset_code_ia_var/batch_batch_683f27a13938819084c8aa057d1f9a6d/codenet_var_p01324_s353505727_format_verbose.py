class WeightedUnionFindWithWeights:
    def __init__(self, number_of_elements):
        self.number_of_elements = number_of_elements
        self.parent_indices = [-1] * number_of_elements
        self.cumulative_weights = [0] * number_of_elements

    def find_root(self, node_index):
        if self.parent_indices[node_index] < 0:
            return node_index
        else:
            root_index = self.find_root(self.parent_indices[node_index])
            self.cumulative_weights[node_index] += self.cumulative_weights[self.parent_indices[node_index]]
            self.parent_indices[node_index] = root_index
            return root_index

    def unite_sets(self, node_index_1, node_index_2, weight_difference):
        updated_weight = weight_difference + self.cumulative_weights[node_index_1] - self.cumulative_weights[node_index_2]
        root_1 = self.find_root(node_index_1)
        root_2 = self.find_root(node_index_2)
        if root_1 == root_2:
            return
        if self.parent_indices[root_1] > self.parent_indices[root_2]:
            root_1, root_2, updated_weight = root_2, root_1, -updated_weight
        self.parent_indices[root_1] += self.parent_indices[root_2]
        self.parent_indices[root_2] = root_1
        self.cumulative_weights[root_2] = updated_weight

    def get_weight_from_root(self, node_index):
        self.find_root(node_index)
        return self.cumulative_weights[node_index]

    def calculate_weight_difference(self, node_index_1, node_index_2):
        return self.get_weight_from_root(node_index_2) - self.get_weight_from_root(node_index_1)

    def are_in_same_set(self, node_index_1, node_index_2):
        return self.find_root(node_index_1) == self.find_root(node_index_2)

while True:
    number_of_constraints = int(input())
    if number_of_constraints == 0:
        exit()
    constraint_queries = []
    unique_element_names = set()
    for _ in range(number_of_constraints):
        _, left_label, _, constraint_string, right_label = input().split()
        constraint_value = int(constraint_string[3:])
        constraint_queries.append((left_label, right_label, constraint_value))
        unique_element_names.add(left_label)
        unique_element_names.add(right_label)
    element_name_to_index = {element_name: index for index, element_name in enumerate(unique_element_names)}
    weighted_union_find = WeightedUnionFindWithWeights(len(unique_element_names))
    for left_label, right_label, constraint_value in constraint_queries:
        left_index = element_name_to_index[left_label]
        right_index = element_name_to_index[right_label]
        if weighted_union_find.are_in_same_set(left_index, right_index):
            actual_difference = weighted_union_find.calculate_weight_difference(left_index, right_index)
            if constraint_value != actual_difference:
                print("No")
                break
        else:
            weighted_union_find.unite_sets(left_index, right_index, constraint_value)
    else:
        print("Yes")