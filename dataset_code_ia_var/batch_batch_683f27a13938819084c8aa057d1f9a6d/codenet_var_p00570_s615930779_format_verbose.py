number_of_items, number_of_groups = map(int, input().split())

item_positions = [int(input()) for position_index in range(number_of_items)]

distances_between_items = []

for current_index in range(number_of_items - 1):
    distance = item_positions[current_index + 1] - item_positions[current_index] - 1
    distances_between_items.append(distance)

distances_between_items.sort(reverse=True)

minimum_total_length = number_of_items + sum(distances_between_items[number_of_groups - 1:])

print(minimum_total_length)