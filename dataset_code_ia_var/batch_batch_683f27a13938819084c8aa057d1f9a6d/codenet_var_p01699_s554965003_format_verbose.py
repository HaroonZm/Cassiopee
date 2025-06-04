import sys

input_stream_read_line = sys.stdin.readline
output_stream_write = sys.stdout.write

def process_test_case():
    number_of_ranges = int(input_stream_read_line())

    if number_of_ranges == 0:
        return False

    range_start_values = [0] * number_of_ranges
    range_end_values = [0] * number_of_ranges

    for range_index in range(number_of_ranges):
        range_start_values[range_index], range_end_values[range_index] = map(int, input_stream_read_line().split())

    total_states = 1 << (3 * number_of_ranges)
    dp_table = [
        [0] * total_states
        for sequence_length in range(2 * number_of_ranges + 1)
    ]

    # Initialize states for the first digit position
    for first_digit_value in range(1, 10):
        bitmask_for_state = 0

        # Range 0 (first range)
        if range_start_values[0] <= first_digit_value <= range_end_values[0]:
            bitmask_for_state |= 1
        if (
            range_start_values[0] // 10 <= first_digit_value < range_end_values[0] // 10
            or (
                range_start_values[0] // 10 == range_end_values[0] // 10
                and range_start_values[0] // 10 == first_digit_value
            )
        ):
            bitmask_for_state |= 2
        if range_start_values[0] // 10 < first_digit_value <= range_end_values[0] // 10:
            bitmask_for_state |= 4

        dp_table[1][bitmask_for_state] += 1

    state_bitmask_limit = 1 << (3 * number_of_ranges)

    for current_sequence_length in range(1, 2 * number_of_ranges):
        current_state_dp = dp_table[current_sequence_length]
        next_state_dp = dp_table[current_sequence_length + 1]
        for current_bitmask in range(1, state_bitmask_limit):
            current_state_value = current_state_dp[current_bitmask]
            if current_state_value == 0:
                continue
            for next_digit_value in range(10):
                updated_bitmask = 0
                for range_idx in range(number_of_ranges):
                    start_of_current_range = range_start_values[range_idx]
                    end_of_current_range = range_end_values[range_idx]
                    mask_for_subrange = 1 << (3 * range_idx)

                    # Extending the 'full match' to the next digit
                    if (
                        current_bitmask & mask_for_subrange
                        and range_idx < number_of_ranges - 1
                        and next_digit_value > 0
                    ):
                        start_of_next_range = range_start_values[range_idx + 1]
                        end_of_next_range = range_end_values[range_idx + 1]

                        if start_of_next_range <= next_digit_value <= end_of_next_range:
                            updated_bitmask |= (mask_for_subrange << 3)
                        if (
                            start_of_next_range // 10 <= next_digit_value < end_of_next_range // 10
                            or (
                                start_of_next_range // 10 == end_of_next_range // 10
                                and start_of_next_range // 10 == next_digit_value
                            )
                        ):
                            updated_bitmask |= (mask_for_subrange << 4)
                        if start_of_next_range // 10 < next_digit_value <= end_of_next_range // 10:
                            updated_bitmask |= (mask_for_subrange << 5)
                    
                    # Extending partial matches by tens and units
                    if current_bitmask & (mask_for_subrange << 1):
                        if current_bitmask & (mask_for_subrange << 2):
                            updated_bitmask |= mask_for_subrange
                        elif start_of_current_range // 10 == end_of_current_range // 10:
                            if start_of_current_range % 10 <= next_digit_value <= end_of_current_range % 10:
                                updated_bitmask |= mask_for_subrange
                        elif start_of_current_range % 10 <= next_digit_value:
                            updated_bitmask |= mask_for_subrange

                    if current_bitmask & (mask_for_subrange << 2):
                        if next_digit_value <= end_of_current_range % 10:
                            updated_bitmask |= mask_for_subrange

                if updated_bitmask != 0:
                    next_state_dp[updated_bitmask] += current_state_value

    total_valid_sequences = 0
    for dp_row_index in range(2 * number_of_ranges + 1):
        current_dp_row = dp_table[dp_row_index]
        significant_bit = 1 << (3 * number_of_ranges - 3)
        total_valid_sequences += sum(
            current_dp_row[state_bit_index]
            for state_bit_index in range(state_bitmask_limit)
            if state_bit_index & significant_bit
        )

    output_stream_write("%d\n" % total_valid_sequences)
    return True

while process_test_case():
    ...