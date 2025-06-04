import sys
sys.setrecursionlimit(1000000)

BIT_MASKS = [1 << i for i in range(10)]

def find_shortest_time(num_tickets, num_cities, num_edges, start_city, end_city):
    start_city -= 1
    end_city -= 1
    ticket_speeds = list(map(int, input().split()))
    adjacency_list = [[] for _ in range(num_cities)]
    for _ in range(num_edges):
        city_from, city_to, edge_length = map(int, input().split())
        city_from -= 1
        city_to -= 1
        adjacency_list[city_from].append((city_to, edge_length))
        adjacency_list[city_to].append((city_from, edge_length))
    distance = [[float("inf")] * num_cities for _ in range(BIT_MASKS[num_tickets])]
    distance[0][start_city] = 0
    for ticket_mask in range(BIT_MASKS[num_tickets]):
        for ticket_index in range(num_tickets):
            if ticket_mask & BIT_MASKS[ticket_index]:
                continue
            next_ticket_mask = ticket_mask | BIT_MASKS[ticket_index]
            for current_city in range(num_cities):
                for neighbor_city, edge_weight in adjacency_list[current_city]:
                    travel_time = distance[ticket_mask][current_city] + edge_weight / ticket_speeds[ticket_index]
                    if travel_time < distance[next_ticket_mask][neighbor_city]:
                        distance[next_ticket_mask][neighbor_city] = travel_time
    min_time = float("inf")
    for mask in range(BIT_MASKS[num_tickets]):
        if distance[mask][end_city] < min_time:
            min_time = distance[mask][end_city]
    if min_time == float("inf"):
        print("Impossible")
    else:
        print(min_time)

while True:
    input_values = list(map(int, input().split()))
    tickets, cities, edges, start, goal = input_values
    if tickets == 0:
        break
    find_shortest_time(tickets, cities, edges, start, goal)