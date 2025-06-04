import itertools

while True:

    total_numbers, numbers_chosen, target_sum = map(int, input().split())

    if total_numbers + numbers_chosen + target_sum == 0:
        break

    possible_combinations = itertools.combinations(range(1, total_numbers + 1), numbers_chosen)

    count_valid_combinations = 0

    for combination in possible_combinations:
        if sum(combination) != target_sum:
            continue
        count_valid_combinations += 1

    print(count_valid_combinations)