modulus = 10**9 + 7

number_of_positions, number_of_operations = map(int, input().split())

latest_left_included = -1
latest_right_included = -1

binary_string = input()

filtered_operations = []

for operation_index in range(number_of_operations):
    current_left, current_right = map(int, input().split())
    current_left -= 1
    current_right -= 1
    if latest_left_included <= current_left and current_right <= latest_right_included:
        continue
    else:
        latest_left_included = current_left
        latest_right_included = current_right
        filtered_operations.append((current_left, current_right))

number_of_filtered_operations = len(filtered_operations)

operations_covering_index = [-1] * number_of_positions
for filtered_index in range(number_of_filtered_operations):
    op_left, op_right = filtered_operations[filtered_index]
    for position in range(op_left, op_right + 1):
        operations_covering_index[position] = filtered_index

dynamic_programming_table = [[0 for column in range(number_of_positions + 1)] for row in range(number_of_positions + 1)]

for column in range(number_of_positions + 1):
    dynamic_programming_table[-1][column] = 1

for row in range(number_of_positions - 1, -1, -1):
    current_op_index = operations_covering_index[row]
    if current_op_index != -1:
        op_left, op_right = filtered_operations[current_op_index]
        total_ones_in_range = sum(int(binary_string[position]) for position in range(op_right + 1))
        total_zeros_in_range = (op_right + 1) - total_ones_in_range
        for ones_used_so_far in range(total_ones_in_range + 1):
            remaining_ones = total_ones_in_range - ones_used_so_far
            remaining_zeros = total_zeros_in_range - (row - ones_used_so_far)
            if remaining_ones == 0:
                if remaining_zeros > 0:
                    dynamic_programming_table[row][ones_used_so_far] = dynamic_programming_table[row + 1][ones_used_so_far]
            else:
                if remaining_zeros > 0:
                    dynamic_programming_table[row][ones_used_so_far] = (dynamic_programming_table[row + 1][ones_used_so_far + 1] + dynamic_programming_table[row + 1][ones_used_so_far]) % modulus
                elif remaining_zeros == 0:
                    dynamic_programming_table[row][ones_used_so_far] = dynamic_programming_table[row + 1][ones_used_so_far + 1]
    else:
        if binary_string[row] == "1":
            for used_ones in range(number_of_positions):
                dynamic_programming_table[row][used_ones] = dynamic_programming_table[row + 1][used_ones + 1]
        else:
            for used_ones in range(number_of_positions + 1):
                dynamic_programming_table[row][used_ones] = dynamic_programming_table[row + 1][used_ones]

print(dynamic_programming_table[0][0])