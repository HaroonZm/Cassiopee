num_rows, num_pairs = map(int, input().split())

if num_rows % 2 == 1:
    for pair_index in range(1, num_pairs + 1):
        first_value = pair_index
        second_value = num_rows - pair_index
        print(first_value, second_value)
else:
    pair_list = []
    max_quarter = num_rows // 4
    half_rows = num_rows // 2
    for pair_index in range(1, max_quarter + 1):
        first_value = pair_index
        second_value = half_rows - pair_index
        pair_list.append((first_value, second_value))
    for pair_index in range(1, max_quarter + 1):
        first_value = half_rows + pair_index
        second_value = num_rows + 1 - pair_index
        pair_list.append((first_value, second_value))

    printed_pairs = 0
    for pair_first, pair_second in pair_list:
        if pair_first != pair_second:
            print(pair_first, pair_second)
            printed_pairs += 1
        if printed_pairs == num_pairs:
            break