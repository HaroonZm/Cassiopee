pattern_values = [
    [1, 2, 6, 7, 15, 16, 28, 29, 45],
    [3, 5, 8, 14, 17, 27, 30, 44],
    [4, 9, 13, 18, 26, 31, 43],
    [10, 12, 19, 25, 32, 42],
    [11, 20, 24, 33, 41],
    [21, 23, 34, 40],
    [22, 35, 39],
    [36, 38],
    [37]
]

def format_cell(cell_value):
    str_value = str(cell_value)
    if len(str_value) == 1:
        return "  " + str_value
    return " " + str_value

case_counter = 0
while True:
    input_size = int(raw_input())
    if input_size == 0:
        break
    case_counter += 1
    matrix = [[0 for _ in range(input_size)] for _ in range(input_size)]
    for row_idx in range(input_size):
        for col_idx in range(input_size):
            if row_idx + col_idx < input_size:
                matrix[row_idx][col_idx] = pattern_values[row_idx][col_idx]
    for row_idx in range(input_size):
        for col_idx in range(input_size):
            if row_idx + col_idx >= input_size:
                matrix[row_idx][col_idx] = (input_size * input_size + 1 
                                            - matrix[input_size - 1 - row_idx][input_size - 1 - col_idx])
    print "Case " + str(case_counter) + ":"
    for row in matrix:
        row_string = ""
        for val in row:
            row_string += format_cell(val)
        print row_string