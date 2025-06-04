while True:

    number_of_players, total_stones_at_start = map(int, input().split())

    if number_of_players == 0 and total_stones_at_start == 0:
        break

    stones_held_by_each_player = [0] * number_of_players
    stones_in_table = total_stones_at_start

    while True:

        game_completed = False

        for current_player_index in range(number_of_players):

            if stones_in_table > 0:
                stones_held_by_each_player[current_player_index] += 1
                stones_in_table -= 1

                if (stones_in_table == 0 and
                    stones_held_by_each_player[current_player_index] == total_stones_at_start):

                    print(current_player_index)
                    game_completed = True
                    break

            else:
                stones_in_table += stones_held_by_each_player[current_player_index]
                stones_held_by_each_player[current_player_index] = 0

        if game_completed:
            break