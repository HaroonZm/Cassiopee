def count_subsets_with_sum(total_max_number, current_min_number, elements_left, remaining_sum):
    
    if elements_left == 1:
        if current_min_number < remaining_sum <= total_max_number:
            return 1
        else:
            return 0

    total_ways = 0

    for next_number in range(current_min_number + 1, total_max_number - elements_left + 2):
        total_ways += count_subsets_with_sum(
            total_max_number,
            next_number,
            elements_left - 1,
            remaining_sum - next_number
        )

    return total_ways


while True:
    
    input_values = input().split()
    total_numbers, subset_size, target_sum = map(int, input_values)
    
    if total_numbers == 0 and subset_size == 0 and target_sum == 0:
        break

    print(
        count_subsets_with_sum(
            total_numbers,
            0,
            subset_size,
            target_sum
        )
    )