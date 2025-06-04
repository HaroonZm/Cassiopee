import itertools

def main():
    num_elements, num_swaps = map(int, input().split())
    swap_indices = [int(input()) - 1 for _ in range(num_swaps)]
    original_order = list(range(num_elements))
    for idx in range(num_elements):
        for swap_pos in swap_indices:
            if original_order[idx] == swap_pos:
                original_order[idx] = swap_pos + 1
            elif original_order[idx] == swap_pos + 1:
                original_order[idx] = swap_pos
    min_max_step = 10
    for swap_order in itertools.permutations(swap_indices):
        current_order = list(range(num_elements))
        for idx in range(num_elements):
            for swap_pos in swap_order:
                if current_order[idx] == swap_pos:
                    current_order[idx] = swap_pos + 1
                elif current_order[idx] == swap_pos + 1:
                    current_order[idx] = swap_pos
        if current_order != original_order:
            continue
        steps_per_position = [0] * num_elements
        for op_idx in range(num_swaps):
            left = swap_order[op_idx]
            step = max(steps_per_position[left], steps_per_position[left + 1])
            steps_per_position[left] = step + 1
            steps_per_position[left + 1] = step + 1
        min_max_step = min(min_max_step, max(steps_per_position))
    print(min_max_step)

if __name__ == "__main__":
    main()