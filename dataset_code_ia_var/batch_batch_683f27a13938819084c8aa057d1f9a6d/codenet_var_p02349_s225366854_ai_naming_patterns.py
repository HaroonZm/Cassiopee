import sys
stdin_input = sys.stdin.readline

class BinaryIndexedTree:
    """Performs range addition and point query operations in O(logN) time.
    Methods:
    - range_add: Adds a value to a half-open range [left, right)
    - point_get: Retrieves value at a given index
    All indexes are 0-based
    """
    def __init__(self, size):
        self.size = size
        self.data = [0] * (size + 1)

    def _internal_add(self, index, value):
        while index > 0:
            self.data[index] += value
            index -= index & -index

    def point_get(self, index):
        index += 1
        result = 0
        while index <= self.size:
            result += self.data[index]
            index += index & -index
        return result

    def range_add(self, left, right, value):
        self._internal_add(right, value)
        self._internal_add(left, -value)

element_count, query_count = map(int, stdin_input().split())
query_list = [list(map(int, stdin_input().split())) for _ in range(query_count)]
bit_tree = BinaryIndexedTree(element_count)

for query_item in query_list:
    query_type = query_item[0]
    if query_type == 0:
        _, left_index, right_index, add_value = query_item
        bit_tree.range_add(left_index - 1, right_index, add_value)
    else:
        _, get_index = query_item
        print(bit_tree.point_get(get_index - 1))