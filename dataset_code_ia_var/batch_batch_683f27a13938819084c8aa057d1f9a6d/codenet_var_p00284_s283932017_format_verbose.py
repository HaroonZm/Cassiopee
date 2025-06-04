def calculate_minimum_train_moves(start_station_number, destination_station_number):

    if start_station_number == destination_station_number:
        return 0

    minimum_moves_required = 0

    if start_station_number % 2 == 1:
        minimum_moves_required += 1
        start_station_number += 1

    if destination_station_number % 2 == 1:
        minimum_moves_required += 1
        destination_station_number -= 1

    return minimum_moves_required + calculate_minimum_train_moves(
        start_station_number // 2,
        destination_station_number // 2
    )


number_of_test_cases = int(input())

for test_case_index in range(number_of_test_cases):

    start_station, destination_station = map(int, input().split())

    print(
        calculate_minimum_train_moves(
            start_station,
            destination_station
        )
    )