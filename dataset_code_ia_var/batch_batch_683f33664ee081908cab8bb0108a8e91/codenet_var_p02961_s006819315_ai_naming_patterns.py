move_step_size = int(input())

def compute_next_step(current_x, current_y):
    if abs(target_x - current_x) + abs(target_y - current_y) >= 2 * move_step_size:
        if abs(target_x - current_x) >= move_step_size:
            step_x = move_step_size if target_x > current_x else -move_step_size
        else:
            step_x = abs(target_x - current_x) * (1 if target_x > current_x else -1)
        step_y = (move_step_size - abs(step_x)) * (1 if target_y > current_y else -1)
    elif abs(target_x - current_x) + abs(target_y - current_y) == move_step_size:
        step_x, step_y = target_x - current_x, target_y - current_y
    else:
        surplus = 2 * move_step_size - abs(target_x - current_x) - abs(target_y - current_y)
        surplus = 0 if surplus % 2 else surplus // 2
        if abs(target_x - current_x) < abs(target_y - current_y):
            step_x = (abs(target_x - current_x) + surplus) * (1 if target_x > current_x else -1)
            step_y = (move_step_size - abs(step_x)) * (1 if target_y > current_y else -1)
        else:
            step_y = (abs(target_y - current_y) + surplus) * (1 if target_y > current_y else -1)
            step_x = (move_step_size - abs(step_y)) * (1 if target_x > current_x else -1)
    return (current_x + step_x, current_y + step_y)

start_x, start_y = 0, 0
target_x, target_y = map(int, input().split())

if move_step_size % 2 == 0 and (target_x + target_y) % 2:
    print(-1)
else:
    path_sequence = []
    while start_x != target_x or start_y != target_y:
        start_x, start_y = compute_next_step(start_x, start_y)
        path_sequence.append((start_x, start_y))
    print(len(path_sequence))
    for path_point in path_sequence:
        print(*path_point)