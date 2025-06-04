#!/usr/bin/env python3
import sys

def compute_maximum_score(
    sequence_length: int,
    maximum_value: int,
    number_of_conditions: int,
    start_indices: "List[int]",
    end_indices: "List[int]",
    required_differences: "List[int]",
    rewards: "List[int]"
):
    from itertools import combinations_with_replacement

    highest_total_reward = 0

    for possible_sequence in combinations_with_replacement(range(1, maximum_value + 1), r=sequence_length):

        current_sequence_reward = 0

        for condition_index in range(number_of_conditions):

            start_index = start_indices[condition_index] - 1
            end_index = end_indices[condition_index] - 1
            required_difference = required_differences[condition_index]
            reward = rewards[condition_index]

            if possible_sequence[end_index] - possible_sequence[start_index] == required_difference:
                current_sequence_reward += reward

        if current_sequence_reward > highest_total_reward:
            highest_total_reward = current_sequence_reward

    print(highest_total_reward)
    return

def main():
    def read_space_separated_tokens_from_stdin():
        for input_line in sys.stdin:
            for token in input_line.split():
                yield token

    input_token_generator = read_space_separated_tokens_from_stdin()

    sequence_length = int(next(input_token_generator))
    maximum_value = int(next(input_token_generator))
    number_of_conditions = int(next(input_token_generator))

    start_indices = [0] * number_of_conditions
    end_indices = [0] * number_of_conditions
    required_differences = [0] * number_of_conditions
    rewards = [0] * number_of_conditions

    for condition_index in range(number_of_conditions):
        start_indices[condition_index] = int(next(input_token_generator))
        end_indices[condition_index] = int(next(input_token_generator))
        required_differences[condition_index] = int(next(input_token_generator))
        rewards[condition_index] = int(next(input_token_generator))

    compute_maximum_score(
        sequence_length,
        maximum_value,
        number_of_conditions,
        start_indices,
        end_indices,
        required_differences,
        rewards
    )

if __name__ == '__main__':
    main()