import sys
from operator import add

def read_input_line():
    return sys.stdin.readline().strip()

def create_2d_list(num_rows, num_columns, default_value):
    return [[default_value] * num_columns for _ in range(num_rows)]

def create_3d_list(num_planes, num_rows, num_columns, default_value):
    return [[[default_value] * num_columns for _ in range(num_rows)] for _ in range(num_planes)]

def create_4d_list(dim1, dim2, dim3, dim4, default_value):
    return [[[[default_value] * dim4 for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

def ceil_division(dividend, divisor=1):
    return int(-(-dividend // divisor))

def read_int():
    return int(read_input_line())

def read_ints_map():
    return map(int, read_input_line().split())

def read_ints_list(num_items=None):
    if num_items is None:
        return list(read_ints_map())
    else:
        return [read_int() for _ in range(num_items)]

def print_Yes():
    print('Yes')

def print_No():
    print('No')

def print_YES():
    print('YES')

def print_NO():
    print('NO')

sys.setrecursionlimit(10 ** 9)

INFINITY_INTEGER = 2 ** 31 - 1
MODULUS = 10 ** 9 + 7

class LazySegmentTree:
    """
    Lazy Segment Tree (Interval Update, Interval Sum Query)
    """

    def __init__(self, segment_size, merge_function, neutral_element):
        self.neutral_element = neutral_element
        self.merge_function = merge_function
        self.levels = (segment_size - 1).bit_length()
        self.tree_size = 2 ** self.levels
        self.data = [neutral_element] * (2 * self.tree_size)
        self.lazy = [None] * (2 * self.tree_size)

    def get_propagation_indices(self, left, right):
        left_index = (left + self.tree_size) >> 1
        right_index = (right + self.tree_size) >> 1
        left_count = 0 if left & 1 else (left_index & -left_index).bit_length()
        right_count = 0 if right & 1 else (right_index & -right_index).bit_length()
        for level in range(self.levels):
            if right_count <= level:
                yield right_index
            if left_index < right_index and left_count <= level:
                yield left_index
            left_index >>= 1
            right_index >>= 1

    def propagate_lazy(self, *indices):
        for index in reversed(indices):
            lazy_value = self.lazy[index - 1]
            if lazy_value is None:
                continue
            self.lazy[2 * index - 1] = self.data[2 * index - 1] = self.lazy[2 * index] = self.data[2 * index] = lazy_value >> 1
            self.lazy[index - 1] = None

    def range_update(self, update_left, update_right, update_value):
        """
        Update values in the interval [update_left, update_right) to update_value
        """
        propagation_indices = tuple(self.get_propagation_indices(update_left, update_right))
        self.propagate_lazy(*propagation_indices)
        left_ptr = self.tree_size + update_left
        right_ptr = self.tree_size + update_right
        current_value = update_value
        while left_ptr < right_ptr:
            if right_ptr & 1:
                right_ptr -= 1
                self.lazy[right_ptr - 1] = self.data[right_ptr - 1] = current_value
            if left_ptr & 1:
                self.lazy[left_ptr - 1] = self.data[left_ptr - 1] = current_value
                left_ptr += 1
            left_ptr >>= 1
            right_ptr >>= 1
            current_value <<= 1
        for index in propagation_indices:
            self.data[index - 1] = self.merge_function(self.data[2 * index - 1], self.data[2 * index])

    def range_query(self, query_left, query_right):
        """
        Get the sum in the interval [query_left, query_right)
        """
        self.propagate_lazy(*self.get_propagation_indices(query_left, query_right))
        left_ptr = self.tree_size + query_left
        right_ptr = self.tree_size + query_right
        result = self.neutral_element
        while left_ptr < right_ptr:
            if right_ptr & 1:
                right_ptr -= 1
                result = self.merge_function(result, self.data[right_ptr - 1])
            if left_ptr & 1:
                result = self.merge_function(result, self.data[left_ptr - 1])
                left_ptr += 1
            left_ptr >>= 1
            right_ptr >>= 1
        return result

number_of_elements, number_of_queries = read_ints_map()
segment_tree = LazySegmentTree(number_of_elements + 1, add, 0)

query_results = []
for query_index in range(number_of_queries):
    command_and_args = list(read_ints_map())
    command_type = command_and_args[0]
    if command_type == 0:
        update_left, update_right, update_value = command_and_args[1:]
        segment_tree.range_update(update_left, update_right + 1, update_value)
    else:
        query_left, query_right = command_and_args[1:]
        range_sum = segment_tree.range_query(query_left, query_right + 1)
        query_results.append(str(range_sum))

print('\n'.join(query_results))