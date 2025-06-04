input_n, input_m = map(int, input().split())
input_tuple_initial = tuple(map(int, input().split()))
input_target_pattern = list(map(int, input().split()))

sequence_level = 0
visited_sequences = {}
current_candidates = []
next_candidates = [input_tuple_initial]
while next_candidates:
    current_candidates, next_candidates = next_candidates, current_candidates
    while current_candidates:
        current_sequence = current_candidates.pop()
        if current_sequence not in visited_sequences:
            visited_sequences[current_sequence] = sequence_level
            mutable_sequence = list(current_sequence)
            for swap_index in range(input_n - 1):
                mutable_sequence[swap_index], mutable_sequence[swap_index + 1] = mutable_sequence[swap_index + 1], mutable_sequence[swap_index]
                next_candidates.append(tuple(mutable_sequence))
                mutable_sequence[swap_index + 1], mutable_sequence[swap_index] = mutable_sequence[swap_index], mutable_sequence[swap_index + 1]
    sequence_level += 1

minimum_steps = sequence_level
for candidate_sequence, step in visited_sequences.items():
    run_lengths = []
    run_counter = 1
    for value_index in range(1, len(candidate_sequence)):
        if candidate_sequence[value_index - 1] == candidate_sequence[value_index]:
            run_counter += 1
        else:
            run_lengths.append(run_counter)
            run_counter = 1
    run_lengths.append(run_counter)
    if run_lengths == input_target_pattern and step < minimum_steps:
        minimum_steps = step

print(minimum_steps)