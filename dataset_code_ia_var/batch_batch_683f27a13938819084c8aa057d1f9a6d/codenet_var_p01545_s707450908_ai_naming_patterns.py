import math
import sys
if sys.version[0] == '2':
    range_, input_ = xrange, raw_input
else:
    range_, input_ = range, input

class FenwickTreeCoherent:
    def __init__(self, seq_initial, func_combine, val_default):
        self.size_tree = len(seq_initial)
        self.tree_data = seq_initial[:]
        self.func_combine = func_combine
        self.val_default = val_default
        max_size = 1 << int(math.ceil(math.log(self.size_tree, 2)))
        for _ in range(self.size_tree, max_size):
            self.tree_data.append(self.val_default)
        for idx in range(self.size_tree - 1):
            parent_idx = idx | (idx + 1)
            self.tree_data[parent_idx] = self.func_combine(self.tree_data[parent_idx], self.tree_data[idx])

    def update_tree(self, idx_update, val_update):
        while idx_update < self.size_tree:
            self.tree_data[idx_update] = self.func_combine(self.tree_data[idx_update], val_update)
            idx_update |= idx_update + 1

    def prefix_query(self, idx_query):
        res_query = 0
        idx_iter = idx_query
        while idx_iter >= 0:
            res_query = self.func_combine(res_query, self.tree_data[idx_iter])
            idx_iter = (idx_iter & (idx_iter + 1)) - 1
        return res_query

size_seq = int(input_())
values_seq = [int(val) for val in input_().split()]
fenwick_dp = FenwickTreeCoherent([0] * size_seq, lambda a, b: max(a, b), 0)
for val_element, idx_element in sorted((val, idx) for idx, val in enumerate(values_seq)):
    curr_max = fenwick_dp.prefix_query(idx_element)
    fenwick_dp.update_tree(idx_element, curr_max + val_element)
result_final = size_seq * (size_seq + 1) // 2 - fenwick_dp.prefix_query(size_seq - 1)
print(result_final)