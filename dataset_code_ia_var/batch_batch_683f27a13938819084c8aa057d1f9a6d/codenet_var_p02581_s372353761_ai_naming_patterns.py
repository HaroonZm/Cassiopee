def relation_insert(rel_dict, key_first, key_second):
    if key_first not in rel_dict:
        rel_dict[key_first] = {}
    if key_second not in rel_dict[key_first]:
        rel_dict[key_first][key_second] = 0

input_count = int(input())
input_list = list(map(int, input().split()))

if input_count == 1:
    print(1)
    exit()

dp_table = [[-1] * (input_count + 1) for _ in range(input_count + 1)]
max_array = [-1] * (input_count + 1)
relation_dict = {}
for idx in range(5):
    element = input_list[idx]
    if element in relation_dict:
        relation_dict[element] += 1
    else:
        relation_dict[element] = 1

triplet_flag = 0
for key_value in relation_dict.keys():
    if relation_dict[key_value] >= 3:
        triplet_flag = 1
        relation_dict[key_value] -= 3

pair_list = []
for key_value in relation_dict.keys():
    if relation_dict[key_value] == 2:
        pair_list.append(key_value)
        dp_table[key_value][key_value] = triplet_flag
        max_array[key_value] = triplet_flag
    elif relation_dict[key_value] == 1:
        pair_list.append(key_value)
        max_array[key_value] = triplet_flag

for first_idx in range(len(pair_list) - 1):
    for second_idx in range(first_idx + 1, len(pair_list)):
        dp_table[pair_list[first_idx]][pair_list[second_idx]] = triplet_flag

common_counter = 0
for loop_idx in range(5, input_count * 3 - 3, 3):
    frequency_list = []
    for freq_idx in range(loop_idx, loop_idx + 3):
        for fl_idx in range(len(frequency_list)):
            if frequency_list[fl_idx][1] == input_list[freq_idx]:
                frequency_list[fl_idx][0] += 1
                break
        else:
            frequency_list.append([1, input_list[freq_idx]])
    frequency_list.sort()
    new_relation_dict = {}
    if len(frequency_list) == 1:
        common_counter += 1
    elif len(frequency_list) == 2:
        first_val = frequency_list[0][1]
        second_val = frequency_list[1][1]
        if dp_table[first_val][first_val] != -1:
            relation_insert(new_relation_dict, second_val, second_val)
            new_relation_dict[second_val][second_val] = max([
                new_relation_dict[second_val][second_val],
                dp_table[second_val][second_val],
                dp_table[first_val][first_val] + 1
            ])
        for idx in range(input_count + 1):
            relation_val = max(dp_table[second_val][idx], dp_table[idx][second_val])
            if relation_val == -1:
                continue
            relation_insert(new_relation_dict, first_val, idx)
            new_relation_dict[first_val][idx] = max([
                new_relation_dict[first_val][idx],
                dp_table[first_val][idx],
                relation_val + 1
            ])
        for idx in range(input_count + 1):
            relation_val = max_array[idx]
            if relation_val == -1:
                continue
            relation_insert(new_relation_dict, first_val, idx)
            new_relation_dict[first_val][idx] = max(new_relation_dict[first_val][idx], relation_val)
            relation_insert(new_relation_dict, second_val, idx)
            new_relation_dict[second_val][idx] = max(new_relation_dict[second_val][idx], relation_val)
        max_value = max(max_array)
        relation_insert(new_relation_dict, first_val, second_val)
        new_relation_dict[first_val][second_val] = max(new_relation_dict[first_val][second_val], max_value)
        relation_insert(new_relation_dict, second_val, second_val)
        new_relation_dict[second_val][second_val] = max(new_relation_dict[second_val][second_val], max_value)
    elif len(frequency_list) == 3:
        first_val = frequency_list[0][1]
        second_val = frequency_list[1][1]
        third_val = frequency_list[2][1]
        relation_insert(new_relation_dict, second_val, third_val)
        relation_insert(new_relation_dict, first_val, third_val)
        relation_insert(new_relation_dict, first_val, second_val)
        if dp_table[first_val][first_val] != -1:
            new_relation_dict[second_val][third_val] = max(new_relation_dict[second_val][third_val], dp_table[first_val][first_val] + 1)
        if dp_table[second_val][second_val] != -1:
            new_relation_dict[first_val][third_val] = max(new_relation_dict[first_val][third_val], dp_table[second_val][second_val] + 1)
        if dp_table[third_val][third_val] != -1:
            new_relation_dict[first_val][second_val] = max(new_relation_dict[first_val][second_val], dp_table[third_val][third_val] + 1)
        for idx in range(input_count + 1):
            relation_val = max_array[idx]
            if relation_val == -1:
                continue
            relation_insert(new_relation_dict, first_val, idx)
            new_relation_dict[first_val][idx] = max(new_relation_dict[first_val][idx], relation_val)
            relation_insert(new_relation_dict, second_val, idx)
            new_relation_dict[second_val][idx] = max(new_relation_dict[second_val][idx], relation_val)
            relation_insert(new_relation_dict, third_val, idx)
            new_relation_dict[third_val][idx] = max(new_relation_dict[third_val][idx], relation_val)
        max_value = max(max_array)
        new_relation_dict[first_val][second_val] = max(new_relation_dict[first_val][second_val], max_value)
        new_relation_dict[second_val][third_val] = max(new_relation_dict[second_val][third_val], max_value)
        new_relation_dict[first_val][third_val] = max(new_relation_dict[first_val][third_val], max_value)
    for rel_key in new_relation_dict.keys():
        for rel_sub_key in new_relation_dict[rel_key].keys():
            relation_val = new_relation_dict[rel_key][rel_sub_key]
            dp_table[rel_key][rel_sub_key] = max(dp_table[rel_key][rel_sub_key], relation_val)
            dp_table[rel_sub_key][rel_key] = max(dp_table[rel_sub_key][rel_key], relation_val)
            max_array[rel_key] = max(max_array[rel_key], relation_val)
            max_array[rel_sub_key] = max(max_array[rel_sub_key], relation_val)

last_element = input_list[-1]
if dp_table[last_element][last_element] != -1:
    dp_table[last_element][last_element] += 1

answer_val = 0
for matrix_row in dp_table:
    for cell_value in matrix_row:
        answer_val = max(answer_val, cell_value)

answer_val += common_counter

print(answer_val)