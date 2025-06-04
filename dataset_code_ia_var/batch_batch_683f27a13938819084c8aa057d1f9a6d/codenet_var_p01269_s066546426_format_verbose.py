from heapq import heappush, heappop

INFINITE_COST = 10 ** 20

while True:
    number_of_cities, number_of_roads, initial_fuel = map(int, input().split())
    if number_of_cities == 0:
        break

    adjacency_list = [
        [] for _ in range(number_of_cities * (initial_fuel + 1))
    ]

    for _ in range(number_of_roads):
        city_a, city_b, required_fuel, enemy_cost = map(int, input().split())
        city_a_index = city_a - 1
        city_b_index = city_b - 1

        for current_fuel in range(required_fuel, initial_fuel + 1):
            origin_index_a = current_fuel * number_of_cities + city_a_index
            destination_index_b = (current_fuel - required_fuel) * number_of_cities + city_b_index

            adjacency_list[origin_index_a].append((0, destination_index_b))
            adjacency_list[
                current_fuel * number_of_cities + city_b_index
            ].append((0, (current_fuel - required_fuel) * number_of_cities + city_a_index))

        for current_fuel in range(initial_fuel + 1):
            origin_index_a = current_fuel * number_of_cities + city_a_index
            destination_index_b = current_fuel * number_of_cities + city_b_index

            adjacency_list[origin_index_a].append((enemy_cost, destination_index_b))
            adjacency_list[
                current_fuel * number_of_cities + city_b_index
            ].append((enemy_cost, origin_index_a))

    dijkstra_queue = []
    start_node_index = initial_fuel * number_of_cities
    heappush(dijkstra_queue, (0, start_node_index))

    minimum_enemy_costs = [INFINITE_COST] * (number_of_cities * (initial_fuel + 1))
    minimum_enemy_costs[start_node_index] = 0

    while dijkstra_queue:
        current_total_cost, current_node_index = heappop(dijkstra_queue)
        for edge_enemy_cost, adjacent_node_index in adjacency_list[current_node_index]:
            if minimum_enemy_costs[adjacent_node_index] > current_total_cost + edge_enemy_cost:
                minimum_enemy_costs[adjacent_node_index] = current_total_cost + edge_enemy_cost
                heappush(
                    dijkstra_queue,
                    (current_total_cost + edge_enemy_cost, adjacent_node_index),
                )

    destination_city_index = number_of_cities - 1
    minimum_total_cost_to_destination = min(
        minimum_enemy_costs[current_fuel * number_of_cities + destination_city_index]
        for current_fuel in range(initial_fuel + 1)
    )

    print(minimum_total_cost_to_destination)