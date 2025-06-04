import sys

def calculate_hit_and_blow(number_lists):
    hit_count = 0
    blow_count = 0
    match_flags_1 = [0, 0, 0, 0]
    match_flags_2 = [0, 0, 0, 0]
    number_lists.append(match_flags_1)
    number_lists.append(match_flags_2)
    for idx_primary in range(4):
        pos_primary = idx_primary * 2
        for idx_secondary in range(4):
            pos_secondary = idx_secondary * 2
            if (number_lists[0][pos_primary] == number_lists[1][pos_secondary] and
                number_lists[2][idx_primary] == 0 and
                number_lists[3][idx_secondary] == 0):
                if pos_primary == pos_secondary:
                    hit_count += 1
                else:
                    blow_count += 1
                number_lists[2][idx_primary] = 1
                number_lists[3][idx_secondary] = 1
    print(hit_count, blow_count)

input_flag = 0
input_numbers = []
for input_line in sys.stdin.readlines():
    if input_flag == 0:
        input_numbers.append(input_line)
        input_flag = 1
    elif input_flag == 1:
        input_numbers.append(input_line)
        input_flag = 2
    if input_flag == 2:
        input_flag = 0
        calculate_hit_and_blow(input_numbers)
        del input_numbers[:]