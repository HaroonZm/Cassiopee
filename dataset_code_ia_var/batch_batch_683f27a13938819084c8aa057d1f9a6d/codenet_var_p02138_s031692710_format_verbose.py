def simulate_game(first_group_initial, second_group_initial, hoge_flag):
    
    first_group_reserve = 0
    second_group_reserve = 0
    turn_count = 0

    while True:

        if turn_count % 2 == 0 and hoge_flag == 0:
            # First player's turn, hoge == 0
            total_first_resources = first_group_initial + first_group_reserve

            remove_from_second_reserve = min(total_first_resources, second_group_reserve)
            second_group_reserve -= remove_from_second_reserve
            total_first_resources -= remove_from_second_reserve

            remove_from_second_initial = min(total_first_resources / 2, second_group_initial)
            second_group_initial -= remove_from_second_initial
            total_first_resources -= remove_from_second_initial * 2

            if second_group_initial > 0 and total_first_resources > 0:
                second_group_initial -= 1
                second_group_reserve += 1

        elif turn_count % 2 == 1 and hoge_flag == 0:
            # Second player's turn, hoge == 0
            total_second_resources = second_group_initial + second_group_reserve

            remove_from_first_initial = min(total_second_resources, first_group_initial)
            first_group_initial -= remove_from_first_initial
            first_group_reserve += remove_from_first_initial
            total_second_resources -= remove_from_first_initial

            remove_from_first_reserve = min(total_second_resources, first_group_reserve)
            first_group_reserve -= remove_from_first_reserve
            total_second_resources -= remove_from_first_reserve

        elif turn_count % 2 == 0 and hoge_flag == 1:
            # First player's turn, hoge == 1
            total_first_resources = first_group_initial + first_group_reserve

            move_to_second_reserve = min(total_first_resources, second_group_initial)
            second_group_initial -= move_to_second_reserve
            second_group_reserve += move_to_second_reserve
            total_first_resources -= move_to_second_reserve

            remove_from_second_reserve = min(total_first_resources, second_group_reserve)
            second_group_reserve -= remove_from_second_reserve
            total_first_resources -= remove_from_second_reserve

        else:
            # Second player's turn, hoge == 1
            total_second_resources = second_group_initial + second_group_reserve

            remove_from_first_reserve = min(total_second_resources, first_group_reserve)
            first_group_reserve -= remove_from_first_reserve
            total_second_resources -= remove_from_first_reserve

            remove_from_first_initial = min(total_second_resources / 2, first_group_initial)
            first_group_initial -= remove_from_first_initial
            total_second_resources -= remove_from_first_initial * 2

            if first_group_initial > 0 and total_second_resources > 0:
                first_group_initial -= 1
                first_group_reserve += 1

        if first_group_initial + first_group_reserve <= 0 or second_group_initial + second_group_reserve <= 0:
            return turn_count

        turn_count += 1


if __name__ == "__main__":

    user_input_first_group, user_input_second_group = map(int, raw_input().split())

    minimum_turns_case_0 = simulate_game(user_input_first_group, user_input_second_group, 0)
    minimum_turns_case_1 = simulate_game(user_input_first_group, user_input_second_group, 1)

    print min(minimum_turns_case_0, minimum_turns_case_1)