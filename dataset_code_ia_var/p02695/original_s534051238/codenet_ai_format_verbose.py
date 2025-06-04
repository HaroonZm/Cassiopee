import itertools

number_of_positions, maximum_value_per_position, number_of_constraints = map(int, input().split())

constraint_list = []

for _ in range(number_of_constraints):
    start_index, end_index, required_difference, constraint_reward = map(int, input().split())
    constraint_list.append(
        (start_index, end_index, required_difference, constraint_reward)
    )

def calculate_total_reward(candidate_sequence, constraint_list):
    total_reward = 0
    for start_index, end_index, required_difference, constraint_reward in constraint_list:
        if candidate_sequence[end_index - 1] - candidate_sequence[start_index - 1] == required_difference:
            total_reward += constraint_reward
    return total_reward

maximum_total_reward = 0

possible_values = range(1, maximum_value_per_position + 1)
all_possible_sequences = itertools.combinations_with_replacement(possible_values, number_of_positions)

for candidate_sequence in all_possible_sequences:
    current_reward = calculate_total_reward(candidate_sequence, constraint_list)
    if current_reward > maximum_total_reward:
        maximum_total_reward = current_reward

print(maximum_total_reward)