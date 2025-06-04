results_for_each_test_case = []

while True:

    number_of_elements_in_sequence = int(input())

    if number_of_elements_in_sequence == 0:
        break

    sequence_of_numbers = list(map(int, input().split()))

    sorted_sequence = sorted(sequence_of_numbers)

    minimum_difference_between_adjacent_numbers = sorted_sequence[-1]

    for index in range(1, number_of_elements_in_sequence):

        current_difference = sorted_sequence[index] - sorted_sequence[index - 1]

        minimum_difference_between_adjacent_numbers = min(
            minimum_difference_between_adjacent_numbers,
            current_difference
        )

    results_for_each_test_case.append(minimum_difference_between_adjacent_numbers)

for minimum_difference in results_for_each_test_case:
    print(minimum_difference)