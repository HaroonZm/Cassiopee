class DisjointSet:
    def __init__(self, node_count):
        self.node_count = node_count
        self.parent_array = [-1] * node_count

    def root_of(self, node_id):
        search_stack = []
        current_node = node_id
        while self.parent_array[current_node] >= 0:
            search_stack.append(current_node)
            current_node = self.parent_array[current_node]
        for traversed_node in search_stack:
            self.parent_array[traversed_node] = current_node
        return current_node

    def merge_groups(self, node_u, node_v):
        root_u = self.root_of(node_u)
        root_v = self.root_of(node_v)
        if root_u == root_v:
            return
        if self.parent_array[root_u] > self.parent_array[root_v]:
            root_u, root_v = root_v, root_u
        self.parent_array[root_u] += self.parent_array[root_v]
        self.parent_array[root_v] = root_u

    def group_size(self, node_id):
        return -self.parent_array[self.root_of(node_id)]

from sys import stdin
input_reader = stdin.buffer.readline

def process_input():
    item_count = int(input_reader())
    range_list = [0] * item_count
    for idx in range(item_count):
        start_idx, end_idx = map(int, input_reader().split())
        range_list[start_idx - 1] = (end_idx - 1, idx)

    dsu = DisjointSet(item_count)
    root_stack = []

    for end_value, item_idx in range_list:
        if len(root_stack) == 0 or root_stack[-1][0] > end_value:
            root_stack.append((end_value, item_idx))
        else:
            last_end_value = root_stack[-1][0]
            while root_stack and root_stack[-1][0] < end_value:
                popped_end_value, popped_idx = root_stack.pop()
                dsu.merge_groups(item_idx, popped_idx)
            root_stack.append((last_end_value, item_idx))

    for idx in range(item_count):
        print(dsu.group_size(idx))

process_input()