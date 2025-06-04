from math import factorial as math_factorial
from Queue import PriorityQueue as PriorityQueueClass

FACTORIAL_LIST = [math_factorial(idx) for idx in xrange(13)]

MOVE_LEFT, MOVE_UP, MOVE_RIGHT, MOVE_DOWN = 0, 1, 2, 3

MOVE_MATRIX = [[0] for loop_idx in xrange(13)]
MOVE_MATRIX[0]  = [-1, -1, -1, 2]
MOVE_MATRIX[1]  = [-1, -1, 2, 5]
MOVE_MATRIX[2]  = [1, 0, 3, 6]
MOVE_MATRIX[3]  = [2, -1, -1, 7]
MOVE_MATRIX[4]  = [-1, -1, 5, -1]
MOVE_MATRIX[5]  = [4, 1, 6, 9]
MOVE_MATRIX[6]  = [5, 2, 7, 10]
MOVE_MATRIX[7]  = [6, 3, 8, 11]
MOVE_MATRIX[8]  = [7, -1, -1, -1]
MOVE_MATRIX[9]  = [-1, 5, 10, -1]
MOVE_MATRIX[10] = [9, 6, 11, 12]
MOVE_MATRIX[11] = [10, 7, -1, -1]
MOVE_MATRIX[12] = [-1, 10, -1, -1]

def perm_hash(state_cells):
    temp_cells = state_cells[:]
    hash_value = 0
    for idx in xrange(12):
        hash_value += temp_cells[idx] * FACTORIAL_LIST[12-idx]
        for next_idx in xrange(idx+1, 13):
            if temp_cells[next_idx] > temp_cells[idx]:
                temp_cells[next_idx] -= 1
    return hash_value

def perm_dehash(hash_key):
    restored_cells = []
    remaining_hash = hash_key
    for idx in xrange(13):
        quotient = remaining_hash // FACTORIAL_LIST[12-idx]
        restored_cells.append(quotient)
        remaining_hash %= FACTORIAL_LIST[12-idx]
    for idx in xrange(12, -1, -1):
        for nxt_idx in xrange(idx+1, 13):
            if restored_cells[idx] <= restored_cells[nxt_idx]:
                restored_cells[nxt_idx] += 1
    return restored_cells

def heuristic_evaluate(cell_state):
    coordinate_points_matrix = [
        [0,2],
        [1,1], [1,2], [1,3],
        [2,0], [2,1], [2,2], [2,3], [2,4],
        [3,1], [3,2], [3,3],
        [4,2]
    ]
    eval_score = 0
    for idx in xrange(13):
        if not (cell_state[idx] == 0 or cell_state[idx] == 12):
            eval_score += abs(coordinate_points_matrix[cell_state[idx]][0] - coordinate_points_matrix[idx][0])
            eval_score += abs(coordinate_points_matrix[cell_state[idx]][1] - coordinate_points_matrix[idx][1])
    return eval_score

if __name__ == "__main__":
    while True:
        input_cells_list = [input()]
        if input_cells_list == [-1]:
            break
        for row_idx in xrange(4):
            for cell_entry in map(int, raw_input().split()):
                input_cells_list.append(cell_entry)
        input_cells_list[input_cells_list.index(0)] = 12
        priority_queue = PriorityQueueClass()
        initial_hash_value = perm_hash(input_cells_list)
        initial_eval_score = heuristic_evaluate(input_cells_list)
        priority_queue.put([initial_eval_score, initial_hash_value, 0])
        visited_map = {}
        visited_map[initial_hash_value] = True
        answer_result = 0 if initial_eval_score == 0 else "NA"
        step_count = 0
        while not priority_queue.empty():
            step_count += 1
            current_eval, current_hash, current_step = priority_queue.get()
            current_cell_state = perm_dehash(current_hash)
            if not (current_eval <= 20 and answer_result == "NA"):
                break
            for cell_idx in xrange(13):
                if current_cell_state[cell_idx] == 0 or current_cell_state[cell_idx] == 12:
                    for move_dir_idx in [MOVE_LEFT, MOVE_UP, MOVE_RIGHT, MOVE_DOWN]:
                        if not MOVE_MATRIX[cell_idx][move_dir_idx] == -1:
                            partner_idx = MOVE_MATRIX[cell_idx][move_dir_idx]
                            current_cell_state[cell_idx], current_cell_state[partner_idx] = current_cell_state[partner_idx], current_cell_state[cell_idx]
                            neighbor_hash = perm_hash(current_cell_state)
                            if neighbor_hash not in visited_map:
                                neighbor_eval = heuristic_evaluate(current_cell_state)
                                if neighbor_eval == 0:
                                    answer_result = current_step + 1
                                    break
                                priority_queue.put([neighbor_eval + current_step + 1, neighbor_hash, current_step + 1])
                                visited_map[neighbor_hash] = True
                            current_cell_state[cell_idx], current_cell_state[partner_idx] = current_cell_state[partner_idx], current_cell_state[cell_idx]
        print answer_result