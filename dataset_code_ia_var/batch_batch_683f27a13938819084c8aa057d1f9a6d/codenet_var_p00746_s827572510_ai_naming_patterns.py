DIRECTION_DELTAS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def compute_field_dimensions(num_positions):
    position_sequence = [(0, 0)]
    for position_index in range(num_positions - 1):
        base_index, direction_index = map(int, input().split())
        base_x, base_y = position_sequence[base_index]
        delta_x, delta_y = DIRECTION_DELTAS[direction_index]
        position_sequence.append((base_x + delta_x, base_y + delta_y))
    min_pos_x = max_pos_x = position_sequence[0][0]
    min_pos_y = max_pos_y = position_sequence[0][1]
    for current_x, current_y in position_sequence:
        if current_x < min_pos_x:
            min_pos_x = current_x
        if current_x > max_pos_x:
            max_pos_x = current_x
        if current_y < min_pos_y:
            min_pos_y = current_y
        if current_y > max_pos_y:
            max_pos_y = current_y
    field_width = max_pos_x - min_pos_x + 1
    field_height = max_pos_y - min_pos_y + 1
    print(field_width, field_height)

while True:
    input_count = int(input())
    if input_count == 0:
        break
    compute_field_dimensions(input_count)