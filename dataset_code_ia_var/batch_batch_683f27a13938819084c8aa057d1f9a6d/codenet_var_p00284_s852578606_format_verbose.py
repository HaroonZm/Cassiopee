def calculate_minimum_operations(start_station, destination_station):
    
    if start_station == destination_station:
        return 0

    operation_count = 0

    if start_station % 2 != 0:
        operation_count += 1
        start_station += 1

    if destination_station % 2 != 0:
        operation_count += 1
        destination_station -= 1

    return operation_count + calculate_minimum_operations(start_station // 2, destination_station // 2)


number_of_queries = int(input())

for query_index in range(number_of_queries):
    start_station_input, destination_station_input = map(int, input().split())
    print(calculate_minimum_operations(start_station_input, destination_station_input))