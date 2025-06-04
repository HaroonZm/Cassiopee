import collections

input_count = input()
input_list = [input() for _ in range(int(input_count))]
counter_dict = collections.Counter(input_list)
max_count = max(counter_dict.values())
max_items = [key for key, value in counter_dict.items() if value == max_count]
max_items_sorted = sorted(max_items, key=str.lower)
for idx, item in enumerate(max_items_sorted):
    print(item)