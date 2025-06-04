class DisjointSetUnion:

    def __init__(self, total_elements):
        self.parent_or_size = [-1] * total_elements

    def find_representative(self, element_index):
        if self.parent_or_size[element_index] < 0:
            return element_index

        self.parent_or_size[element_index] = self.find_representative(self.parent_or_size[element_index])

        return self.parent_or_size[element_index]

    def unite_sets(self, first_element_index, second_element_index):
        root_first = self.find_representative(first_element_index)
        root_second = self.find_representative(second_element_index)

        if root_first == root_second:
            return

        if self.parent_or_size[root_first] > self.parent_or_size[root_second]:
            root_first, root_second = root_second, root_first

        self.parent_or_size[root_first] += self.parent_or_size[root_second]
        self.parent_or_size[root_second] = root_first

    def get_set_size(self, element_index):
        representative_index = self.find_representative(element_index)
        return -self.parent_or_size[representative_index]

def main():

    number_of_elements, number_of_connections = map(int, input().split())
    disjoint_set = DisjointSetUnion(number_of_elements)

    for _ in range(number_of_connections):
        first_node_input, second_node_input = map(int, input().split())
        disjoint_set.unite_sets(first_node_input - 1, second_node_input - 1)

    largest_connected_component_size = max(
        disjoint_set.get_set_size(element_index)
        for element_index in range(number_of_elements)
    )

    return largest_connected_component_size

print(main())