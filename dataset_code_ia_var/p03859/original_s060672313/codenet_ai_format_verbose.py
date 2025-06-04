import sys

import numpy as np

input_stream = sys.stdin.readline

MODULUS = 10 ** 9 + 7

string_length, number_of_constraints = map(int, input_stream().split())

binary_character_array = np.array(
    list(input_stream().rstrip()),
    dtype='U1'
)

constraint_ranges = [
    [int(token) for token in input_stream().split()]
    for _ in range(number_of_constraints)
]

cumulative_count_of_zeros = (binary_character_array == '0').cumsum()
cumulative_count_of_ones = (binary_character_array == '1').cumsum()

maximum_usable_zeros_up_to = np.copy(cumulative_count_of_zeros)
maximum_usable_ones_up_to = np.copy(cumulative_count_of_ones)

for start_index, end_index in constraint_ranges:
    zero_max_to_update = max(
        maximum_usable_zeros_up_to[start_index - 1],
        cumulative_count_of_zeros[end_index - 1]
    )
    one_max_to_update = max(
        maximum_usable_ones_up_to[start_index - 1],
        cumulative_count_of_ones[end_index - 1]
    )
    maximum_usable_zeros_up_to[start_index - 1] = zero_max_to_update
    maximum_usable_ones_up_to[start_index - 1] = one_max_to_update

np.maximum.accumulate(
    maximum_usable_zeros_up_to,
    out=maximum_usable_zeros_up_to
)
np.maximum.accumulate(
    maximum_usable_ones_up_to,
    out=maximum_usable_ones_up_to
)

number_of_ways_to_form_each_prefix_by_one_usage_count = np.zeros(
    string_length + 1,
    dtype=np.int64
)
number_of_ways_to_form_each_prefix_by_one_usage_count[0] = 1

for character_position in range(string_length):

    previous_dp_array = number_of_ways_to_form_each_prefix_by_one_usage_count
    number_of_ways_to_form_each_prefix_by_one_usage_count = np.zeros(
        string_length + 1,
        dtype=np.int64
    )

    minimum_ones_allowed = max(
        0,
        (character_position + 1) - maximum_usable_zeros_up_to[character_position]
    )
    maximum_ones_allowed = maximum_usable_ones_up_to[character_position]

    # Try to place a '0' at the current position
    number_of_ways_to_form_each_prefix_by_one_usage_count[
        minimum_ones_allowed:maximum_ones_allowed + 1
    ] += previous_dp_array[
        minimum_ones_allowed:maximum_ones_allowed + 1
    ]

    # Try to place a '1' at the current position
    minimum_ones_with_one_used = max(1, minimum_ones_allowed)
    number_of_ways_to_form_each_prefix_by_one_usage_count[
        minimum_ones_with_one_used:maximum_ones_allowed + 1
    ] += previous_dp_array[
        minimum_ones_with_one_used - 1:maximum_ones_allowed
    ]

    number_of_ways_to_form_each_prefix_by_one_usage_count %= MODULUS

total_number_of_valid_sequences = number_of_ways_to_form_each_prefix_by_one_usage_count.sum()
print(total_number_of_valid_sequences)