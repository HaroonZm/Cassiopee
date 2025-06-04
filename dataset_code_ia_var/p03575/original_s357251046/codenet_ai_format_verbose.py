import sys

sys.setrecursionlimit(10 ** 9)

def convert_to_zero_based_index(number_as_string):
    return int(number_as_string) - 1

def read_single_integer():
    return int(input())

def read_multiple_integers():
    return map(int, input().split())

def read_multiple_integers_zero_based():
    return map(convert_to_zero_based_index, input().split())

def read_integer_list():
    return list(map(int, input().split()))

def read_integer_list_zero_based():
    return list(map(convert_to_zero_based_index, input().split()))

def read_list_of_integer_lists(total_rows):
    return [read_integer_list() for _ in range(total_rows)]

def read_list_of_strings():
    return input().split()

def read_character_list_from_string():
    return list(input())

def read_list_of_character_lists(total_rows):
    return [read_character_list_from_string() for _ in range(total_rows)]

def print_list_elements(elements_list, separator=' '):
    print(separator.join(list(map(str, elements_list))))

INFINITY = float('inf')

class UnionFindDisjointSet:
    def __init__(self, total_elements):
        self.total_elements = total_elements
        self.parent_node_or_size = [-1] * total_elements

    def find_representative(self, element):
        if self.parent_node_or_size[element] < 0:
            return element
        else:
            self.parent_node_or_size[element] = self.find_representative(self.parent_node_or_size[element])
            return self.parent_node_or_size[element]

    def unite_sets(self, element_x, element_y):
        root_of_x = self.find_representative(element_x)
        root_of_y = self.find_representative(element_y)

        if root_of_x == root_of_y:
            return

        if self.parent_node_or_size[root_of_x] > self.parent_node_or_size[root_of_y]:
            root_of_x, root_of_y = root_of_y, root_of_x

        self.parent_node_or_size[root_of_x] += self.parent_node_or_size[root_of_y]
        self.parent_node_or_size[root_of_y] = root_of_x

    def size_of_set_containing(self, element):
        return -self.parent_node_or_size[self.find_representative(element)]

    def are_in_same_set(self, element_x, element_y):
        return self.find_representative(element_x) == self.find_representative(element_y)

    def members_of_set(self, element):
        root_element = self.find_representative(element)
        return [i for i in range(self.total_elements) if self.find_representative(i) == root_element]

    def all_root_elements(self):
        return [i for i, val in enumerate(self.parent_node_or_size) if val < 0]

    def count_total_groups(self):
        return len(self.all_root_elements())

    def all_groups_members(self):
        return {root: self.members_of_set(root) for root in self.all_root_elements()}

    def sizes_of_all_groups(self):
        return [self.size_of_set_containing(root) for root in self.all_root_elements()]

    def __str__(self):
        return '\n'.join('{}: {}'.format(root, self.members_of_set(root)) for root in self.all_root_elements())

def solve_problem():
    number_of_nodes, number_of_edges = read_multiple_integers()
    edge_list = []
    for edge_index in range(number_of_edges):
        node_from, node_to = read_multiple_integers_zero_based()
        edge_list.append((node_from, node_to))

    count_of_critical_edges = 0

    for edge_being_removed in edge_list:
        union_find = UnionFindDisjointSet(number_of_nodes)

        for edge in edge_list:
            if edge == edge_being_removed:
                continue
            node1, node2 = edge
            union_find.unite_sets(node1, node2)

        if union_find.count_total_groups() > 1:
            count_of_critical_edges += 1

    print(count_of_critical_edges)

if __name__ == '__main__':
    solve_problem()