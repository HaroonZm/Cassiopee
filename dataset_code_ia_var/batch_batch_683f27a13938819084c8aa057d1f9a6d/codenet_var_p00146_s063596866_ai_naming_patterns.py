num_items = int(input())
data_matrix = [list(map(int, input().split())) for idx_data in range(num_items)]
memoization_dict = {(2**num_items-1, idx): (0, ()) for idx in range(num_items)}

def compute_minimal_path(current_state, current_position, current_weight):
    memo_key = (current_state, current_position)
    if memo_key in memoization_dict:
        return memoization_dict[memo_key]
    minimal_result = None
    for next_idx in range(num_items):
        if (current_state >> next_idx) & 1 == 0:
            current_cost = data_matrix[current_position][1]
            next_start, next_dest, next_value = data_matrix[next_idx]
            recursive_result = compute_minimal_path(
                current_state | (1 << next_idx),
                next_idx,
                current_weight + 20 * next_value
            )
            computed_value = (
                recursive_result[0] + abs(current_cost - next_dest) * (70 + current_weight),
                recursive_result[1] + (next_start,)
            )
            if minimal_result is None or computed_value < minimal_result:
                minimal_result = computed_value
    if minimal_result is not None:
        memoization_dict[memo_key] = minimal_result
    return minimal_result

def main_solver():
    for initial_idx in range(num_items):
        initial_start, initial_dest, initial_value = data_matrix[initial_idx]
        computed_result = compute_minimal_path(
            1 << initial_idx,
            initial_idx,
            20 * initial_value
        )
        yield computed_result[0], computed_result[1] + (initial_start,)

optimal_result = min(main_solver())
print(*reversed(optimal_result[1]))