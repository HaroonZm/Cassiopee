number_of_cities, cost_per_distance, fixed_cost = map(int, input().split())

city_positions = list(map(int, input().split()))

total_minimum_cost = 0

for current_city_index in range(1, number_of_cities):
    
    distance_between_cities = city_positions[current_city_index] - city_positions[current_city_index - 1]
    
    travel_cost_by_distance = cost_per_distance * distance_between_cities
    
    minimum_travel_cost = min(travel_cost_by_distance, fixed_cost)
    
    total_minimum_cost += minimum_travel_cost

print(total_minimum_cost)