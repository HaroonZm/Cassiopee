number_of_points = int(input())

coordinates_list = [list(map(int, input().split())) for _ in range(number_of_points)]

parity_of_first_sum = sum(coordinates_list[0]) % 2

for x_coordinate, y_coordinate in coordinates_list:
    if parity_of_first_sum != (x_coordinate + y_coordinate) % 2:
        print(-1)
        exit()

number_of_steps = 33 - parity_of_first_sum
print(number_of_steps)

movement_lengths = [2 ** i for i in range(31, -1, -1)]
if parity_of_first_sum == 0:
    movement_lengths.append(1)

print(" ".join(map(str, movement_lengths)))

for x_target, y_target in coordinates_list:
    movement_sequence = " "
    for movement_length in movement_lengths:
        if x_target - y_target >= 0 and x_target + y_target >= 0:
            movement_sequence += "R"
            x_target -= movement_length
        elif x_target - y_target < 0 and x_target + y_target >= 0:
            movement_sequence += "U"
            y_target -= movement_length
        elif x_target - y_target >= 0 and x_target + y_target < 0:
            movement_sequence += "D"
            y_target += movement_length
        else:
            movement_sequence += "L"
            x_target += movement_length
    print(movement_sequence)