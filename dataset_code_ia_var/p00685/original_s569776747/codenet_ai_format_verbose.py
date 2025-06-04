def count_board_arrangements_for_concentration_game():
    def generate_arrangements(current_tile_number):
        global total_arrangements

        if current_tile_number == 9:
            total_arrangements += 1
            return

        for row in range(4):
            for column in range(4):
                if board_grid[row][column] != 0:
                    continue

                board_grid[row][column] = current_tile_number

                for neighbor_index in range(4):
                    delta_x = input_positions[neighbor_index * 2]
                    delta_y = input_positions[neighbor_index * 2 + 1]
                    new_column = column + delta_x
                    new_row = row + delta_y

                    if (
                        new_column < 0
                        or new_column >= 4
                        or new_row < 0
                        or new_row >= 4
                        or board_grid[new_row][new_column] != 0
                    ):
                        continue

                    board_grid[new_row][new_column] = current_tile_number
                    generate_arrangements(current_tile_number + 1)
                    board_grid[new_row][new_column] = 0

                board_grid[row][column] = 0
                return

    while True:
        input_positions = list(map(int, input().split()))
        if len(input_positions) == 1:
            break

        board_grid = [ [0 for _ in range(4)] for _ in range(4) ]
        total_arrangements = 0
        board_grid[0][0] = 1

        for neighbor_index in range(4):
            initial_x = input_positions[neighbor_index * 2]
            initial_y = input_positions[neighbor_index * 2 + 1]
            if initial_x >= 0 and initial_y >= 0:
                board_grid[initial_y][initial_x] = 1
                generate_arrangements(2)
                board_grid[initial_y][initial_x] = 0

        print(total_arrangements)