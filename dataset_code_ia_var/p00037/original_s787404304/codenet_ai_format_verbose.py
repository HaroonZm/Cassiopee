def is_wall_between_coordinates(
    start_x, start_y, end_x, end_y
):
    if (
        start_x < 0 or start_x > 4
        or start_y < 0 or start_y > 4
        or end_x < 0 or end_x > 4
        or end_y < 0 or end_y > 4
    ):
        return False

    elif start_x == end_x:
        if start_y > end_y:
            start_y, end_y = end_y, start_y

        if end_y - start_y != 1:
            return False

        wall_character = maze_wall_representation[start_y * 2 + 1][start_x]
        return wall_character == "1"

    elif start_y == end_y:
        if start_x > end_x:
            start_x, end_x = end_x, start_x

        if end_x - start_x != 1:
            return False

        wall_character = maze_wall_representation[start_y * 2][start_x]
        return wall_character == "1"

    else:
        return False


def determine_next_move(
    current_x, current_y
):
    previous_move_index = movement_history[-1]

    if previous_move_index == 3:
        previous_move_index = -1

    if previous_move_index < -1:
        previous_move_index += 4

    right_turn_direction_index = previous_move_index + 1
    right_turn_dx = movement_directions[right_turn_direction_index][1]
    right_turn_dy = movement_directions[right_turn_direction_index][2]
    right_turn_new_x = current_x + right_turn_dx
    right_turn_new_y = current_y + right_turn_dy

    if is_wall_between_coordinates(
        current_x, current_y,
        right_turn_new_x, right_turn_new_y
    ):
        return (
            right_turn_direction_index,
            right_turn_new_x,
            right_turn_new_y
        )

    forward_direction_index = previous_move_index
    forward_dx = movement_directions[forward_direction_index][1]
    forward_dy = movement_directions[forward_direction_index][2]
    forward_new_x = current_x + forward_dx
    forward_new_y = current_y + forward_dy

    if is_wall_between_coordinates(
        current_x, current_y,
        forward_new_x, forward_new_y
    ):
        return (
            forward_direction_index,
            forward_new_x,
            forward_new_y
        )

    left_turn_direction_index = previous_move_index - 1
    left_turn_dx = movement_directions[left_turn_direction_index][1]
    left_turn_dy = movement_directions[left_turn_direction_index][2]
    left_turn_new_x = current_x + left_turn_dx
    left_turn_new_y = current_y + left_turn_dy

    if is_wall_between_coordinates(
        current_x, current_y,
        left_turn_new_x, left_turn_new_y
    ):
        return (
            left_turn_direction_index,
            left_turn_new_x,
            left_turn_new_y
        )

    backward_direction_index = previous_move_index - 2
    backward_dx = movement_directions[backward_direction_index][1]
    backward_dy = movement_directions[backward_direction_index][2]
    backward_new_x = current_x + backward_dx
    backward_new_y = current_y + backward_dy

    if is_wall_between_coordinates(
        current_x, current_y,
        backward_new_x, backward_new_y
    ):
        return (
            backward_direction_index,
            backward_new_x,
            backward_new_y
        )


movement_directions = [
    ["R", 1, 0],
    ["U", 0, -1],
    ["L", -1, 0],
    ["D", 0, 1]
]

maze_wall_representation = []

movement_history = [0]

for line_index in range(9):
    input_line = input()
    maze_wall_representation.append(input_line)

current_position_x = 1
current_position_y = 0

print("R", end="")

while True:
    next_move_index, current_position_x, current_position_y = determine_next_move(
        current_position_x, current_position_y
    )

    movement_history.append(next_move_index)
    print(movement_directions[next_move_index][0], end="")

    if current_position_x == 0 and current_position_y == 0:
        break

print()