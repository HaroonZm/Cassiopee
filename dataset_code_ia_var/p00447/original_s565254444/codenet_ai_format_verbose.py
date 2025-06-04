for number_of_patterns in iter(input, '0'):

    piece_coordinates = [
        [*map(int, input().split())]
        for _ in [0] * int(number_of_patterns)
    ]

    min_piece_x, min_piece_y = min(piece_coordinates)

    number_of_placements = int(input())

    placements = {
        tuple(map(int, input().split()))
        for _ in [0] * number_of_placements
    }

    maximum_piece_x = max([x for x, y in placements])
    maximum_coordinate_x = max([x for x, y in piece_coordinates])

    x_shift_limit = maximum_piece_x - maximum_coordinate_x + min_piece_x

    for placement_x, placement_y in placements:

        if placement_x <= x_shift_limit:

            for piece_x, piece_y in piece_coordinates:

                translated_x = placement_x + piece_x - min_piece_x
                translated_y = placement_y + piece_y - min_piece_y

                if (translated_x, translated_y) not in placements:
                    break

            else:
                print(placement_x - min_piece_x, placement_y - min_piece_y)
                break