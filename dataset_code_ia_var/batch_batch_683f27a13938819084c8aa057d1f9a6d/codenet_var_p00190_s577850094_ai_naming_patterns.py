from heapq import heappush as queue_push, heappop as queue_pop

COORDINATE_MAP = [
    (1, 1), (2, 1), (3, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (1, 3), (2, 3), (3, 3)
]

INDEX_TILES = range(11)
INDEX_ZEROS = (11, 12)

def calc_manhattan(coord_a, coord_b):
    x_a, y_a = coord_a
    x_b, y_b = coord_b
    return abs(x_b - x_a) + abs(y_b - y_a)

def calc_heuristic(state_tuple):
    return sum([calc_manhattan(state_tuple[i], COORDINATE_MAP[i]) for i in INDEX_TILES])

def get_swapped_state(state_tuple, idx1, idx2):
    mutable_state = list(state_tuple)
    mutable_state[idx1], mutable_state[idx2] = mutable_state[idx2], mutable_state[idx1]
    return tuple(mutable_state)

def run_solver():
    while True:
        input_tile_top = int(input())
        if input_tile_top == -1:
            break
        row_0 = [-1, -1, input_tile_top, -1, -1]
        row_1 = [-1] + list(map(int, input().split())) + [-1]
        row_2 = list(map(int, input().split()))
        row_3 = [-1] + list(map(int, input().split())) + [-1]
        row_4 = [-1, -1, int(input()), -1, -1]
        board_matrix = [row_0, row_1, row_2, row_3, row_4]

        state_tuple = [None] * 13
        for current_y in range(5):
            for current_x in range(5):
                current_val = board_matrix[current_y][current_x]
                if current_val != -1:
                    if current_val == 0:
                        if not state_tuple[11]:
                            state_tuple[11] = (current_x, current_y)
                        else:
                            state_tuple[12] = (current_x, current_y)
                    else:
                        state_tuple[current_val - 1] = (current_x, current_y)
        state_tuple = tuple(state_tuple)
        visited_states = {}
        visited_states[state_tuple] = True
        state_queue = []
        queue_push(state_queue, (calc_heuristic(state_tuple) + 0, 0, state_tuple))
        while state_queue:
            queue_score, move_count, current_state = queue_pop(state_queue)
            if queue_score == move_count:
                print(move_count)
                break
            for zero_index in INDEX_ZEROS:
                for tile_index in INDEX_TILES:
                    if calc_manhattan(current_state[zero_index], current_state[tile_index]) == 1:
                        swapped_state = get_swapped_state(current_state, tile_index, zero_index)
                        if swapped_state not in visited_states:
                            visited_states[swapped_state] = True
                            next_score = calc_heuristic(swapped_state) + move_count + 1
                            if next_score <= 20:
                                queue_push(state_queue, (next_score, move_count + 1, swapped_state))
        else:
            print("NA")

run_solver()