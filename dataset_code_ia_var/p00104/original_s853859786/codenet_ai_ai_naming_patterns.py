while True:
    dimensions_input = list(map(int, input().split()))
    grid_height, grid_width = dimensions_input[0], dimensions_input[1]
    if grid_height == 0 and grid_width == 0:
        break

    grid_tiles = [input() for grid_row_index in range(grid_height)]
    current_row_index, current_col_index, step_counter = 0, 0, 0
    max_steps = grid_height * grid_width

    while True:
        current_tile = grid_tiles[current_row_index][current_col_index]

        if step_counter >= max_steps:
            print("LOOP")
            break

        if current_tile == ">":
            if current_col_index + 1 < grid_width:
                current_col_index += 1
            else:
                print(current_col_index, current_row_index)
                break

        elif current_tile == "<":
            if current_col_index - 1 >= 0:
                current_col_index -= 1
            else:
                print(current_col_index, current_row_index)
                break

        elif current_tile == "^":
            if current_row_index - 1 >= 0:
                current_row_index -= 1
            else:
                print(current_col_index, current_row_index)
                break

        elif current_tile == "v":
            if current_row_index + 1 < grid_height:
                current_row_index += 1
            else:
                print(current_col_index, current_row_index)
                break

        else:
            print(current_col_index, current_row_index)
            break

        step_counter += 1