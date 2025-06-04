delta_x_moves = [2, 2, 2, 1, 0, -1, -2, -2, -2, -1, 0, 1]

delta_y_moves = [-1, 0, 1, 2, 2, 2, 1, 0, -1, -2, -2, -2]

def is_within_proximity(candidate_x, candidate_y, target_x, target_y):

    if not (0 <= candidate_x <= 9 and 0 <= candidate_y <= 9):
        return False

    return abs(candidate_x - target_x) < 2 and abs(candidate_y - target_y) < 2

def solve_path(current_x, current_y, step_index):

    if step_index == 2 * total_targets:
        return True

    target_x = target_coordinates[step_index]
    target_y = target_coordinates[step_index + 1]

    for move_delta_x, move_delta_y in zip(delta_x_moves, delta_y_moves):

        next_x = current_x + move_delta_x
        next_y = current_y + move_delta_y

        if is_within_proximity(next_x, next_y, target_x, target_y):

            reached = solve_path(next_x, next_y, step_index + 2)
            if reached:
                return True

while True:

    input_line = raw_input()
    start_x, start_y = map(int, input_line.split())

    if start_x == 0 and start_y == 0:
        break

    total_targets = input()
    target_coordinates = map(int, raw_input().split())

    is_solution_found = solve_path(start_x, start_y, 0)

    if is_solution_found:
        print "OK"
    else:
        print "NA"