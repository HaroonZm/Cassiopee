first_player_initial_attack, second_player_initial_attack = map(int, input().split())

minimum_turns_strategy_one = 0

first_player_current_attack = first_player_initial_attack
second_player_current_attack = second_player_initial_attack

first_player_remaining_health = first_player_initial_attack * 2
second_player_remaining_health = second_player_initial_attack * 2

while True:

    # First player attacks second player
    second_player_remaining_health -= first_player_current_attack
    if second_player_remaining_health <= 0:
        break
    else:
        minimum_turns_strategy_one += 1
        if second_player_remaining_health < second_player_current_attack:
            second_player_current_attack = second_player_remaining_health

    # Second player attacks first player
    first_player_remaining_health -= second_player_current_attack
    if first_player_remaining_health <= 0:
        break
    else:
        minimum_turns_strategy_one += 1
        if first_player_remaining_health < first_player_current_attack:
            first_player_current_attack = first_player_remaining_health

result_strategy_one = minimum_turns_strategy_one

first_player_current_attack = first_player_initial_attack
second_player_current_attack = second_player_initial_attack

minimum_turns_strategy_two = 0

first_player_remaining_health = first_player_initial_attack * 2
second_player_remaining_health = second_player_initial_attack * 2

while True:

    # First player attacks second player
    second_player_remaining_health -= first_player_current_attack
    if second_player_remaining_health <= 0:
        break
    else:
        minimum_turns_strategy_two += 1
        if second_player_remaining_health < second_player_current_attack and first_player_initial_attack < second_player_initial_attack:
            second_player_current_attack = second_player_remaining_health
        elif second_player_remaining_health < second_player_current_attack and first_player_initial_attack > second_player_initial_attack:
            if second_player_remaining_health % 2 == 0:
                second_player_current_attack = second_player_remaining_health // 2
            else:
                second_player_current_attack = second_player_remaining_health // 2 + 1

    # Second player attacks first player
    first_player_remaining_health -= second_player_current_attack
    if first_player_remaining_health <= 0:
        break
    else:
        minimum_turns_strategy_two += 1
        if first_player_remaining_health < first_player_current_attack and first_player_initial_attack > second_player_initial_attack:
            first_player_current_attack = first_player_remaining_health
        elif first_player_remaining_health < first_player_current_attack and first_player_initial_attack < second_player_initial_attack:
            if first_player_remaining_health % 2 == 0:
                first_player_current_attack = first_player_remaining_health // 2
            else:
                first_player_current_attack = first_player_remaining_health // 2 + 1

if result_strategy_one < minimum_turns_strategy_two:
    print(result_strategy_one)
else:
    print(minimum_turns_strategy_two)