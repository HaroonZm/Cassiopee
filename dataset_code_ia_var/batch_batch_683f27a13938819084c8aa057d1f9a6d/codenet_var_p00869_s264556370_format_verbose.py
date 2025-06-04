from collections import deque
import sys

read_line_from_stdin = sys.stdin.readline
write_to_stdout = sys.stdout.write

DIRECTION_DICE_ROTATIONS = [
    (1, 5, 2, 3, 0, 4),  # 'U' (Up)
    (3, 1, 0, 5, 4, 2),  # 'R' (Right)
    (4, 0, 2, 3, 5, 1),  # 'D' (Down)
    (2, 1, 5, 0, 4, 3),  # 'L' (Left)
]

POSSIBLE_DICE_DIRECTIONS = (0, 0, 0, 1, 1, 2, 2, 3) * 3

def rotate_single_dice_faces(dice_faces, move_direction_index):
    return tuple(dice_faces[new_position] for new_position in DIRECTION_DICE_ROTATIONS[move_direction_index])

def generate_all_dice_permutations(initial_dice_faces):
    dice_faces = list(initial_dice_faces[:])
    for direction_index in POSSIBLE_DICE_DIRECTIONS:
        yield dice_faces
        dice_faces[:] = [dice_faces[new_position] for new_position in DIRECTION_DICE_ROTATIONS[direction_index]]

def construct_dice_graph():
    initial_dice_faces = [0, 1, 2, 3, 4, 5]
    all_dice_states = list(map(tuple, generate_all_dice_permutations(initial_dice_faces)))
    all_dice_states.sort()
    dice_state_to_index = {tuple(dice_state): index for index, dice_state in enumerate(all_dice_states)}
    dice_state_transitions = [
        [dice_state_to_index[tuple(rotate_single_dice_faces(current_dice_state, direction_index))]
         for direction_index in range(4)]
        for current_dice_state in all_dice_states
    ]
    return all_dice_states, dice_state_transitions

ALL_DICE_STATES, DICE_STATE_GRAPH = construct_dice_graph()

def solve_one_case():
    board_width, board_height = map(int, read_line_from_stdin().split())
    if board_width == 0 and board_height == 0:
        return False

    color_mapping_string = "wrgbcmy#"  # 'w', 'r', 'g', 'b', 'c', 'm', 'y', '#'
    game_board_code = [
        list(map(color_mapping_string.find, read_line_from_stdin().strip()))
        for _ in range(board_height)
    ]
    color_sequence = list(map(color_mapping_string.find, read_line_from_stdin().strip()))
    
    color_to_sequence_position = [-1] * 7
    for sequence_index, color_value in enumerate(color_sequence):
        color_to_sequence_position[color_value] = sequence_index

    color_x_positions = [0] * 8
    color_y_positions = [0] * 8

    for row in range(board_height):
        row_data = game_board_code[row]
        for column in range(board_width):
            color = row_data[column]
            if color >= 1:
                color_x_positions[color] = column
                color_y_positions[color] = row
                if color == 7:  # '#' treated as special
                    row_data[column] = 0

    MOVEMENTS = ((0, -1), (1, 0), (0, 1), (-1, 0))  # Left, Down, Right, Up

    DICE_FACE_POSITIONS_TO_COLORS = (1, 5, 3, 6, 2, 4)
    start_x = color_x_positions[7]
    start_y = color_y_positions[7]

    bfs_queue = deque([(0, start_x, start_y, 0)])  # (current_seq_idx, x, y, dice_orientation_idx)
    distances = [
        [
            [
                {} for _ in range(board_width)
            ] for _ in range(board_height)
        ] for _ in range(7)
    ]
    distances[0][start_y][start_x][0] = 0
    remaining_moves_per_color = [4] * 6  # Up to 4 moves allowed per color
    answer_steps = -1

    while bfs_queue and answer_steps == -1:
        current_seq_idx, current_x, current_y, dice_state_idx = bfs_queue.popleft()

        if remaining_moves_per_color[current_seq_idx] == 0:
            continue

        distances_by_seq = distances[current_seq_idx]
        distances_by_seq_next = distances[current_seq_idx + 1] if current_seq_idx + 1 < 7 else None
        current_dist = distances_by_seq[current_y][current_x][dice_state_idx]

        for direction in range(4):
            delta_x, delta_y = MOVEMENTS[direction]
            next_x = current_x + delta_x
            next_y = current_y + delta_y

            if not (0 <= next_x < board_width and 0 <= next_y < board_height):
                continue

            if game_board_code[next_y][next_x] == -1:
                continue

            next_dice_state_idx = DICE_STATE_GRAPH[dice_state_idx][direction]

            if game_board_code[next_y][next_x] != 0:
                expected_color = DICE_FACE_POSITIONS_TO_COLORS[ALL_DICE_STATES[next_dice_state_idx][0]]
                if (expected_color != game_board_code[next_y][next_x] or
                        color_to_sequence_position[expected_color] != current_seq_idx):
                    continue

                if next_dice_state_idx not in distances_by_seq_next[next_y][next_x]:
                    distances_by_seq_next[next_y][next_x][next_dice_state_idx] = current_dist + 1
                    remaining_moves_per_color[current_seq_idx] -= 1
                    if current_seq_idx + 1 < 6:
                        bfs_queue.append((current_seq_idx + 1, next_x, next_y, next_dice_state_idx))
                    else:
                        answer_steps = current_dist + 1
            else:
                if next_dice_state_idx not in distances_by_seq[next_y][next_x]:
                    distances_by_seq[next_y][next_x][next_dice_state_idx] = current_dist + 1
                    bfs_queue.append((current_seq_idx, next_x, next_y, next_dice_state_idx))

    if answer_steps != -1:
        write_to_stdout("%d\n" % answer_steps)
    else:
        write_to_stdout("unreachable\n")

    return True

while solve_one_case():
    pass