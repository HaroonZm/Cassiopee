INFINITY = 10 ** 20

number_of_stations, number_of_days = map(int, input().split())

station_distances = [int(input()) for _ in range(number_of_stations)]

weather_factors = [int(input()) for _ in range(number_of_days)]

minimum_total_cost = [INFINITY] * (number_of_stations + 1)

minimum_total_cost[0] = 0

for current_day_index in range(number_of_days):

    for station_index in range(number_of_stations, 0, -1):

        previous_cost = minimum_total_cost[station_index - 1] + station_distances[station_index - 1] * weather_factors[current_day_index]

        minimum_total_cost[station_index] = min(minimum_total_cost[station_index], previous_cost)

print(minimum_total_cost[number_of_stations])