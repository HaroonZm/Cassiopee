input_count = int(input())
input_numbers = list(map(int, input().split()))
input_numbers.sort()
found_pair_flag = 0
for outer_index in range(input_count):
    if found_pair_flag == 1:
        break
    for inner_offset in range(1, input_count - outer_index):
        if found_pair_flag == 1:
            break
        if (input_numbers[outer_index + inner_offset] - input_numbers[outer_index]) % (input_count - 1) == 0:
            print(input_numbers[outer_index], input_numbers[outer_index + inner_offset])
            found_pair_flag = 1