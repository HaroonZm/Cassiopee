from math import factorial as math_factorial
from Queue import PriorityQueue as QueuePriorityQueue

FACTORIAL_TABLE = [math_factorial(idx) for idx in xrange(13)]

DIR_LEFT, DIR_UP, DIR_RIGHT, DIR_DOWN = 0, 1, 2, 3

MOVE_TABLE = [[0] for _ in xrange(13)]
MOVE_TABLE[0] =   [-1, -1, -1,  2]
MOVE_TABLE[1] =   [-1, -1,  2,  5]
MOVE_TABLE[2] =   [ 1,  0,  3,  6]
MOVE_TABLE[3] =   [ 2, -1, -1,  7]
MOVE_TABLE[4] =   [-1, -1,  5, -1]
MOVE_TABLE[5] =   [ 4,  1,  6,  9]
MOVE_TABLE[6] =   [ 5,  2,  7, 10]
MOVE_TABLE[7] =   [ 6,  3,  8, 11]
MOVE_TABLE[8] =   [ 7, -1, -1, -1]
MOVE_TABLE[9] =   [-1,  5, 10, -1]
MOVE_TABLE[10] =  [ 9,  6, 11, 12]
MOVE_TABLE[11] =  [10,  7, -1, -1]
MOVE_TABLE[12] =  [-1, 10, -1, -1]

def permutation_to_hash(permutation_cell):
    perm = permutation_cell[:]
    perm_hash = 0
    for idx in xrange(12):
        perm_hash += perm[idx] * FACTORIAL_TABLE[12 - idx]
        for tmp_idx in xrange(idx + 1, 13):
            if perm[tmp_idx] > perm[idx]:
                perm[tmp_idx] -= 1
    return perm_hash

def hash_to_permutation(hash_key):
    cell = []
    local_key = hash_key
    for idx in xrange(13):
        value = local_key / FACTORIAL_TABLE[12 - idx]
        cell.append(value)
        local_key %= FACTORIAL_TABLE[12 - idx]
    for idx in xrange(12, -1, -1):
        for tmp_idx in xrange(idx + 1, 13):
            if cell[idx] <= cell[tmp_idx]:
                cell[tmp_idx] += 1
    return cell

def board_evaluate(permutation_cell):
    POSITION_GRID = [
        [0,2], [1,1],[1,2],[1,3],
        [2,0],[2,1],[2,2],[2,3],[2,4],
        [3,1],[3,2],[3,3],
        [4,2]
    ]
    heuristic = 0
    for idx in xrange(13):
        val = permutation_cell[idx]
        if not (val == 0 or val == 12):
            heuristic += abs(POSITION_GRID[val][0] - POSITION_GRID[idx][0])
            heuristic += abs(POSITION_GRID[val][1] - POSITION_GRID[idx][1])
    return heuristic

GOAL_HASHES = [
    permutation_to_hash([0,1,2,3,4,5,6,7,8,9,10,11,12]),
    permutation_to_hash([12,1,2,3,4,5,6,7,8,9,10,11,0])
]

while True:
    input_cells = [input()]
    if input_cells == [-1]:
        break
    for row_idx in xrange(4):
        input_cells.extend(map(int, raw_input().split()))
    input_cells[input_cells.index(0)] = 12
    pq = QueuePriorityQueue()
    pq.put([board_evaluate(input_cells), permutation_to_hash(input_cells), 0])
    visited_dict = {}
    input_hash = permutation_to_hash(input_cells)
    visited_dict[input_hash] = True
    solution = 0 if input_hash in GOAL_HASHES else "NA"
    while not pq.empty():
        heuristic_val, curr_hash, curr_steps = pq.get()
        curr_cells = hash_to_permutation(curr_hash)
        if not (heuristic_val <= 20 and solution == "NA"):
            break
        for position_idx in xrange(13):
            if curr_cells[position_idx] == 0 or curr_cells[position_idx] == 12:
                for direction in [DIR_LEFT, DIR_UP, DIR_RIGHT, DIR_DOWN]:
                    move_pos = MOVE_TABLE[position_idx][direction]
                    if move_pos != -1:
                        curr_cells[position_idx], curr_cells[move_pos] = curr_cells[move_pos], curr_cells[position_idx]
                        next_hash = permutation_to_hash(curr_cells)
                        if not next_hash in visited_dict:
                            if next_hash in GOAL_HASHES:
                                solution = curr_steps + 1
                                break
                            pq.put([board_evaluate(curr_cells) + curr_steps + 1, next_hash, curr_steps + 1])
                            visited_dict[next_hash] = True
                        curr_cells[position_idx], curr_cells[move_pos] = curr_cells[move_pos], curr_cells[position_idx]
    print solution