number_of_positions, number_of_constraints = map(int, input().split())

left_limits = [0] * number_of_constraints
right_limits = [0] * number_of_constraints

brightness_values = list(map(int, input().split()))

for constraint_index in range(number_of_constraints):
    left_limits[constraint_index], right_limits[constraint_index] = map(int, input().split())

predecessor_indices = [0] * (number_of_positions + 1)
dp_array = [0] * (number_of_positions + 1)

for position_index in range(1, number_of_positions + 1):
    predecessor_indices[position_index] = position_index - 1

for constraint_index in range(number_of_constraints):
    right_position = right_limits[constraint_index]
    left_position = left_limits[constraint_index]
    predecessor_indices[right_position] = min(predecessor_indices[right_position], left_position - 1)

for position_index in range(number_of_positions - 1, 0, -1):
    predecessor_indices[position_index] = min(predecessor_indices[position_index], predecessor_indices[position_index + 1])

for position_index in range(1, number_of_positions + 1):
    dp_array[position_index] = max(dp_array[position_index - 1], dp_array[predecessor_indices[position_index]] + brightness_values[position_index - 1])

print(dp_array[number_of_positions])