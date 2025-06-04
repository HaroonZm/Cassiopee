import sys
input_reader = sys.stdin.readline
from operator import itemgetter as item_getter

class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size

    def find(self, index):
        if self.parent[index] < 0:
            return index
        path = []
        current = index
        while self.parent[current] >= 0:
            path.append(current)
            current = self.parent[current]
        for node in path:
            self.parent[node] = current
        return current

    def unite(self, index_a, index_b):
        root_a = self.find(index_a)
        root_b = self.find(index_b)
        if root_a != root_b:
            if self.parent[root_a] > self.parent[root_b]:
                root_a, root_b = root_b, root_a
            self.parent[root_a] += self.parent[root_b]
            self.parent[root_b] = root_a
        return root_a

node_count = int(input_reader())
node_records = []
for node_index in range(node_count):
    coord_x, coord_y = map(int, input_reader().split())
    node_records.append((node_index, coord_x, coord_y))

_, _, y_values = map(list, zip(*node_records))

node_records.sort(key=item_getter(1))

union_find = UnionFind(node_count)

merge_stack = []
for current_index, _, current_y in node_records:
    candidate_index = current_index
    while merge_stack and y_values[merge_stack[-1]] < current_y:
        if y_values[merge_stack[-1]] < y_values[candidate_index]:
            candidate_index = merge_stack[-1]
        union_find.unite(merge_stack.pop(), current_index)
    merge_stack.append(candidate_index)

component_sizes = [-union_find.parent[union_find.find(i)] for i in range(node_count)]

print('\n'.join(map(str, component_sizes)))