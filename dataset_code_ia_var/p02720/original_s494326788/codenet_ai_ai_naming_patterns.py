result_sequence = []
def generate_sequence(depth_remaining, previous_digit, current_sequence):
    if depth_remaining == 1:
        if 1 <= previous_digit <= 8:
            return [current_sequence + str(next_digit) for next_digit in [previous_digit - 1, previous_digit, previous_digit + 1]]
        elif previous_digit == 9:
            return [current_sequence + '8', current_sequence + '9']
        else:
            return [current_sequence + '0', current_sequence + '1']
    generated = []
    for candidate_digit in range(max(0, previous_digit - 1), min(previous_digit + 2, 10)):
        generated += generate_sequence(depth_remaining - 1, candidate_digit, current_sequence + str(candidate_digit))
    return generated

target_index = int(input())
current_candidates = [str(initial_digit) for initial_digit in range(1, 10)]
current_depth = 2
while len(current_candidates) < target_index:
    for starting_digit in range(1, 10):
        current_candidates += generate_sequence(current_depth - 1, starting_digit, str(starting_digit))
    current_depth += 1
print(current_candidates[target_index - 1])