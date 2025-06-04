import sys

if sys.version_info[0] >= 3:
    raw_input = input

input_count = int(raw_input())

for input_index in range(input_count):
    input_values = [int(input_element) for input_element in raw_input().split()]
    current_row = input_values[0] - 1
    current_column = input_values[1] - 1
    current_offset = input_values[2]
    calculation_base = 196471
    calculation_row = current_row * 195
    calculation_row_extra = (current_row // 3) * 5
    calculation_column = current_column * 20
    calculation_column_extra = current_column // 2 if current_row % 3 != 2 else 0
    final_result = calculation_base - calculation_row - calculation_row_extra - calculation_column + calculation_column_extra - current_offset
    print(final_result)