class DisjointSetUnion:

    def __init__(self, total_elements):

        self.total_elements = total_elements

        self.parent_or_size = [-1] * total_elements

    def find_representative(self, element_index):

        if self.parent_or_size[element_index] < 0:

            return element_index

        else:

            self.parent_or_size[element_index] = self.find_representative(self.parent_or_size[element_index])

            return self.parent_or_size[element_index]

    def union_sets(self, first_index, second_index):

        root_first = self.find_representative(first_index)

        root_second = self.find_representative(second_index)

        if root_first == root_second:

            return

        if self.parent_or_size[root_first] > self.parent_or_size[root_second]:

            root_first, root_second = root_second, root_first

        self.parent_or_size[root_first] += self.parent_or_size[root_second]

        self.parent_or_size[root_second] = root_first

    def size_of_set(self, element_index):

        return -self.parent_or_size[self.find_representative(element_index)]

    def are_in_same_set(self, first_index, second_index):

        return self.find_representative(first_index) == self.find_representative(second_index)

    def get_set_members(self, element_index):

        representative = self.find_representative(element_index)

        return [i for i in range(self.total_elements) if self.find_representative(i) == representative]

    def get_all_roots(self):

        return [index for index, parent in enumerate(self.parent_or_size) if parent < 0]

    def count_distinct_sets(self):

        return len(self.get_all_roots())

    def all_sets_with_members(self):

        return {root: self.get_set_members(root) for root in self.get_all_roots()}

    def __str__(self):

        return '\n'.join('{}: {}'.format(root, self.get_set_members(root)) for root in self.get_all_roots())

number_of_nodes, number_of_edges = map(int, input().split())

disjoint_set_union = DisjointSetUnion(number_of_nodes)

for _ in range(number_of_edges):

    node_a, node_b = map(int, input().split())

    disjoint_set_union.union_sets(node_a - 1, node_b - 1)

minimum_edges_needed_to_connect_all_nodes = disjoint_set_union.count_distinct_sets() - 1

print(minimum_edges_needed_to_connect_all_nodes)