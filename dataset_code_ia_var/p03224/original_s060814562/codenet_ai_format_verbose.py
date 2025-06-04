from itertools import combinations
from math import sqrt

number_of_elements = int(input())

potential_group_count = int(sqrt(2 * number_of_elements)) + 1

if potential_group_count * (potential_group_count - 1) == 2 * number_of_elements:

    distribution_matrix = [
        [0 for _ in range(potential_group_count - 1)]
        for _ in range(potential_group_count)
    ]

    current_assignment_index = [0 for _ in range(potential_group_count)]

    for pair_index, element_pair in enumerate(combinations(range(potential_group_count), 2)):
        for participant in element_pair:
            distribution_matrix[participant][current_assignment_index[participant]] = pair_index + 1
            current_assignment_index[participant] += 1

    print('Yes')
    print(potential_group_count)

    for participant_group in distribution_matrix:
        print(potential_group_count - 1, end=' ')
        for assignment_number in participant_group:
            print(assignment_number, end=' ')
        print('')

else:
    print('No')