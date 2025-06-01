def compute_min_difference(min_length, total_segments, segment_lengths):
    max_infinite = 10 ** 20
    min_dp_values = [max_infinite for _ in range(total_segments + 1)]
    min_dp_values[0] = min_length
    for current_end in range(total_segments):
        current_sum = 0
        for current_start in range(current_end, -1, -1):
            current_sum += segment_lengths[current_start]
            if current_end + 1 == total_segments and current_start == 0:
                continue
            if current_sum >= min_length:
                updated_max = max(current_sum, min_dp_values[current_start])
                min_dp_values[current_end + 1] = min(min_dp_values[current_end + 1], updated_max)
    return min_dp_values[total_segments] - min_length

def main():
    total_segments = int(input())
    segment_lengths = [int(input()) for _ in range(total_segments)]
    max_infinite = 10 ** 20
    minimum_difference = max_infinite
    for starting_index in range(total_segments):
        current_length_sum = 0
        for ending_index in range(starting_index, total_segments):
            current_length_sum += segment_lengths[ending_index]
            difference_candidate = compute_min_difference(current_length_sum, total_segments, segment_lengths)
            minimum_difference = min(minimum_difference, difference_candidate)

    print(minimum_difference)

main()