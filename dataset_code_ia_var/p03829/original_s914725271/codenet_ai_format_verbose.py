import itertools

number_of_positions, cost_per_unit_distance, maximum_cost = map(int, input().split())

positions_list = list(map(int, input().split()))

total_minimal_travel_cost = 0

for current_position, next_position in zip(positions_list, positions_list[1:]):

    absolute_distance = abs(current_position - next_position)

    calculated_travel_cost = cost_per_unit_distance * absolute_distance

    minimal_travel_cost = min(calculated_travel_cost, maximum_cost)

    total_minimal_travel_cost += minimal_travel_cost

print(total_minimal_travel_cost)