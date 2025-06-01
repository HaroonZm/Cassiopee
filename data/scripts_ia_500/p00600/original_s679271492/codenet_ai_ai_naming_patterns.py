import sys
from sys import stdin
import heapq

input_line = stdin.readline

while True:
    station_count, district_count = map(int, input_line().split())
    if station_count == 0:
        break

    station_visited = [1] * station_count + [0] * district_count
    priority_queue = []
    adjacency_list = [[] for _ in range(station_count + district_count)]

    for station_index in range(station_count):
        costs_to_districts = list(map(int, input_line().split()))
        for district_index in range(district_count):
            cost = costs_to_districts[district_index]
            if cost > 0:
                heapq.heappush(priority_queue, (cost, station_index, station_count + district_index))

    for district_i in range(district_count - 1):
        costs_between_districts = list(map(int, input_line().split()))
        for district_j_offset, cost in enumerate(costs_between_districts, start=district_i + 1):
            if cost > 0:
                adjacency_list[station_count + district_i].append((station_count + district_j_offset, cost))
                adjacency_list[station_count + district_j_offset].append((station_count + district_i, cost))

    total_cost = 0
    connected_districts = 0

    while connected_districts < district_count:
        while True:
            cost, node_a, node_b = heapq.heappop(priority_queue)
            if station_visited[node_a] == 0 or station_visited[node_b] == 0:
                break
        total_cost += cost
        connected_districts += 1

        if station_visited[node_a]:
            next_node = node_b
        else:
            next_node = node_a

        station_visited[next_node] = 1

        for adjacent_node, edge_cost in adjacency_list[next_node]:
            if station_visited[adjacent_node] == 0:
                heapq.heappush(priority_queue, (edge_cost, next_node, adjacent_node))

    print(total_cost)