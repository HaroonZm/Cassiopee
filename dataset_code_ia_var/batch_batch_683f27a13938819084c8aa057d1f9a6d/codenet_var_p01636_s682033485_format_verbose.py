user_input_digits = list(input())

for index in range(len(user_input_digits)):
    user_input_digits[index] = int(user_input_digits[index])

total_valid_partitions = 0

for split_position in range(len(user_input_digits)):

    if user_input_digits[split_position] == 0:
        continue

    number_before_split = 0

    for index_before in range(split_position):
        number_before_split *= 10
        number_before_split += user_input_digits[index_before]

    number_after_split = 0

    for index_after in range(split_position, len(user_input_digits)):
        number_after_split *= 10
        number_after_split += user_input_digits[index_after]

    sum_of_parts = number_before_split + number_after_split

    if sum_of_parts % 2 != 0:
        continue

    first_half = sum_of_parts // 2
    second_half = number_after_split - first_half

    if first_half >= 0 and second_half >= 0:
        total_valid_partitions += 1

print(total_valid_partitions)