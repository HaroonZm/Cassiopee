pair_count = int(input())

pair_list = []
for pair_index in range(pair_count):
    current_pair = tuple(map(int, input().split()))
    pair_list.append(current_pair)

pair_list_sorted_first = sorted(pair_list, key=lambda pair: pair[0])
pair_list_sorted_second = sorted(pair_list, key=lambda pair: pair[1])

if pair_count % 2 == 1:
    median_first_a, median_first_b = pair_list_sorted_first[pair_count // 2]
    median_second_a, median_second_b = pair_list_sorted_second[pair_count // 2]
    print(median_second_b - median_first_a + 1)
else:
    left_first_a, left_first_b = pair_list_sorted_first[pair_count // 2 - 1]
    right_first_a, right_first_b = pair_list_sorted_first[pair_count // 2]
    left_second_a, left_second_b = pair_list_sorted_second[pair_count // 2 - 1]
    right_second_a, right_second_b = pair_list_sorted_second[pair_count // 2]
    print((left_second_b + right_second_b) - (left_first_a + right_first_a) + 1)