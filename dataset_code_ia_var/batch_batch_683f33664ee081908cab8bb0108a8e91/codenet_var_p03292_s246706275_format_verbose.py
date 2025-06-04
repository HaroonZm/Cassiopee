first_house_location, second_house_location, third_house_location = map(int, input().split())

cost_to_move_first_and_second = abs(first_house_location - second_house_location)
cost_to_move_second_and_third = abs(second_house_location - third_house_location)
cost_to_move_third_and_first = abs(third_house_location - first_house_location)

all_possible_pairwise_costs = [
    cost_to_move_first_and_second,
    cost_to_move_second_and_third,
    cost_to_move_third_and_first
]

sorted_pairwise_costs = sorted(all_possible_pairwise_costs)

minimal_total_cost = sum(sorted_pairwise_costs[:-1:])

print(minimal_total_cost)