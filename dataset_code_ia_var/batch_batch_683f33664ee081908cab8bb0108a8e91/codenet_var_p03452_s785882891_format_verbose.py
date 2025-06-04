import sys

def read_input():
    return sys.stdin.readline()

class WeightedUnionFind:
    def __init__(self, number_of_elements):
        self.number_of_elements = number_of_elements
        self.parent_indexes = [-1] * number_of_elements  # Negative value stores size of set
        self.distances_from_parent = [0] * number_of_elements  # Distance to parent/root for weighted union-find

    def find_root(self, element_index):
        if self.parent_indexes[element_index] < 0:
            return element_index
        root_index = self.find_root(self.parent_indexes[element_index])
        self.distances_from_parent[element_index] += self.distances_from_parent[self.parent_indexes[element_index]]
        self.parent_indexes[element_index] = root_index
        return root_index

    def get_distance_from_root(self, element_index):
        self.find_root(element_index)
        return self.distances_from_parent[element_index]

    def unite_sets_with_weight(self, first_index, second_index, relative_weight):
        updated_weight = relative_weight + self.distances_from_parent[first_index] - self.distances_from_parent[second_index]
        first_root = self.find_root(first_index)
        second_root = self.find_root(second_index)

        if first_root == second_root:
            return False
        if self.parent_indexes[first_root] > self.parent_indexes[second_root]:
            first_root, second_root = second_root, first_root
            updated_weight = -updated_weight
        self.parent_indexes[first_root] += self.parent_indexes[second_root]
        self.parent_indexes[second_root] = first_root
        self.distances_from_parent[second_root] = updated_weight
        return True

    def are_in_same_set(self, first_index, second_index):
        return self.find_root(first_index) == self.find_root(second_index)

    def get_set_size(self, element_index):
        return -self.parent_indexes[self.find_root(element_index)]

    def get_weight_difference(self, first_index, second_index):
        return self.get_distance_from_root(second_index) - self.get_distance_from_root(first_index)

def main():
    number_of_nodes, number_of_constraints = map(int, read_input().split())
    weighted_union_find = WeightedUnionFind(number_of_nodes)

    for _ in range(number_of_constraints):
        left_index, right_index, expected_difference = map(int, read_input().split())
        left_index -= 1  # Adjust for zero-based indexing
        right_index -= 1

        if weighted_union_find.are_in_same_set(left_index, right_index):
            actual_difference = weighted_union_find.get_weight_difference(left_index, right_index)
            if expected_difference != actual_difference:
                print('No')
                exit()
        else:
            weighted_union_find.unite_sets_with_weight(left_index, right_index, expected_difference)

    print('Yes')

if __name__ == "__main__":
    main()