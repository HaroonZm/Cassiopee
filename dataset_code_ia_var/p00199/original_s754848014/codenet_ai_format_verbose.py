INFINITY_DISTANCE = 10**10

while True:
    number_of_chairs, number_of_people = [int(value) for value in input().split()]

    if number_of_chairs + number_of_people == 0:
        break

    seat_status_list = ["#" for _ in range(number_of_chairs)]

    for person_index in range(number_of_people):
        person_type = str(input())

        if person_type == "A":
            for seat_index in range(number_of_chairs):
                if seat_status_list[seat_index] == "#":
                    seat_status_list[seat_index] = "A"
                    break

        elif person_type == "B":
            assigned_successfully = False

            for seat_index in range(number_of_chairs - 1, -1, -1):
                if seat_status_list[seat_index] == "#":
                    if seat_index != 0 and seat_status_list[seat_index - 1] == "A":
                        continue
                    if seat_index != number_of_chairs - 1 and seat_status_list[seat_index + 1] == "A":
                        continue
                    seat_status_list[seat_index] = "B"
                    assigned_successfully = True
                    break

            if assigned_successfully:
                continue

            for seat_index in range(number_of_chairs):
                if seat_status_list[seat_index] == "#":
                    seat_status_list[seat_index] = "B"
                    break

        elif person_type == "C":
            if seat_status_list.count("#") == number_of_chairs:
                central_seat_index = number_of_chairs // 2
                seat_status_list[central_seat_index] = "C"
                continue

            assigned_successfully = False

            for seat_index in range(number_of_chairs):
                if seat_status_list[seat_index] != "#":
                    if seat_index != number_of_chairs - 1 and seat_status_list[seat_index + 1] == "#":
                        seat_status_list[seat_index + 1] = "C"
                        assigned_successfully = True
                        break
                    if seat_index != 0 and seat_status_list[seat_index - 1] == "#":
                        seat_status_list[seat_index - 1] = "C"
                        assigned_successfully = True
                        break

        elif person_type == "D":
            if seat_status_list.count("#") == number_of_chairs:
                seat_status_list[0] = "D"
                continue

            distance_calculation_started = False
            seats_distance_map = [0 for _ in range(number_of_chairs)]
            current_distance = 0

            for seat_index in range(number_of_chairs):
                if seat_status_list[seat_index] != "#":
                    current_distance = 0
                    seats_distance_map[seat_index] = current_distance
                    distance_calculation_started = True
                elif distance_calculation_started:
                    current_distance += 1
                    seats_distance_map[seat_index] = current_distance
                else:
                    seats_distance_map[seat_index] = INFINITY_DISTANCE

            distance_calculation_started = False
            for seat_index in range(number_of_chairs - 1, -1, -1):
                if seat_status_list[seat_index] != "#":
                    current_distance = 0
                    seats_distance_map[seat_index] = min(current_distance, seats_distance_map[seat_index])
                    distance_calculation_started = True
                elif distance_calculation_started:
                    current_distance += 1
                    seats_distance_map[seat_index] = min(current_distance, seats_distance_map[seat_index])

            maximum_distance = max(seats_distance_map)

            for seat_index in range(number_of_chairs):
                if seats_distance_map[seat_index] == maximum_distance and seat_status_list[seat_index] == "#":
                    seat_status_list[seat_index] = "D"
                    break

    print("".join(seat_status_list))