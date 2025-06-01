import sys
sys.setrecursionlimit(10002)

height, num_obstacles = [int(value) for value in input().split()]
locate_put_sets = [set(), {0, 1}, {1, 2}, {2, 3}, {0, 1, 2, 3}]
not_obstructed_per_level = [{0, 1, 2, 3} for _ in range(height)]
memoized_fn = {}

for _ in range(num_obstacles):
    x_coordinate, y_level = [int(value) for value in input().split()]
    not_obstructed_per_level[y_level].remove(x_coordinate)

def compute_max_count(level_index, previous_way_index):
    if (level_index, previous_way_index) in memoized_fn:
        return memoized_fn[(level_index, previous_way_index)]
    if level_index == 0:
        return 0
    max_count = 0
    for current_way_index, current_put_set in enumerate(locate_put_sets):
        available_positions = not_obstructed_per_level[level_index] - locate_put_sets[previous_way_index] & not_obstructed_per_level[level_index - 1]
        if current_put_set.issubset(available_positions):
            count = compute_max_count(level_index - 1, current_way_index)
            if current_way_index == 0:
                increment = 0
            elif current_way_index == 4:
                increment = 2
            else:
                increment = 1
            count += increment
            max_count = count if count > max_count else max_count
    memoized_fn[(level_index, previous_way_index)] = max_count
    return max_count

print(compute_max_count(height - 1, 0))