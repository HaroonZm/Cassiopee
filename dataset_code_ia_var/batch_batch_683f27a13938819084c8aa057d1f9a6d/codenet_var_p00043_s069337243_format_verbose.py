def is_hand_solved(tile_numbers):

    unique_tile_numbers = set(tile_numbers)

    for pair_tile in unique_tile_numbers:

        if tile_numbers.count(pair_tile) >= 2:

            tiles_remaining = tile_numbers[:]
            tiles_remaining.remove(pair_tile)
            tiles_remaining.remove(pair_tile)

            for base_tile in unique_tile_numbers:

                count_base_tile = tiles_remaining.count(base_tile)

                if count_base_tile == 4:

                    if (base_tile + 1 in tiles_remaining) and (base_tile + 2 in tiles_remaining):
                        for _ in range(4):
                            tiles_remaining.remove(base_tile)
                        tiles_remaining.remove(base_tile + 1)
                        tiles_remaining.remove(base_tile + 2)

                elif count_base_tile == 3:
                    for _ in range(3):
                        tiles_remaining.remove(base_tile)

                elif (tiles_remaining.count(base_tile + 1) >= count_base_tile) and (tiles_remaining.count(base_tile + 2) >= count_base_tile):
                    for _ in range(count_base_tile):
                        tiles_remaining.remove(base_tile)
                        tiles_remaining.remove(base_tile + 1)
                        tiles_remaining.remove(base_tile + 2)

            if tiles_remaining == []:
                return True

    return False


while True:

    try:
        input_tiles_as_string = input()
        input_tiles_as_numbers = list(map(int, list(input_tiles_as_string)))

        possible_winning_tiles = []

        for candidate_tile in range(1, 10):
            if input_tiles_as_numbers.count(candidate_tile) <= 3 and \
               is_hand_solved(input_tiles_as_numbers + [candidate_tile]):
                possible_winning_tiles.append(candidate_tile)

        if possible_winning_tiles:
            print(*possible_winning_tiles)
        else:
            print(0)

    except EOFError:
        break