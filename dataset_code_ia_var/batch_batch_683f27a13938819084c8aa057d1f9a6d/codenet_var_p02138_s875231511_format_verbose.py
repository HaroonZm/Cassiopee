def get_two_integers_from_input():
    return list(map(int, input().split()))

number_of_initial_uki_units, number_of_initial_ushi_units = get_two_integers_from_input()

# --- First Scenario: Destroy all uki units ---

current_uki_first_group = number_of_initial_uki_units
current_uki_second_group = number_of_initial_uki_units
current_ushi_group_1 = number_of_initial_ushi_units
total_ushi_units = number_of_initial_ushi_units * 2

turn_count_to_destroy_uki = 0

while True:
    total_ushi_units -= current_uki_first_group
    current_ushi_group_1 = -(-total_ushi_units // 2)
    
    if total_ushi_units <= 0:
        break

    turn_count_to_destroy_uki += 1

    if current_uki_second_group - current_ushi_group_1 >= 0:
        current_uki_second_group -= current_ushi_group_1
    else:
        current_uki_first_group = current_uki_first_group + current_uki_second_group - current_ushi_group_1
        current_uki_second_group = 0

    if current_uki_first_group <= 0:
        break

    turn_count_to_destroy_uki += 1

# --- Second Scenario: Destroy all ushi units ---

turn_count_to_destroy_ushi = 0

current_uki_second_group = number_of_initial_uki_units
current_uki_first_group = number_of_initial_uki_units
current_ushi_group_1 = number_of_initial_ushi_units
current_ushi_group_2 = number_of_initial_ushi_units
total_ushi_units = number_of_initial_ushi_units * 2
total_uki_units = number_of_initial_uki_units * 2

while True:
    if current_ushi_group_2 - current_uki_first_group >= 0:
        current_ushi_group_2 -= current_uki_first_group
    else:
        current_ushi_group_1 = current_ushi_group_1 + current_ushi_group_2 - current_uki_first_group
        current_ushi_group_2 = 0

    if current_ushi_group_1 <= 0:
        break

    turn_count_to_destroy_ushi += 1

    total_uki_units -= current_ushi_group_1
    current_uki_first_group = -(-total_uki_units // 2)

    if total_uki_units <= 0:
        break

    turn_count_to_destroy_ushi += 1

minimum_turns_required = min(turn_count_to_destroy_uki, turn_count_to_destroy_ushi)
print(minimum_turns_required)