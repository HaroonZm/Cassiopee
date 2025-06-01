while True:
    board_row_1 = input()
    if board_row_1 == "0":
        break
    board_row_2 = input()
    board_row_3 = input()

    winning_symbol = "NA"

    # Check rows for a win
    if board_row_1[0] != "+" and board_row_1[0] == board_row_1[1] == board_row_1[2]:
        winning_symbol = board_row_1[0]
    elif board_row_2[0] != "+" and board_row_2[0] == board_row_2[1] == board_row_2[2]:
        winning_symbol = board_row_2[0]
    elif board_row_3[0] != "+" and board_row_3[0] == board_row_3[1] == board_row_3[2]:
        winning_symbol = board_row_3[0]

    # Check columns for a win
    elif board_row_1[0] != "+" and board_row_1[0] == board_row_2[0] == board_row_3[0]:
        winning_symbol = board_row_1[0]
    elif board_row_1[1] != "+" and board_row_1[1] == board_row_2[1] == board_row_3[1]:
        winning_symbol = board_row_1[1]
    elif board_row_1[2] != "+" and board_row_1[2] == board_row_2[2] == board_row_3[2]:
        winning_symbol = board_row_1[2]

    # Check diagonals for a win
    elif board_row_1[0] != "+" and board_row_1[0] == board_row_2[1] == board_row_3[2]:
        winning_symbol = board_row_1[0]
    elif board_row_1[2] != "+" and board_row_1[2] == board_row_2[1] == board_row_3[0]:
        winning_symbol = board_row_1[2]

    print(winning_symbol)