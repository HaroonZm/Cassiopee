import sys
_input_readline = sys.stdin.readline
_input_readlines = sys.stdin.readlines

import numpy as np

item_count = int(_input_readline())
interval_list = [tuple(int(_value) for _value in _line.split()) for _line in _input_readlines()]

interval_list.sort(key=lambda interval: -(interval[0] + interval[1]))

infinity_constant = 10 ** 18
dp_left_uncentered = np.full(1, infinity_constant, np.int64)
dp_left_centered = np.full(1, infinity_constant, np.int64)
if item_count % 2 == 1:
    dp_left_uncentered[0] = 0
else:
    dp_left_centered[0] = 0

for interval_index, (left_value, right_value) in enumerate(interval_list):
    interval_length = left_value + right_value
    prev_dp_left_uncentered = dp_left_uncentered
    prev_dp_left_centered = dp_left_centered
    dp_left_uncentered = np.full(interval_index + 2, infinity_constant, np.int64)
    dp_left_centered = np.full(interval_index + 2, infinity_constant, np.int64)
    left_positions = np.arange(interval_index + 1, dtype=np.int64)
    # Place on left side
    np.minimum(
        prev_dp_left_uncentered[:interval_index + 1] + right_value + left_positions * interval_length,
        dp_left_uncentered[1:interval_index + 2],
        out=dp_left_uncentered[1:interval_index + 2]
    )
    np.minimum(
        prev_dp_left_centered[:interval_index + 1] + right_value + left_positions * interval_length,
        dp_left_centered[1:interval_index + 2],
        out=dp_left_centered[1:interval_index + 2]
    )
    # Place on right side
    np.minimum(
        prev_dp_left_uncentered[:interval_index + 1] + left_value + (interval_index - left_positions) * interval_length,
        dp_left_uncentered[:interval_index + 1],
        out=dp_left_uncentered[:interval_index + 1]
    )
    np.minimum(
        prev_dp_left_centered[:interval_index + 1] + left_value + (interval_index - left_positions) * interval_length,
        dp_left_centered[:interval_index + 1],
        out=dp_left_centered[:interval_index + 1]
    )
    # Place in center
    np.minimum(
        prev_dp_left_uncentered[:interval_index + 1] + ((item_count - 1) // 2) * interval_length,
        dp_left_centered[:interval_index + 1],
        out=dp_left_centered[:interval_index + 1]
    )

result_cost = dp_left_centered[item_count // 2]
print(result_cost)