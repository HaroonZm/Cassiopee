import sys
from sys import stdin

read_line_from_input = stdin.readline

INFINITY_COST = 0x7fffffff

number_of_cities, number_of_days = map(int, read_line_from_input().split())

distance_per_city_list = [int(read_line_from_input()) for current_city_index in range(number_of_cities)]

cost_per_day_list = [int(read_line_from_input()) for current_day_index in range(number_of_days)]

minimum_total_cost = [
    [INFINITY_COST for city_processed_count in range(number_of_cities + 1)]
    for day_index in range(number_of_days + 1)
]

minimum_total_cost[0][0] = 0

for day_index in range(number_of_days):

    for cities_visited_count in range(number_of_cities + 1):
        minimum_total_cost[day_index + 1][cities_visited_count] = minimum_total_cost[day_index][cities_visited_count]

    for cities_visited_count in range(number_of_cities):
        if minimum_total_cost[day_index][cities_visited_count] != INFINITY_COST:
            next_cost = (
                minimum_total_cost[day_index][cities_visited_count]
                + cost_per_day_list[day_index] * distance_per_city_list[cities_visited_count]
            )
            minimum_total_cost[day_index + 1][cities_visited_count + 1] = min(
                minimum_total_cost[day_index + 1][cities_visited_count + 1],
                next_cost
            )

print(minimum_total_cost[number_of_days][number_of_cities])