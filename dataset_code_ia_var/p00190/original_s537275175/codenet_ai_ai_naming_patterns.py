from math import factorial as math_factorial
from Queue import PriorityQueue as StdPriorityQueue

# Constants for board and moves
POS_COUNT = 13
MOVE_DIRECTIONS = 4
DIR_LEFT, DIR_UP, DIR_RIGHT, DIR_DOWN = 0, 1, 2, 3

# Factorials for hashing
factorial_table = [math_factorial(idx) for idx in xrange(POS_COUNT)]

# Move mapping per position
move_map = [[0] for _ in xrange(POS_COUNT)]
move_map[0]  = [-1, -1, -1, 2]
move_map[1]  = [-1, -1, 2, 5]
move_map[2]  = [1, 0, 3, 6]
move_map[3]  = [2, -1, -1, 7]
move_map[4]  = [-1, -1, 5, -1]
move_map[5]  = [4, 1, 6, 9]
move_map[6]  = [5, 2, 7, 10]
move_map[7]  = [6, 3, 8, 11]
move_map[8]  = [7, -1, -1, -1]
move_map[9]  = [-1, 5, 10, -1]
move_map[10] = [9, 6, 11, 12]
move_map[11] = [10, 7, -1, -1]
move_map[12] = [-1, 10, -1, -1]

# Target positions
target_position_map = [
    [0, 2],
    [1, 1], [1, 2], [1, 3],
    [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
    [3, 1], [3, 2], [3, 3],
    [4, 2]
]

def puzzle_hash(state_list):
    temp_state = state_list[:]
    res_hash = 0
    for idx_outer in xrange(POS_COUNT - 1):
        res_hash += temp_state[idx_outer] * factorial_table[POS_COUNT - 1 - idx_outer]
        for idx_inner in xrange(idx_outer + 1, POS_COUNT):
            if temp_state[idx_inner] > temp_state[idx_outer]:
                temp_state[idx_inner] -= 1
    return res_hash

def puzzle_unhash(hash_key):
    cell_state = []
    left_key = hash_key
    for idx in xrange(POS_COUNT):
        quotient = left_key // factorial_table[POS_COUNT - 1 - idx]
        cell_state.append(quotient)
        left_key = left_key % factorial_table[POS_COUNT - 1 - idx]
    for idx_outer in xrange(POS_COUNT - 1, -1, -1):
        for idx_inner in xrange(idx_outer + 1, POS_COUNT):
            if cell_state[idx_outer] <= cell_state[idx_inner]:
                cell_state[idx_inner] += 1
    return cell_state

def board_heuristic(state_list):
    heuristic_score = 0
    for idx in xrange(POS_COUNT):
        tile_val = state_list[idx]
        if tile_val != 0 and tile_val != (POS_COUNT - 1):
            heuristic_score += abs(target_position_map[tile_val][0] - target_position_map[idx][0])
            heuristic_score += abs(target_position_map[tile_val][1] - target_position_map[idx][1])
    return heuristic_score

# Precomputed answers
canonical_start_hashes = [
    puzzle_hash(range(POS_COUNT)),
    puzzle_hash([POS_COUNT-1] + range(1, POS_COUNT-1) + [0])
]

while True:
    flat_input = [input()]
    if flat_input == [-1]:
        break
    for _ in xrange(4):
        flat_input.extend(map(int, raw_input().split()))
    blank_index = flat_input.index(0)
    flat_input[blank_index] = POS_COUNT - 1

    pq_queue = StdPriorityQueue()
    initial_state_hash = puzzle_hash(flat_input)
    pq_queue.put([board_heuristic(flat_input), initial_state_hash, 0])
    visited_hashes = {initial_state_hash: True}
    solution_steps = 0 if initial_state_hash in canonical_start_hashes else "NA"

    while not pq_queue.empty():
        _, cur_hash, cur_step_count = pq_queue.get()
        cur_state = puzzle_unhash(cur_hash)
        if not (cur_step_count < 20 and solution_steps == "NA"):
            break
        for pos_idx in xrange(POS_COUNT):
            if cur_state[pos_idx] == 0 or cur_state[pos_idx] == (POS_COUNT - 1):
                for dir_idx in [DIR_LEFT, DIR_UP, DIR_RIGHT, DIR_DOWN]:
                    dest_idx = move_map[pos_idx][dir_idx]
                    if dest_idx != -1:
                        cur_state[pos_idx], cur_state[dest_idx] = cur_state[dest_idx], cur_state[pos_idx]
                        new_hash = puzzle_hash(cur_state)
                        if new_hash not in visited_hashes:
                            if new_hash in canonical_start_hashes:
                                solution_steps = cur_step_count + 1
                                break
                            pq_queue.put([board_heuristic(cur_state) + cur_step_count + 1, new_hash, cur_step_count + 1])
                            visited_hashes[new_hash] = True
                        cur_state[pos_idx], cur_state[dest_idx] = cur_state[dest_idx], cur_state[pos_idx]
    print solution_steps