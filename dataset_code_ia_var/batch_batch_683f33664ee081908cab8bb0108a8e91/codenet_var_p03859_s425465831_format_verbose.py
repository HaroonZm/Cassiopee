#!/usr/bin/env python3

MODULO = 10 ** 9 + 7

def count_valid_configurations(string_length, num_intervals, binary_string, interval_list):

    cumulative_ones_count = [0] * string_length
    current_one_count = 0

    for current_index in range(string_length):
        if binary_string[current_index] == '1':
            current_one_count += 1
        cumulative_ones_count[current_index] = current_one_count

    dp_table = [[0] * (string_length + 1) for _ in range(string_length + 1)]
    dp_table[0][0] = 1

    furthest_right_end = 0
    next_interval_index = 0

    for current_position in range(string_length):

        while next_interval_index < num_intervals:
            interval_start, interval_end = interval_list[next_interval_index]
            if interval_start <= current_position:
                furthest_right_end = max(furthest_right_end, interval_end)
                next_interval_index += 1
            else:
                break

        if furthest_right_end <= current_position:
            ones_up_to_current = cumulative_ones_count[current_position]
            if ones_up_to_current > 0:
                dp_table[current_position + 1][ones_up_to_current] = (
                    dp_table[current_position][ones_up_to_current]
                    + dp_table[current_position][ones_up_to_current - 1]
                ) % MODULO
            else:
                dp_table[current_position + 1][0] = dp_table[current_position][0]
        else:
            left_most_ones = max(0, cumulative_ones_count[furthest_right_end] - furthest_right_end + current_position)
            right_most_ones = min(current_position + 1, cumulative_ones_count[furthest_right_end])
            for selected_ones_count in range(left_most_ones, right_most_ones + 1):
                if selected_ones_count > 0:
                    dp_table[current_position + 1][selected_ones_count] = (
                        dp_table[current_position][selected_ones_count]
                        + dp_table[current_position][selected_ones_count - 1]
                    ) % MODULO
                else:
                    dp_table[current_position + 1][0] = dp_table[current_position][0]

    return dp_table[string_length][cumulative_ones_count[string_length - 1]]

def main():
    input_string_length, input_num_intervals = input().split()
    input_string_length = int(input_string_length)
    input_num_intervals = int(input_num_intervals)
    input_binary_string = input()
    intervals = []

    for _ in range(input_num_intervals):
        interval_left, interval_right = input().split()
        interval_left = int(interval_left) - 1
        interval_right = int(interval_right) - 1
        intervals.append((interval_left, interval_right))

    result = count_valid_configurations(input_string_length, input_num_intervals, input_binary_string, intervals)
    print(result)

if __name__ == '__main__':
    main()