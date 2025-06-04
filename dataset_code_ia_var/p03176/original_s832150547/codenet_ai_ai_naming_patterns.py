class FenwickTreeMax:
    """1-indexed max Fenwick Tree"""

    def __init__(self, length):
        self.ftree_size = length
        self.ftree_data = [0] * (length + 1)

    def get_prefix_max(self, index):
        result_max = 0
        while index > 0:
            result_max = max(result_max, self.ftree_data[index])
            index -= index & -index
        return result_max

    def set_point_max(self, index, value):
        while index <= self.ftree_size:
            self.ftree_data[index] = max(self.ftree_data[index], value)
            index += index & -index

input_length = int(input())
heights_seq = tuple(map(int, input().split()))
values_seq = tuple(map(int, input().split()))

height_and_index_pairs = sorted([(h, idx) for idx, h in enumerate(heights_seq)])

fenwick_tree = FenwickTreeMax(input_length)
for curr_height, curr_index in height_and_index_pairs:
    prefix_max_value = fenwick_tree.get_prefix_max(curr_index)
    fenwick_tree.set_point_max(curr_index + 1, prefix_max_value + values_seq[curr_index])
print(fenwick_tree.get_prefix_max(input_length))