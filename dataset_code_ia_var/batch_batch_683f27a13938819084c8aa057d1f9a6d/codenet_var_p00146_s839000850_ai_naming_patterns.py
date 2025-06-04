num_packages = int(input())
package_ids = []
package_distances = []
package_weights = []
for package_index in range(num_packages):
    package_id, package_distance, package_value = map(int, input().split())
    package_ids.append(package_id)
    package_distances.append(package_distance)
    package_weights.append(package_value * 20)

memo_table = {}
MAX_SCORE = 10**20

def compute_optimal_sequence(remaining_mask, current_position, current_weight, path_sequence):
    if remaining_mask == 0:
        return 0, []
    if (remaining_mask, current_position) in memo_table:
        return memo_table[(remaining_mask, current_position)]

    candidate_mask = 1
    best_result = (MAX_SCORE, [])
    for candidate_index in range(num_packages):
        if remaining_mask & candidate_mask:
            updated_mask = remaining_mask & ~candidate_mask
            candidate_score, candidate_path = compute_optimal_sequence(updated_mask, candidate_index, current_weight + package_weights[candidate_index], path_sequence)
            movement_cost = abs(package_distances[current_position] - package_distances[candidate_index]) / 2000 * current_weight
            total_score = candidate_score + movement_cost
            candidate_result = (total_score, [candidate_index] + candidate_path)
            if candidate_result < best_result:
                best_result = candidate_result
        candidate_mask <<= 1
    memo_table[(remaining_mask, current_position)] = best_result
    return best_result

all_packages_mask = (1 << num_packages) - 1
optimal_sequence = min(
    [compute_optimal_sequence(all_packages_mask, start_index, 70, []) for start_index in range(num_packages)]
)
print(*[package_ids[index] for index in optimal_sequence[1]])