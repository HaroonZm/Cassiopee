num_records, min_count = map(int, input().split())
records_list = []
pair_frequency_dict = {}

for record_index in range(num_records):
    records_list.append(list(input().split()))
    for item_index_1 in range(1, len(records_list[record_index]) - 1):
        for item_index_2 in range(item_index_1 + 1, len(records_list[record_index])):
            item_a = records_list[record_index][item_index_1]
            item_b = records_list[record_index][item_index_2]
            smaller_item, larger_item = min(item_a, item_b), max(item_a, item_b)
            pair_key = (smaller_item, larger_item)
            if pair_key not in pair_frequency_dict:
                pair_frequency_dict[pair_key] = 1
            else:
                pair_frequency_dict[pair_key] += 1

qualified_pairs_list = []
for pair_tuple in pair_frequency_dict:
    if pair_frequency_dict[pair_tuple] >= min_count:
        qualified_pairs_list.append(list(pair_tuple))

qualified_pairs_list = sorted(qualified_pairs_list, key=lambda x: x[1])
qualified_pairs_list = sorted(qualified_pairs_list)
print(len(qualified_pairs_list))
if len(qualified_pairs_list) != 0:
    for result_index in range(len(qualified_pairs_list)):
        print(*qualified_pairs_list[result_index])