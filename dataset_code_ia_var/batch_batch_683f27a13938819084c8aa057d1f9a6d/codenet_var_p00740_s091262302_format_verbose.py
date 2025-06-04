def main():
    while True:
        user_input = input()
        splitted_input = user_input.split(" ")
        
        for position in range(len(splitted_input)):
            splitted_input[position] = int(splitted_input[position])

        if splitted_input == [0, 0]:
            return

        number_of_players = splitted_input[0]
        total_stones = splitted_input[1]
        print(find_winner_player_index(number_of_players, total_stones))


def find_winner_player_index(number_of_players, total_stones):
    stones_held_by_each_player = [0 for _ in range(number_of_players)]

    while True:
        for current_player_index in range(number_of_players):

            if total_stones != 0:
                total_stones -= 1
                stones_held_by_each_player[current_player_index] += 1

                if total_stones == 0:
                    zero_stone_players_count = 0

                    for stones in stones_held_by_each_player:
                        if stones == 0:
                            zero_stone_players_count += 1

                    if zero_stone_players_count == number_of_players - 1:
                        return current_player_index

            else:
                total_stones = stones_held_by_each_player[current_player_index]
                stones_held_by_each_player[current_player_index] = 0

main()