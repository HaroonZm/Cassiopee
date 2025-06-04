class ConsistentSegmentTree:
    def __init__(self, initial_values, operation_func, identity_element=0):
        self.operation_func = operation_func
        self.identity_element = identity_element
        self.segment_size = 1 << (len(initial_values) - 1).bit_length()
        self.segment_nodes = self._initialize_segment_nodes(initial_values)

    def _initialize_segment_nodes(self, initial_values):
        segment_nodes = [self.identity_element] * (self.segment_size * 2 - 1)
        for element_index, element_value in enumerate(initial_values, self.segment_size - 1):
            segment_nodes[element_index] = element_value
        for parent_index in range(self.segment_size - 2, -1, -1):
            left_child_index = parent_index * 2 + 1
            right_child_index = parent_index * 2 + 2
            segment_nodes[parent_index] = self.operation_func(
                segment_nodes[left_child_index], segment_nodes[right_child_index]
            )
        return segment_nodes

    def assign(self, target_index, assign_value):
        node_index = target_index + self.segment_size - 1
        self.segment_nodes[node_index] = assign_value
        while node_index > 0:
            parent_index = (node_index - 1) // 2
            left_child_index = parent_index * 2 + 1
            right_child_index = parent_index * 2 + 2
            self.segment_nodes[parent_index] = self.operation_func(
                self.segment_nodes[left_child_index], self.segment_nodes[right_child_index]
            )
            node_index = parent_index

    def range_query(self, query_left, query_right):
        left_index = query_left + self.segment_size
        right_index = query_right + self.segment_size
        query_result = self.identity_element
        while left_index < right_index:
            if left_index & 1:
                query_result = self.operation_func(query_result, self.segment_nodes[left_index - 1])
                left_index += 1
            if right_index & 1:
                right_index -= 1
                query_result = self.operation_func(query_result, self.segment_nodes[right_index - 1])
            left_index >>= 1
            right_index >>= 1
        return query_result

number_of_elements = int(input())
height_sequence = tuple(map(int, input().split()))
beauty_sequence = tuple(map(int, input().split()))

maximum_sum_array = [0] * (number_of_elements + 1)

segment_structure = ConsistentSegmentTree(
    initial_values=maximum_sum_array,
    operation_func=max,
    identity_element=0
)

for height_value, beauty_value in zip(height_sequence, beauty_sequence):
    maximum_value = segment_structure.range_query(0, height_value) + beauty_value
    segment_structure.assign(height_value, maximum_value)
print(segment_structure.range_query(0, number_of_elements + 1))