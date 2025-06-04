import sys

def read_input_line():
    return sys.stdin.readline().strip()

def create_2d_list(num_rows, num_cols, initial_value):
    return [[initial_value] * num_cols for _ in range(num_rows)]

def create_3d_list(dim1, dim2, dim3, initial_value):
    return [[[initial_value] * dim3 for _ in range(dim2)] for _ in range(dim1)]

def create_4d_list(dim1, dim2, dim3, dim4, initial_value):
    return [[[[initial_value] * dim4 for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

def ceil_division(numerator, denominator=1):
    return int(-(-numerator // denominator))

def read_integer():
    return int(read_input_line())

def read_integer_map():
    return map(int, read_input_line().split())

def read_integer_list(number_of_elements=None):
    if number_of_elements is None:
        return list(read_integer_map())
    else:
        return [read_integer() for _ in range(number_of_elements)]

def print_yes_lowercase():
    print('Yes')

def print_no_lowercase():
    print('No')

def print_yes_uppercase():
    print('YES')

def print_no_uppercase():
    print('NO')

sys.setrecursionlimit(10 ** 9)
INFINITY_VALUE = 10 ** 18
MODULO_VALUE = 10 ** 9 + 7

element_count = read_integer()
element_list = read_integer_list(element_count)

position_in_sequence = [0] * element_count

for zero_based_index, sequence_value in enumerate(element_list):
    position_in_sequence[sequence_value - 1] = zero_based_index

maximum_consecutive_sorted_length = 1
current_consecutive_length = 1

for position_index in range(element_count - 1):
    if position_in_sequence[position_index] < position_in_sequence[position_index + 1]:
        current_consecutive_length += 1
    else:
        current_consecutive_length = 1

    maximum_consecutive_sorted_length = max(maximum_consecutive_sorted_length, current_consecutive_length)

minimal_operations_to_sort = element_count - maximum_consecutive_sorted_length
print(minimal_operations_to_sort)