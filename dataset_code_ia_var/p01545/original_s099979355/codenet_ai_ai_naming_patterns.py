import math
import sys
if sys.version[0] == '2':
    range, input = xrange, raw_input

class FenwickTreeSystematic:
    def __init__(self, initial_list, combine_func, neutral_element):
        self.size = len(initial_list)
        self.tree = initial_list[:]
        self.combine_func = combine_func
        self.neutral_element = neutral_element
        for idx_padding in range(self.size, 1 << int(math.ceil(math.log(self.size, 2)))):
            self.tree.append(self.neutral_element)
        for idx_build in range(self.size - 1):
            target_idx = idx_build | (idx_build + 1)
            self.tree[target_idx] = self.combine_func(self.tree[target_idx], self.tree[idx_build])

    def point_update(self, update_idx, update_value):
        while update_idx < self.size:
            self.tree[update_idx] = self.combine_func(self.tree[update_idx], update_value)
            update_idx |= update_idx + 1

    def prefix_query(self, query_idx):
        aggregate = self.neutral_element
        while query_idx >= 0:
            aggregate = self.combine_func(aggregate, self.tree[query_idx])
            query_idx = (query_idx & (query_idx + 1)) - 1
        return aggregate

sequence_length = int(input())
input_sequence = [int(element) for element in input().split()]
dp_tree = FenwickTreeSystematic([0] * sequence_length, lambda left, right: max(left, right), 0)
sorted_pairs = sorted((element_value, element_index) for element_index, element_value in enumerate(input_sequence))
for value_element, index_element in sorted_pairs:
    current_max = dp_tree.prefix_query(index_element)
    dp_tree.point_update(index_element, current_max + value_element)
result = sequence_length * (sequence_length + 1) // 2 - dp_tree.prefix_query(sequence_length - 1)
print(result)