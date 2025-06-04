total_circular_distance, number_of_houses = map(int, input().split())

house_positions = list(map(int, input().split()))

distance_between_adjacent_houses = []

for current_house_index in range(number_of_houses - 1):
    next_house_distance = house_positions[current_house_index + 1] - house_positions[current_house_index]
    distance_between_adjacent_houses.append(next_house_distance)

wrap_around_distance = total_circular_distance - house_positions[-1] + house_positions[0]
distance_between_adjacent_houses.append(wrap_around_distance)

distance_between_adjacent_houses.sort()

minimum_total_distance = 0

for index in range(number_of_houses - 1):
    minimum_total_distance += distance_between_adjacent_houses[index]

print(minimum_total_distance)