range_large_for_attack_zone = range(-2, 3)
range_small_for_attack_zone = range(-1, 2)

attack_zone_large = [
    (delta_x, delta_y)
    for delta_x in range_large_for_attack_zone
    for delta_y in range_large_for_attack_zone
    if 3 < delta_x**2 + delta_y**2 < 6
]

attack_zone_small = [
    (delta_x, delta_y)
    for delta_x in range_small_for_attack_zone
    for delta_y in range_small_for_attack_zone
]

def read_two_integers_from_input():
    return map(int, raw_input().split(" "))

def generate_reachable_positions(current_x, current_y, attack_type_flag):
    attack_zone = [attack_zone_large, attack_zone_small][attack_type_flag > 0]
    valid_positions = set(
        [
            (current_x + delta_x, current_y + delta_y)
            for (delta_x, delta_y) in attack_zone
            if 0 <= current_x + delta_x < 10 and 0 <= current_y + delta_y < 10
        ]
    )
    return valid_positions

while True:

    final_x, final_y = read_two_integers_from_input()
    if final_x == 0 and final_y == 0:
        break

    number_of_steps = input()
    raw_positions = read_two_integers_from_input()
    positions_sequence = zip(raw_positions[0::2], raw_positions[1::2])

    final_positions_set = set([(final_x, final_y)])

    for step_x, step_y in positions_sequence:
        possible_attacker_positions = generate_reachable_positions(
            step_x, step_y, attack_type_flag=1
        )
        next_final_positions_set = set([])

        for curr_final_x, curr_final_y in final_positions_set:
            next_final_positions_set = next_final_positions_set | (
                possible_attacker_positions & generate_reachable_positions(curr_final_x, curr_final_y, attack_type_flag=0)
            )

        final_positions_set = next_final_positions_set

    print ["NA", "OK"][len(final_positions_set) > 0]