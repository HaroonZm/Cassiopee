import bisect

def assign_fish_to_nearest_bait(bait_locations_sorted, fish_list, fish_total_at_bait, fish_indices_at_bait, fish_index):
    """
    Associe un poisson à l'appât le plus proche et met à jour les totaux et indices.
    """
    fish_x_location = fish_list[fish_index][0]
    amount_of_fish = fish_list[fish_index][2]
    index_for_right_bait = bisect.bisect_left(bait_locations_sorted, fish_x_location)

    if index_for_right_bait == 0:
        nearest_left_bait_location = -1e10
        nearest_right_bait_location = bait_locations_sorted[index_for_right_bait]
    elif index_for_right_bait == len(bait_locations_sorted):
        nearest_left_bait_location = bait_locations_sorted[index_for_right_bait - 1]
        nearest_right_bait_location = 1e10
    else:
        nearest_left_bait_location = bait_locations_sorted[index_for_right_bait - 1]
        nearest_right_bait_location = bait_locations_sorted[index_for_right_bait]

    distance_to_left_bait = abs(fish_x_location - nearest_left_bait_location)
    distance_to_right_bait = abs(fish_x_location - nearest_right_bait_location)

    if distance_to_left_bait <= distance_to_right_bait:
        fish_total_at_bait[index_for_right_bait - 1] += amount_of_fish
        fish_indices_at_bait[index_for_right_bait - 1].append(fish_index)
    else:
        fish_total_at_bait[index_for_right_bait] += amount_of_fish
        fish_indices_at_bait[index_for_right_bait].append(fish_index)

while True:
    input_line = raw_input()
    number_of_fish, number_of_baits = [int(value) for value in input_line.split()]

    if number_of_baits == 0:
        break

    fish_list = []
    bait_locations_sorted = []
    fish_total_at_bait = [0 for _ in range(number_of_baits)]
    fish_indices_at_bait = [[] for _ in range(number_of_baits)]

    for _ in range(number_of_fish):
        fish_info_input = raw_input()
        fish_position_x, fish_position_y, amount_of_fish = [int(val) for val in fish_info_input.split()]
        fish_list.append([fish_position_x, fish_position_y, amount_of_fish])

    for _ in range(number_of_baits):
        bait_location_input = int(raw_input())
        bait_locations_sorted.append(bait_location_input)

    bait_locations_sorted.sort()

    total_amount_of_fish = sum([fish_list[index][2] for index in range(number_of_fish)])

    for fish_index in range(number_of_fish):
        assign_fish_to_nearest_bait(
            bait_locations_sorted,
            fish_list,
            fish_total_at_bait,
            fish_indices_at_bait,
            fish_index
        )

    minimum_maximum_value = total_amount_of_fish

    for _ in range(number_of_baits - 1):
        current_max_fish = max(fish_total_at_bait)
        minimum_maximum_value = min(minimum_maximum_value, current_max_fish)

        index_of_bait_with_most_fish = fish_total_at_bait.index(current_max_fish)
        fish_indices_to_redistribute = fish_indices_at_bait[index_of_bait_with_most_fish]

        bait_locations_sorted = (
            bait_locations_sorted[:index_of_bait_with_most_fish] +
            bait_locations_sorted[index_of_bait_with_most_fish + 1:]
        )
        fish_total_at_bait = (
            fish_total_at_bait[:index_of_bait_with_most_fish] +
            fish_total_at_bait[index_of_bait_with_most_fish + 1:]
        )
        fish_indices_at_bait = (
            fish_indices_at_bait[:index_of_bait_with_most_fish] +
            fish_indices_at_bait[index_of_bait_with_most_fish + 1:]
        )

        for fish_index in fish_indices_to_redistribute:
            assign_fish_to_nearest_bait(
                bait_locations_sorted,
                fish_list,
                fish_total_at_bait,
                fish_indices_at_bait,
                fish_index
            )

    print minimum_maximum_value