import itertools

while True:

    number_of_elements, subset_size, target_sum = map(int, input().split())

    if number_of_elements == 0:
        break

    possible_combinations = itertools.combinations(range(1, number_of_elements + 1), subset_size)

    number_of_valid_subsets = sum(
        1 if sum(combination) == target_sum else 0
        for combination in possible_combinations
    )

    print(number_of_valid_subsets)