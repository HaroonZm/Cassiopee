number_of_cities, cost_per_distance_unit, fixed_cost = map(int, input().split())

city_locations = [int(location) for location in input().split()]

total_travel_cost = 0

for city_index in range(1, number_of_cities):

    distance_between_cities = city_locations[city_index] - city_locations[city_index - 1]

    variable_cost = cost_per_distance_unit * distance_between_cities

    if variable_cost >= fixed_cost:

        total_travel_cost += fixed_cost

    else:

        total_travel_cost += variable_cost

print(total_travel_cost)