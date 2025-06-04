from collections import Counter

pair_counter = Counter()
num_groups, min_frequency = map(int, input().split())

for _ in range(num_groups):
    group_input = input().split()
    group_size = int(group_input[0])
    group_items = group_input[1:]
    group_items.sort()
    for idx_a in range(group_size):
        for idx_b in range(idx_a + 1, group_size):
            item_pair = (group_items[idx_a], group_items[idx_b])
            pair_counter[item_pair] += 1

filtered_pairs = [(pair, count) for pair, count in pair_counter.most_common() if count >= min_frequency]
filtered_pairs.sort()

print(len(filtered_pairs))
for pair, count in filtered_pairs:
    print(*pair)