import sys

def is_valid_hand(tile_sequence):

    global pair_found
    if not tile_sequence and pair_found == 1:
        possible_completion_tiles.append(current_tile_candidate)
        return True

    for tile_value in tile_sequence:

        if check_triplet(tile_value, tile_sequence):
            return True

        if check_pair(tile_value, tile_sequence):
            return True

        if check_sequence(tile_value, tile_sequence):
            return True

def check_triplet(tile_value, tile_sequence):

    triplet_count = 0

    for tile_to_check in tile_sequence[:3]:
        if tile_to_check == tile_value:
            triplet_count += 1

    else:
        if triplet_count == 3:
            if is_valid_hand(tile_sequence[3:]):
                return True

def check_pair(tile_value, tile_sequence):

    global pair_found

    pair_count = 0

    for tile_to_check in tile_sequence[:2]:
        if tile_to_check == tile_value:
            pair_count += 1

    else:
        if pair_count == 2:
            pair_found += 1
            if is_valid_hand(tile_sequence[2:]):
                return True
            pair_found -= 1

def check_sequence(tile_value, tile_sequence):

    potential_sequence = [tile_value, tile_value + 1, tile_value + 2]

    for attempt in range(3):
        for required_tile in potential_sequence:
            if required_tile < 0 or (required_tile not in tile_sequence):
                for decrement_index in range(3):
                    potential_sequence[decrement_index] -= 1
                break
        else:
            for number_in_sequence in potential_sequence:
                index_to_remove = 0
                while tile_sequence:
                    if tile_sequence[index_to_remove] == number_in_sequence:
                        del tile_sequence[index_to_remove]
                        break
                    index_to_remove += 1
            else:
                if is_valid_hand(tile_sequence):
                    return True

pair_found = 0
possible_completion_tiles = []
current_tile_candidate = 0

for input_line in sys.stdin:

    for tile_candidate_index in range(9):

        current_tile_candidate = tile_candidate_index + 1
        trimmed_input = input_line.rstrip()
        tiles_as_string = sorted(trimmed_input + str(current_tile_candidate))
        merged_tile_string = ''.join(tiles_as_string)
        candidate_index = merged_tile_string.find(str(current_tile_candidate))
        # Skip if already 5 of this tile (not a valid draw in Mahjong)
        if merged_tile_string[candidate_index:candidate_index+5] == str(current_tile_candidate)*5:
            continue

        is_valid_hand([int(tile_char) for tile_char in merged_tile_string])

        possible_completion_tiles_sorted_str = sorted([str(tile_number) for tile_number in possible_completion_tiles])
        pair_found = 0

    else:
        if possible_completion_tiles:
            print ' '.join(possible_completion_tiles_sorted_str)
        else:
            print 0

    pair_found = 0
    possible_completion_tiles = []
    current_tile_candidate = 0