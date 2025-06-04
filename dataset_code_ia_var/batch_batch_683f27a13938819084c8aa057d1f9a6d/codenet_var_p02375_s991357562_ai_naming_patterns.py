class ConsistentTree:
    def __init__(self, node_count, edge_list):
        self.node_count = node_count
        self.adjacency_list = [[] for _ in range(node_count)]
        for node_a, node_b in edge_list:
            node_a_idx = node_a - 1
            node_b_idx = node_b - 1
            self.adjacency_list[node_a_idx].append(node_b_idx)
            self.adjacency_list[node_b_idx].append(node_a_idx)

    def initialize_root(self, root_index):
        self.root_index = root_index
        self.parent_list = [None] * self.node_count
        self.parent_list[root_index] = -1
        self.depth_list = [None] * self.node_count
        self.depth_list[root_index] = 0
        self.node_order = []
        self.node_order.append(root_index)
        self.subtree_size = [1] * self.node_count
        traversal_stack = [root_index]
        while traversal_stack:
            current_node = traversal_stack.pop()
            for neighbor in self.adjacency_list[current_node]:
                if self.parent_list[neighbor] is None:
                    self.parent_list[neighbor] = current_node
                    self.depth_list[neighbor] = self.depth_list[current_node] + 1
                    self.node_order.append(neighbor)
                    traversal_stack.append(neighbor)
        for current_node in reversed(self.node_order):
            for neighbor in self.adjacency_list[current_node]:
                if self.parent_list[current_node] == neighbor:
                    continue
                self.subtree_size[current_node] += self.subtree_size[neighbor]

    def decompose_heavy_light(self):
        self.node_pos_in_order = [None] * self.node_count
        self.chain_head = [None] * self.node_count
        self.chain_head[self.root_index] = self.root_index
        self.heavy_child = [None] * self.node_count
        decompose_stack = [self.root_index]
        order_label = 0
        while decompose_stack:
            current_node = decompose_stack.pop()
            self.node_pos_in_order[current_node] = order_label
            order_label += 1
            largest_subtree_size = 0
            for neighbor in self.adjacency_list[current_node]:
                if self.parent_list[current_node] == neighbor:
                    continue
                if largest_subtree_size < self.subtree_size[neighbor]:
                    largest_subtree_size = self.subtree_size[neighbor]
                    self.heavy_child[current_node] = neighbor
            for neighbor in self.adjacency_list[current_node]:
                if self.parent_list[current_node] == neighbor or self.heavy_child[current_node] == neighbor:
                    continue
                self.chain_head[neighbor] = neighbor
                decompose_stack.append(neighbor)
            if self.heavy_child[current_node] is not None:
                self.chain_head[self.heavy_child[current_node]] = self.chain_head[current_node]
                decompose_stack.append(self.heavy_child[current_node])

    def get_hld_ranges(self, u_idx, v_idx, include_edge=False):
        result_ranges = []
        while True:
            if self.node_pos_in_order[u_idx] > self.node_pos_in_order[v_idx]:
                u_idx, v_idx = v_idx, u_idx
            if self.chain_head[u_idx] != self.chain_head[v_idx]:
                result_ranges.append((self.node_pos_in_order[self.chain_head[v_idx]], self.node_pos_in_order[v_idx] + 1))
                v_idx = self.parent_list[self.chain_head[v_idx]]
            else:
                result_ranges.append((self.node_pos_in_order[u_idx] + include_edge, self.node_pos_in_order[v_idx] + 1))
                return result_ranges

    def get_subtree_hld_range(self, node_idx):
        return self.node_pos_in_order[node_idx], self.node_pos_in_order[node_idx] + self.subtree_size[node_idx]

    def get_hld_lca(self, node_u, node_v):
        while True:
            if self.node_pos_in_order[node_u] > self.node_pos_in_order[node_v]:
                node_u, node_v = node_v, node_u
            if self.chain_head[node_u] != self.chain_head[node_v]:
                node_v = self.parent_list[self.chain_head[node_v]]
            else:
                return node_u

class ConsistentBinaryIndexedTree:
    def __init__(self, length):
        self.length = length
        self.data = [0] * (length + 1)

    def prefix_sum(self, index):
        result = 0
        while index:
            result += self.data[index]
            index -= index & -index
        return result

    def add_value(self, index, value):
        while index <= self.length:
            self.data[index] += value
            index += index & -index

    def lower_bound(self, value):
        if value <= 0:
            return 0
        result = 0
        bit = 1 << (self.length.bit_length() - 1)
        while bit:
            if result + bit <= self.length and self.data[result + bit] < value:
                value -= self.data[result + bit]
                result += bit
            bit >>= 1
        return result + 1

class ConsistentRangeAddRangeSum:
    def __init__(self, length):
        self.primary_bit = ConsistentBinaryIndexedTree(length)
        self.auxiliary_bit = ConsistentBinaryIndexedTree(length)

    def add_range(self, left, right, value):
        self.primary_bit.add_value(left, -value * (left - 1))
        self.primary_bit.add_value(right, value * (right - 1))
        self.auxiliary_bit.add_value(left, value)
        self.auxiliary_bit.add_value(right, -value)

    def range_sum(self, left, right):
        total_sum_r = self.auxiliary_bit.prefix_sum(right - 1) * (right - 1) + self.primary_bit.prefix_sum(right - 1)
        total_sum_l = self.auxiliary_bit.prefix_sum(left - 1) * (left - 1) + self.primary_bit.prefix_sum(left - 1)
        return total_sum_r - total_sum_l

import sys
input_reader = sys.stdin.readline

from operator import add as op_add

node_total = int(input_reader())
edge_pairs = []

for node_index in range(node_total):
    split_input = list(map(int, input_reader().split()))
    conn_count = split_input[0]
    connections = split_input[1:]
    for conn_index in range(conn_count):
        edge_pairs.append((node_index + 1, connections[conn_index] + 1))

tree_ref = ConsistentTree(node_total, edge_pairs)
tree_ref.initialize_root(0)
tree_ref.decompose_heavy_light()

range_adder_summer = ConsistentRangeAddRangeSum(node_total)

output_result_list = []

query_total = int(input_reader())

for _ in range(query_total):
    query_split = list(map(int, input_reader().split()))
    query_type = query_split[0]
    query_params = query_split[1:]
    if query_type == 0:
        vertex, weight = query_params
        for left_pos, right_pos in tree_ref.get_hld_ranges(0, vertex, include_edge=True):
            range_adder_summer.add_range(left_pos, right_pos, weight)
    else:
        sum_result = 0
        u_value = query_params[0]
        for left_pos, right_pos in tree_ref.get_hld_ranges(0, u_value, include_edge=True):
            sum_result += range_adder_summer.range_sum(left_pos, right_pos)
        output_result_list.append(sum_result)

print('\n'.join(map(str, output_result_list)))