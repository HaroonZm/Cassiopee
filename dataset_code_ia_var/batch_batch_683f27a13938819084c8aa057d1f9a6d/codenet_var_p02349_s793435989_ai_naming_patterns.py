class ConsistentSegmentTree:
    _size = 1
    _data = []
    def __init__(self, size_value):
        while self._size < size_value:
            self._size <<= 1
        self._data = [0 for _ in range(self._size * 2)]

    def range_add(self, left_index, right_index, add_value):
        left_index += self._size
        right_index += self._size
        while left_index < right_index:
            if left_index & 1:
                self._data[left_index] += add_value
                left_index += 1
            if right_index & 1:
                self._data[right_index - 1] += add_value
                right_index -= 1
            left_index >>= 1
            right_index >>= 1

    def point_query(self, position_index):
        position_index += self._size
        result_value = self._data[position_index]
        while position_index > 1:
            position_index >>= 1
            result_value += self._data[position_index]
        return result_value

input_n, input_q = map(int, input().split())
consistent_tree = ConsistentSegmentTree(input_n)

for _ in range(input_q):
    input_query = [int(token) for token in input().split()]
    if len(input_query) == 4:
        _, query_left, query_right, query_add = input_query
        query_left -= 1
        query_right -= 1
        consistent_tree.range_add(query_left, query_right + 1, query_add)
    if len(input_query) == 2:
        _, query_index = input_query
        query_index -= 1
        print(consistent_tree.point_query(query_index))