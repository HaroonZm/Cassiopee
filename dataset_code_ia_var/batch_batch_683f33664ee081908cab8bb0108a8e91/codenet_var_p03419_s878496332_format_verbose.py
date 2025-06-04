def calculate_inner_cells_of_grid():

    number_of_rows, number_of_columns = map(int, input().split())

    if number_of_rows == 1 and number_of_columns == 1:
        print(1)
        return

    if number_of_rows == 1:
        number_of_inner_cells = number_of_columns - 2
        print(number_of_inner_cells)
        return

    if number_of_columns == 1:
        number_of_inner_cells = number_of_rows - 2
        print(number_of_inner_cells)
        return

    number_of_inner_cells = (number_of_rows - 2) * (number_of_columns - 2)
    print(number_of_inner_cells)


if __name__ == "__main__":
    calculate_inner_cells_of_grid()