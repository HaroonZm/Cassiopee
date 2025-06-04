input_point_count = int(input())
input_point_list = [[int(coord) for coord in input().split()] for _ in range(input_point_count)]

coordinate_mod2_reference = (input_point_list[0][0] + input_point_list[0][1]) % 2
for current_x, current_y in input_point_list:
    if (current_x + current_y) % 2 != coordinate_mod2_reference:
        print(-1)
        exit()

if coordinate_mod2_reference == 1:
    move_count = 31
    move_lengths = [2 ** i for i in range(move_count)]
    print(move_count)
    print(" ".join(str(move_length) for move_length in move_lengths))
else:
    move_count = 32
    move_lengths = [1] + [2 ** i for i in range(31)]
    print(move_count)
    print(" ".join(str(move_length) for move_length in move_lengths))

for target_x, target_y in input_point_list:
    x_value = target_x
    y_value = target_y
    if coordinate_mod2_reference == 0:
        x_value -= 1
        print("R", end="")
    coordinate_sum = x_value + y_value
    coordinate_diff = x_value - y_value
    bit_matrix = [[0] * 31 for _ in range(2)]
    if coordinate_sum < 0:
        bit_matrix[0] = [1] * 31
        bit_matrix[0][30] = 0
    else:
        bit_matrix[0][30] = 1
    if coordinate_diff < 0:
        bit_matrix[1] = [1] * 31
        bit_matrix[1][30] = 0
    else:
        bit_matrix[1][30] = 1
    for bit_index in range(30):
        if coordinate_sum >= 0 and abs(coordinate_sum) // 2 >> bit_index & 1:
            bit_matrix[0][bit_index] = 1
        if coordinate_sum < 0 and abs(coordinate_sum) // 2 >> bit_index & 1:
            bit_matrix[0][bit_index] = 0
        if coordinate_diff >= 0 and abs(coordinate_diff) // 2 >> bit_index & 1:
            bit_matrix[1][bit_index] = 1
        if coordinate_diff < 0 and abs(coordinate_diff) // 2 >> bit_index & 1:
            bit_matrix[1][bit_index] = 0
    for horizontal_bit, vertical_bit in zip(bit_matrix[0], bit_matrix[1]):
        if horizontal_bit == 1 and vertical_bit == 1:
            print("R", end="")
        elif horizontal_bit == 0 and vertical_bit == 0:
            print("L", end="")
        elif horizontal_bit == 1 and vertical_bit == 0:
            print("U", end="")
        elif horizontal_bit == 0 and vertical_bit == 1:
            print("D", end="")
    print("")