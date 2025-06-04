import sys

def read_input_line():
    return sys.stdin.readline().strip()

def create_2d_list(num_rows, num_cols, initial_value):
    return [[initial_value] * num_cols for _ in range(num_rows)]

def create_3d_list(dim1, dim2, dim3, initial_value):
    return [[[initial_value] * dim3 for _ in range(dim2)] for _ in range(dim1)]

def create_4d_list(dim1, dim2, dim3, dim4, initial_value):
    return [[[[initial_value] * dim4 for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

def integer_ceiling(dividend, divisor=1):
    return int(-(-dividend // divisor))

def read_integer():
    return int(read_input_line())

def read_int_map():
    return map(int, read_input_line().split())

def read_integer_list(length=None):
    if length is None:
        return list(read_int_map())
    else:
        return [read_integer() for _ in range(length)]

def print_yes_lowercase():
    print('Yes')

def print_no_lowercase():
    print('No')

def print_yes_uppercase():
    print('YES')

def print_no_uppercase():
    print('NO')

sys.setrecursionlimit(10 ** 9)

LARGE_NUMBER_INFINITY = 10 ** 18
MODULO_DIVISOR = 10 ** 9 + 7

input_string = read_input_line()
input_string_length = len(input_string)

# dp_table[index][abc_state]: number of ways to select first (abc_state) chars of "ABC" up to index-th character 
number_of_characters = input_string_length
number_of_abc_states = 4

dp_table = create_2d_list(number_of_characters + 1, number_of_abc_states, 0)
dp_table[0][0] = 1

for current_index in range(number_of_characters):
    current_character = input_string[current_index]
    for abc_progress in range(number_of_abc_states):
        # Option 1: Do not select the current character
        if current_character == '?':
            # '?' can transition to three different types
            dp_table[current_index + 1][abc_progress] += dp_table[current_index][abc_progress] * 3
            dp_table[current_index + 1][abc_progress] %= MODULO_DIVISOR
        else:
            dp_table[current_index + 1][abc_progress] += dp_table[current_index][abc_progress]
            dp_table[current_index + 1][abc_progress] %= MODULO_DIVISOR
        
        # Option 2: Select the current character if valid for the next letter in "ABC"
        if abc_progress < 3:
            is_valid_selection = (
                current_character == '?' or
                (current_character == 'A' and abc_progress == 0) or
                (current_character == 'B' and abc_progress == 1) or
                (current_character == 'C' and abc_progress == 2)
            )
            if is_valid_selection:
                dp_table[current_index + 1][abc_progress + 1] += dp_table[current_index][abc_progress]
                dp_table[current_index + 1][abc_progress + 1] %= MODULO_DIVISOR

# Output: number of ways to select "A", "B", "C" in order, possibly using '?'
print(dp_table[number_of_characters][3])