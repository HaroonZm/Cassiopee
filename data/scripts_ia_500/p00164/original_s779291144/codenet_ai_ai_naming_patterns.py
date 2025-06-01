while True:
    number_of_players = int(input())
    if number_of_players == 0:
        break
    player_moves = list(map(int, input().split()))

    ohajiki_pieces = 32
    turn_counter = 0
    while ohajiki_pieces != 0:
        remainder_pieces = (ohajiki_pieces - 1) % 5
        ohajiki_pieces -= remainder_pieces
        print(ohajiki_pieces)

        current_player_move = player_moves[turn_counter % number_of_players]
        ohajiki_pieces -= current_player_move
        if ohajiki_pieces < 0:
            ohajiki_pieces = 0
        print(ohajiki_pieces)
        turn_counter += 1