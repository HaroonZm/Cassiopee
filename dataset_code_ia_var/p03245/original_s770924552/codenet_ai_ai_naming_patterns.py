input_count = int(input())
coordinate_list = [list(map(int, input().split())) for _ in range(input_count)]
initial_parity = sum(coordinate_list[0]) % 2
for coord_x, coord_y in coordinate_list:
    if initial_parity != (coord_x + coord_y) % 2:
        print(-1)
        exit()
move_count = 33 - initial_parity
print(move_count)
move_lengths = [2 ** i for i in range(31, -1, -1)]
if initial_parity == 0:
    move_lengths.append(1)
print(" ".join(map(str, move_lengths)))
for point_x, point_y in coordinate_list:
    movement_path = " "
    for move_length in move_lengths:
        if point_x - point_y >= 0 and point_x + point_y >= 0:
            movement_path += "R"
            point_x -= move_length
        elif point_x - point_y < 0 and point_x + point_y >= 0:
            movement_path += "U"
            point_y -= move_length
        elif point_x - point_y >= 0 and point_x + point_y < 0:
            movement_path += "D"
            point_y += move_length
        else:
            movement_path += "L"
            point_x += move_length
    print(movement_path)