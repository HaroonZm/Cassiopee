import sys
from sys import stdin
input = stdin.readline

num_stations, num_segments = map(int, input().split())
route_sequence = list(map(int, input().split()))
segment_costs = []
for _ in range(num_stations - 1):
    cost_cash, cost_ic, cost_fee = map(int, input().split())
    segment_costs.append((cost_cash, cost_ic, cost_fee))

segment_usage = [0] * num_stations
for index in range(num_segments - 1):
    start_station = route_sequence[index] - 1
    end_station = route_sequence[index + 1] - 1
    if start_station > end_station:
        start_station, end_station = end_station, start_station
    segment_usage[start_station] += 1
    segment_usage[end_station] -= 1

for station_index in range(num_stations - 1):
    segment_usage[station_index + 1] += segment_usage[station_index]

total_cost = 0
for segment_index in range(num_stations - 1):
    cost_cash, cost_ic, cost_fee = segment_costs[segment_index]
    count = segment_usage[segment_index]
    cost_if_cash = cost_cash * count
    cost_if_ic = cost_ic * count + cost_fee
    total_cost += min(cost_if_cash, cost_if_ic)

print(total_cost)