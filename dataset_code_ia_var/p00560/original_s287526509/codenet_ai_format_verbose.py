from heapq import heapify, heappop, heappush

number_of_points, number_of_stations, max_operations = map(int, input().split())
length_per_operation, station_gap_time, operation_reduction = map(int, input().split())
total_time_available = int(input())
station_positions = [int(input()) - 1 for _ in range(number_of_stations)]

def calculate_max_operations(remaining_time, remaining_distance):
    return min(remaining_time // length_per_operation, remaining_distance - 1)

total_maximum_steps = 0
potential_operations_heap = []

for current_station_index in range(number_of_stations - 1):

    start_position = station_positions[current_station_index]
    end_position = station_positions[current_station_index + 1]

    if station_gap_time * start_position <= total_time_available:
        remaining_time = total_time_available - station_gap_time * start_position
        remaining_distance = end_position - start_position

        max_operations_current = calculate_max_operations(remaining_time, remaining_distance)
        total_maximum_steps += max_operations_current + 1

        remaining_time -= (max_operations_current + 1) * operation_reduction
        remaining_distance -= (max_operations_current + 1)

        extra_operations = calculate_max_operations(remaining_time, remaining_distance)

        if extra_operations >= 0:
            potential_operations_heap.append((-extra_operations, remaining_time, remaining_distance))

if station_gap_time * station_positions[-1] <= total_time_available:
    total_maximum_steps += 1

heapify(potential_operations_heap)

for _ in range(max_operations - number_of_stations):
    if not potential_operations_heap:
        break

    neg_operations, remaining_time, remaining_distance = heappop(potential_operations_heap)
    operations_to_apply = -neg_operations

    remaining_time -= (operations_to_apply + 1) * operation_reduction
    remaining_distance -= (operations_to_apply + 1)
    total_maximum_steps += operations_to_apply + 1

    extra_operations = calculate_max_operations(remaining_time, remaining_distance)
    if extra_operations >= 0:
        heappush(potential_operations_heap, (-extra_operations, remaining_time, remaining_distance))

print(total_maximum_steps - 1)