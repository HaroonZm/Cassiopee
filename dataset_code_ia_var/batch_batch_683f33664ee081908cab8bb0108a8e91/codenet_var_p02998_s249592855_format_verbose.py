import sys

standard_input_reader = sys.stdin.readline

def read_single_integer():
    return int(standard_input_reader())

def read_multiple_integers():
    return map(int, standard_input_reader().split())

def read_list_of_integers():
    return list(map(int, standard_input_reader().split()))

def main():
    
    class UnionFindStructure:
        """
        parents:
            If parents[i] < 0, node i is a root, and abs(parents[i]) is the size of the group.
            Otherwise, parents[i] is the parent of i.
        find(x):
            Returns the root of group containing x with path compression.
        union(x, y):
            Unites the group of x and group of y.
        size(x):
            Returns the size of the group containing x.
        same(x, y):
            True if x and y belong to the same group.
        members(x):
            Returns list of nodes in the group containing x.
        roots():
            Returns list of root nodes (i.e., one per group).
        group_count():
            Returns the number of groups.
        all_group_members():
            Returns a dictionary mapping root to list of nodes.
        """
        def __init__(self, total_elements):
            self.total_elements = total_elements
            self.parents = [-1] * total_elements

        def find(self, node_index):
            if self.parents[node_index] < 0:
                return node_index
            else:
                self.parents[node_index] = self.find(self.parents[node_index])
                return self.parents[node_index]

        def union(self, node_x, node_y):
            root_x = self.find(node_x)
            root_y = self.find(node_y)

            if root_x == root_y:
                return

            if self.parents[root_x] > self.parents[root_y]:
                root_x, root_y = root_y, root_x

            self.parents[root_x] += self.parents[root_y]
            self.parents[root_y] = root_x

        def size(self, node_index):
            return -self.parents[self.find(node_index)]

        def same(self, node_x, node_y):
            return self.find(node_x) == self.find(node_y)

        def members(self, node_index):
            group_root = self.find(node_index)
            return [i for i in range(self.total_elements) if self.find(i) == group_root]

        def roots(self):
            return [i for i, parent_value in enumerate(self.parents) if parent_value < 0]

        def group_count(self):
            return len(self.roots())

        def all_group_members(self):
            return {root: self.members(root) for root in self.roots()}

        def __str__(self):
            string_representation = ''
            for root in self.roots():
                string_representation += '{}: {}\n'.format(root, self.members(root))
            return string_representation.strip()
    
    TOTAL_COORDINATE_VALUES = 10 ** 5

    number_of_input_points = read_single_integer()

    # XY_connection_counts[i]: number of edges incident to node i (x or y node)
    XY_connection_counts = [0] * (2 * TOTAL_COORDINATE_VALUES)

    graph_union_find = UnionFindStructure(2 * TOTAL_COORDINATE_VALUES)

    for _ in range(number_of_input_points):
        input_x_coordinate, input_y_coordinate = read_multiple_integers()
        x_node_index = input_x_coordinate - 1
        y_node_index = input_y_coordinate - 1 + TOTAL_COORDINATE_VALUES
        XY_connection_counts[x_node_index] += 1
        XY_connection_counts[y_node_index] += 1
        graph_union_find.union(x_node_index, y_node_index)

    from collections import defaultdict

    group_x_count = defaultdict(int)     # root_index -> count of x-nodes in this group
    group_y_count = defaultdict(int)     # root_index -> count of y-nodes in this group
    group_edge_count = defaultdict(int)  # root_index -> sum of incidences (edges) in this group

    for node_index in range(2 * TOTAL_COORDINATE_VALUES):
        root_index = graph_union_find.find(node_index)
        if node_index < TOTAL_COORDINATE_VALUES:
            group_x_count[root_index] += 1
        else:
            group_y_count[root_index] += 1
        group_edge_count[root_index] += XY_connection_counts[node_index]

    total_possible_pairs = 0

    for root, total_incident_edges in group_edge_count.items():
        num_x_nodes_in_group = group_x_count[root]
        num_y_nodes_in_group = group_y_count[root]
        # Each point originally forms an edge between x and y, so total_incident_edges // 2 = number of such edges
        possible_pairs_in_group = num_x_nodes_in_group * num_y_nodes_in_group - (total_incident_edges // 2)
        total_possible_pairs += possible_pairs_in_group

    print(total_possible_pairs)

main()