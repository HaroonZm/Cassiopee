DIRECTION_DELTAS = [
    (-1, 0),  # LEFT
    (0, -1),  # DOWN
    (1, 0),   # RIGHT
    (0, 1)    # UP
]

while True:
    square_count = int(input())
    if square_count == 0:
        break

    x_position_list = [0]
    y_position_list = [0]

    for square_index in range(square_count - 1):
        adjacent_square_index, move_direction_index = map(int, input().split())
        current_x = x_position_list[adjacent_square_index]
        current_y = y_position_list[adjacent_square_index]
        delta_x, delta_y = DIRECTION_DELTAS[move_direction_index]
        next_x = current_x + delta_x
        next_y = current_y + delta_y
        x_position_list.append(next_x)
        y_position_list.append(next_y)

    x_range = max(x_position_list) - min(x_position_list) + 1
    y_range = max(y_position_list) - min(y_position_list) + 1

    print(x_range, y_range)