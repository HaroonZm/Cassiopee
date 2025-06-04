count_items, min_frequency = map(int, input().split())
item_pair_count = {}
for entry_index in range(count_items):
    item_count, *item_list = input().split()
    item_count = int(item_count)
    for first_index in range(item_count):
        for second_index in range(first_index):
            pair_key = tuple(sorted([item_list[first_index], item_list[second_index]]))
            item_pair_count[pair_key] = item_pair_count.get(pair_key, 0) + 1
qualified_pairs = sorted(pair for pair in item_pair_count if item_pair_count[pair] >= min_frequency)
print(len(qualified_pairs))
if qualified_pairs:
    for item_a, item_b in qualified_pairs:
        print(item_a, item_b)