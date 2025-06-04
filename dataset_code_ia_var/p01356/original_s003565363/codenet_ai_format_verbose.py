import sys

input_stream = sys.stdin.readline
output_stream = sys.stdout.write

def find_minimum_difference():
    total_terms, target_sum, factor_a, factor_b, increment_a, increment_b = map(int, input_stream().split())
    minimal_difference = target_sum

    if factor_a == 1 and factor_b == 1:
        combined_increment = increment_a + increment_b
        max_visible_terms = min(total_terms, target_sum // combined_increment)
        minimal_difference = min(minimal_difference, target_sum - max_visible_terms * combined_increment)
        if max_visible_terms + 1 <= total_terms:
            minimal_difference = min(minimal_difference, (max_visible_terms + 1) * combined_increment - target_sum)
    else:
        current_index = 0
        generated_sequence = []
        power_a = 1
        power_b = 1
        while current_index < total_terms:
            current_value = increment_a * power_a + increment_b * power_b
            generated_sequence.append(current_value)
            if current_value > target_sum:
                break
            power_a *= factor_a
            power_b *= factor_b
            current_index += 1

        def generate_possible_sums(sub_sequence):
            possible_sums = {0}
            for value in sub_sequence:
                new_sums = set(possible_sums)
                for existing_sum in possible_sums:
                    new_sums.add(existing_sum + value)
                possible_sums = new_sums
            return sorted(possible_sums)

        sequence_length = len(generated_sequence)
        first_half_sums = generate_possible_sums(generated_sequence[:sequence_length // 2])
        second_half_sums = generate_possible_sums(generated_sequence[sequence_length // 2:])
        last_index = len(second_half_sums) - 1

        # Find the closest sum that does not exceed target_sum
        for partial_sum in first_half_sums:
            while last_index > 0 and partial_sum + second_half_sums[last_index] > target_sum:
                last_index -= 1
            if partial_sum + second_half_sums[last_index] <= target_sum:
                minimal_difference = min(minimal_difference, target_sum - partial_sum - second_half_sums[last_index])

        last_index = len(second_half_sums) - 1
        # Find the closest sum that is at least target_sum
        for partial_sum in first_half_sums:
            while last_index > 0 and partial_sum + second_half_sums[last_index - 1] >= target_sum:
                last_index -= 1
            if partial_sum + second_half_sums[last_index] >= target_sum:
                minimal_difference = min(minimal_difference, partial_sum + second_half_sums[last_index] - target_sum)

    output_stream(f"{minimal_difference}\n")

find_minimum_difference()