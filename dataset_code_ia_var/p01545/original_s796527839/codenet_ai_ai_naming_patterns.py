class SegmentTreeMax:
    DEFAULT_VALUE = 0

    def __init__(self, size_origin):
        self.size_origin = size_origin
        self.size_internal = 1
        while self.size_internal < size_origin:
            self.size_internal *= 2
        self.tree_data = [self.DEFAULT_VALUE] * (2 * self.size_internal - 1)

    def set_value(self, index, value):
        pos = index + self.size_internal - 1
        self.tree_data[pos] = value
        while pos > 0:
            pos = (pos - 1) // 2
            left_child = self.tree_data[pos * 2 + 1]
            right_child = self.tree_data[pos * 2 + 2]
            self.tree_data[pos] = max(left_child, right_child)

    def range_query(self, query_left, query_right, node_index, seg_left, seg_right):
        if seg_right <= query_left or query_right <= seg_left:
            return self.DEFAULT_VALUE
        if query_left <= seg_left and seg_right <= query_right:
            return self.tree_data[node_index]
        left_result = self.range_query(query_left, query_right, node_index * 2 + 1, seg_left, (seg_left + seg_right) // 2)
        right_result = self.range_query(query_left, query_right, node_index * 2 + 2, (seg_left + seg_right) // 2, seg_right)
        return max(left_result, right_result)

    def get_max(self, range_left, range_right):
        return self.range_query(range_left, range_right, 0, 0, self.size_internal)

input_n = int(input())
input_values = list(map(int, input().split()))
segment_tree = SegmentTreeMax(input_n + 1)
for current_value in input_values:
    current_max = segment_tree.get_max(1, current_value)
    segment_tree.set_value(current_value, current_value + current_max)
result = sum(input_values) - segment_tree.get_max(1, input_n + 1)
print(result)