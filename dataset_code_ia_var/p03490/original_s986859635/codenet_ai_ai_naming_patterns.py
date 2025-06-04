input_command_sequence = input() + "T"
command_sequence_length = len(input_command_sequence)
target_x, target_y = map(int, input().split())

forward_step_count = 0
turn_count = 0
reachable_x_positions = set()
reachable_y_positions = set([0])

for command_index in range(command_sequence_length):
    if input_command_sequence[command_index] == "F":
        forward_step_count += 1
        continue

    if turn_count == 0:
        reachable_x_positions.add(forward_step_count)
    elif turn_count % 2 == 0:
        updated_x_positions = set()
        for current_x_position in reachable_x_positions:
            updated_x_positions.add(current_x_position - forward_step_count)
            updated_x_positions.add(current_x_position + forward_step_count)
        reachable_x_positions = updated_x_positions
    else:
        updated_y_positions = set()
        for current_y_position in reachable_y_positions:
            updated_y_positions.add(current_y_position - forward_step_count)
            updated_y_positions.add(current_y_position + forward_step_count)
        reachable_y_positions = updated_y_positions

    turn_count += 1
    forward_step_count = 0

if target_x in reachable_x_positions and target_y in reachable_y_positions:
    print("Yes")
else:
    print("No")