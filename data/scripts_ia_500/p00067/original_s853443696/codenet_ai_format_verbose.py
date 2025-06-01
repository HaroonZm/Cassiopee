def fill_coordinates_and_mark_visited(x_coordinate, y_coordinate, game_board):

    game_board[y_coordinate][x_coordinate] = 2

    adjacent_points = [
        [y_coordinate, x_coordinate + 1],
        [y_coordinate, x_coordinate - 1],
        [y_coordinate + 1, x_coordinate],
        [y_coordinate - 1, x_coordinate]
    ]

    if y_coordinate == 0:
        adjacent_points.remove([y_coordinate - 1, x_coordinate])
    elif y_coordinate == 11:
        adjacent_points.remove([y_coordinate + 1, x_coordinate])

    if x_coordinate == 0:
        adjacent_points.remove([y_coordinate, x_coordinate - 1])
    elif x_coordinate == 11:
        adjacent_points.remove([y_coordinate, x_coordinate + 1])

    for point in adjacent_points:
        if game_board[point[0]][point[1]] == 1:
            game_board = fill_coordinates_and_mark_visited(point[1], point[0], game_board)

    return game_board


while True:
    try:
        islands_grid = [list(map(int, list(input()))) for _ in range(12)]

        number_of_islands = 0

        for y_index in range(12):
            for x_index in range(12):
                if islands_grid[y_index][x_index] == 1:
                    islands_grid = fill_coordinates_and_mark_visited(x_index, y_index, islands_grid)
                    number_of_islands += 1

        print(number_of_islands)

        input()  # wait for next input set
    except:
        break