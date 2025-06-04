class ConsistentRangeMaxQuery:
    def __init__(self, num_elements):
        self.tree_size = num_elements
        self.tree_data = [0] * (2 * num_elements - 1)

    def set_value(self, index, value):
        tree_index = index + self.tree_size - 1
        self.tree_data[tree_index] = value
        while tree_index > 0:
            parent_index = (tree_index - 1) // 2
            left_child = self.tree_data[parent_index * 2 + 1]
            right_child = self.tree_data[parent_index * 2 + 2]
            if left_child > right_child:
                self.tree_data[parent_index] = left_child
            else:
                self.tree_data[parent_index] = right_child
            tree_index = parent_index

    def query_max(self, query_left, query_right, node_index, seg_left, seg_right):
        if seg_right <= query_left or query_right <= seg_left:
            return 0
        elif query_left <= seg_left and seg_right <= query_right:
            return self.tree_data[node_index]
        else:
            left_max = self.query_max(query_left, query_right, node_index * 2 + 1, seg_left, (seg_left + seg_right) // 2)
            right_max = self.query_max(query_left, query_right, node_index * 2 + 2, (seg_left + seg_right) // 2, seg_right)
            if left_max > right_max:
                return left_max
            else:
                return right_max

def run_consistent_range_calc():
    from math import ceil, log2

    input_n = int(input())
    input_values = list(map(int, input().split()))
    padded_size = 2 ** ceil(log2(input_n))
    max_query_tree = ConsistentRangeMaxQuery(padded_size)
    for current_value in input_values:
        current_max = max_query_tree.query_max(0, current_value - 1, 0, 0, padded_size) + current_value
        max_query_tree.set_value(current_value - 1, current_max)
    total_sum = input_n * (input_n + 1) // 2
    result_value = total_sum - max_query_tree.query_max(0, input_n, 0, 0, padded_size)
    print(result_value)

run_consistent_range_calc()