while True:

    string_to_rotate = raw_input()

    if string_to_rotate == "-":
        break

    total_rotation_offset = 0
    number_of_rotations = int(raw_input())

    for rotation_index in range(number_of_rotations):
        rotation_amount = int(raw_input())
        total_rotation_offset += rotation_amount

    effective_rotation_offset = total_rotation_offset % len(string_to_rotate)

    rotated_string = string_to_rotate[effective_rotation_offset:] + string_to_rotate[:effective_rotation_offset]

    print rotated_string