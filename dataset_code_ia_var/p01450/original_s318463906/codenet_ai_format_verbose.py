number_of_items, max_total_weight = map(int, input().split())

modulo = 10**9 + 7

item_weights = [int(input()) for item_index in range(number_of_items)]

item_weights.sort(reverse=True)

remaining_total_weight = sum(item_weights)

count_of_ways_with_weight = [0] * (max_total_weight + 1)
count_of_ways_with_weight[0] = 1

number_of_valid_selections = 0

if remaining_total_weight <= max_total_weight:
    number_of_valid_selections += 1

for item_index in range(number_of_items):

    current_weight = item_weights[item_index]

    remaining_total_weight -= current_weight

    range_start = max(max_total_weight + 1 - current_weight - remaining_total_weight, 0)
    range_end = max(max_total_weight + 1 - remaining_total_weight, 0)

    number_of_valid_selections += sum(
        count_of_ways_with_weight[range_start:range_end]
    ) % modulo

    for total_weight in range(max_total_weight, current_weight - 1, -1):
        count_of_ways_with_weight[total_weight] += count_of_ways_with_weight[total_weight - current_weight]
        count_of_ways_with_weight[total_weight] %= modulo

print(number_of_valid_selections % modulo)