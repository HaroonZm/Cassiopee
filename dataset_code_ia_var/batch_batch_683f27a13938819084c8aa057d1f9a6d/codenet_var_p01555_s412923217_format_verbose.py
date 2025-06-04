def count_divisible_numbers_in_range(range_start, range_end, divisor):
    # Counts numbers divisible by divisor in [range_start, range_end)
    return (range_end - 1) // divisor - (range_start - 1) // divisor

def calculate_fizzbuzz_index_for_number(target_number):
    total_fizzbuzz_index, digit_length = 0, 1

    while 10 ** digit_length < target_number:
        digit_limit = 10 ** digit_length
        previous_digit_limit = 10 ** (digit_length - 1)

        count_divisible_by_fifteen = count_divisible_numbers_in_range(previous_digit_limit, digit_limit, 15)
        count_divisible_by_three = count_divisible_numbers_in_range(previous_digit_limit, digit_limit, 3)
        count_divisible_by_five = count_divisible_numbers_in_range(previous_digit_limit, digit_limit, 5)

        total_fizzbuzz_index += (
            digit_length * (digit_limit - previous_digit_limit)
            + (count_divisible_by_three + count_divisible_by_five) * 4
            - (count_divisible_by_three + count_divisible_by_five - count_divisible_by_fifteen) * digit_length
        )

        digit_length += 1

    last_digit_limit = 10 ** (digit_length - 1)
    count_divisible_by_fifteen = count_divisible_numbers_in_range(last_digit_limit, target_number, 15)
    count_divisible_by_three = count_divisible_numbers_in_range(last_digit_limit, target_number, 3)
    count_divisible_by_five = count_divisible_numbers_in_range(last_digit_limit, target_number, 5)

    total_fizzbuzz_index += (
        digit_length * (target_number - last_digit_limit)
        + (count_divisible_by_three + count_divisible_by_five) * 4
        - (count_divisible_by_three + count_divisible_by_five - count_divisible_by_fifteen) * digit_length
    )

    return total_fizzbuzz_index

target_character_index = int(input()) - 1

search_left_bound, search_right_bound = 1, 10 ** 18

while search_left_bound + 1 < search_right_bound:
    current_middle_number = (search_left_bound + search_right_bound) // 2
    fizzbuzz_index_at_middle = calculate_fizzbuzz_index_for_number(current_middle_number)

    if fizzbuzz_index_at_middle <= target_character_index:
        search_left_bound = current_middle_number
    else:
        search_right_bound = current_middle_number

fizzbuzz_concatenated_sequence = ""

for candidate_number in range(search_left_bound, search_left_bound + 30):
    fizzbuzz_item = ""

    if candidate_number % 3 == 0:
        fizzbuzz_item += "Fizz"
    if candidate_number % 5 == 0:
        fizzbuzz_item += "Buzz"
    if not fizzbuzz_item:
        fizzbuzz_item = str(candidate_number)

    fizzbuzz_concatenated_sequence += fizzbuzz_item

fizzbuzz_index_at_left_bound = calculate_fizzbuzz_index_for_number(search_left_bound)
substring_start_index = target_character_index - fizzbuzz_index_at_left_bound
substring_end_index = substring_start_index + 20

print(fizzbuzz_concatenated_sequence[substring_start_index : substring_end_index])