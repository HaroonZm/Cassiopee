import heapq

input_item_count, input_capacity = [int(item) for item in input().split()]
total_weight = 0
total_value = 0
value_ratio_minheap = []

for item_index in range(input_item_count):
    item_weight, item_value = [int(entry) for entry in input().split()]
    if item_weight < 0:
        total_weight += item_weight
        total_value += item_value
        item_weight = -item_weight
        item_value = -item_value
    if item_value > 0:
        if item_weight == 0:
            total_value += item_value
        else:
            heapq.heappush(
                value_ratio_minheap, (-(item_value / item_weight), item_weight, item_value)
            )

while (input_capacity - total_weight) > 1e-9 and value_ratio_minheap:
    current_entry = heapq.heappop(value_ratio_minheap)
    current_weight = current_entry[1]
    current_value = current_entry[2]
    consume_fraction = min(1, (input_capacity - total_weight) / current_weight)
    total_weight += consume_fraction * current_weight
    total_value += consume_fraction * current_value

print(total_value)