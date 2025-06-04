import sys
import numpy as np

def main():
    input_stream = sys.stdin
    input_readline = input_stream.readline
    input_readlines = input_stream.readlines

    num_intervals = int(input_readline())
    interval_list = [tuple(map(int, line.split())) for line in input_readlines()]

    interval_list.sort(key=lambda interval: -(interval[0] + interval[1]))

    max_cost = 10 ** 18
    dp_center_unused = np.full(num_intervals + 1, max_cost, np.int64)
    dp_center_used = np.full(num_intervals + 1, max_cost, np.int64)

    if num_intervals % 2 == 1:
        dp_center_unused[0] = 0
    else:
        dp_center_used[0] = 0

    for idx, (left_cost, right_cost) in enumerate(interval_list):
        curr_length = left_cost + right_cost
        prev_dp_center_unused = dp_center_unused
        prev_dp_center_used = dp_center_used
        dp_center_unused = np.full(num_intervals + 1, max_cost, np.int64)
        dp_center_used = np.full(num_intervals + 1, max_cost, np.int64)

        left_items_arr = np.arange(idx + 1, dtype=np.int64)

        # Place to left
        np.minimum(
            prev_dp_center_unused[:idx + 1] + right_cost + left_items_arr * curr_length,
            dp_center_unused[1:idx + 2],
            out=dp_center_unused[1:idx + 2]
        )
        np.minimum(
            prev_dp_center_used[:idx + 1] + right_cost + left_items_arr * curr_length,
            dp_center_used[1:idx + 2],
            out=dp_center_used[1:idx + 2]
        )

        # Place to right
        np.minimum(
            prev_dp_center_unused[:idx + 1] + left_cost + (idx - left_items_arr) * curr_length,
            dp_center_unused[:idx + 1],
            out=dp_center_unused[:idx + 1]
        )
        np.minimum(
            prev_dp_center_used[:idx + 1] + left_cost + (idx - left_items_arr) * curr_length,
            dp_center_used[:idx + 1],
            out=dp_center_used[:idx + 1]
        )

        # Place to center
        np.minimum(
            prev_dp_center_unused[:idx + 1] + ((num_intervals - 1) // 2) * curr_length,
            dp_center_used[:idx + 1],
            out=dp_center_used[:idx + 1]
        )

    result = dp_center_used[num_intervals // 2]
    print(result)

if __name__ == "__main__":
    main()