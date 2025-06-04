num_records, freq_threshold = map(int, input().split())
pair_count_map = {}
for record_idx in range(num_records):
    input_data = input().split()
    item_count = int(input_data[0])
    item_list = input_data[1:]
    for idx1 in range(item_count - 1):
        for idx2 in range(idx1 + 1, item_count):
            pair_tuple = (min(item_list[idx1], item_list[idx2]), max(item_list[idx1], item_list[idx2]))
            if pair_tuple in pair_count_map:
                pair_count_map[pair_tuple] += 1
            else:
                pair_count_map[pair_tuple] = 1
result_pairs = []
for pair_key in pair_count_map:
    if pair_count_map[pair_key] >= freq_threshold:
        result_pairs.append((pair_key, pair_count_map[pair_key]))
result_pairs.sort(key=lambda item: (item[0][0], item[0][1]))
print(len(result_pairs))
for pair_info in result_pairs:
    print(*pair_info[0])