import sys

def calculate_largest_square(grid_lines):
    max_square_size = 0
    numeric_grid = []
    for line in grid_lines:
        numeric_row = []
        for character in line:
            if character == '.':
                numeric_row.append(1)
            else:
                numeric_row.append(0)
        numeric_grid.append(numeric_row)

    previous_row_values = numeric_grid[0]
    for current_row_values in numeric_grid[1:]:
        for column_index, cell_value in enumerate(current_row_values[1:], start=1):
            if cell_value == 1:
                current_row_values[column_index] = min(
                    previous_row_values[column_index - 1],
                    previous_row_values[column_index],
                    current_row_values[column_index - 1]
                ) + 1
                if current_row_values[column_index] > max_square_size:
                    max_square_size = current_row_values[column_index]
        previous_row_values = current_row_values

    return max_square_size

def main(cli_arguments):
    while True:
        dimension = int(input())
        if dimension == 0:
            break
        input_grid = [input() for _ in range(dimension)]
        largest_square_result = calculate_largest_square(input_grid)
        print(largest_square_result)

if __name__ == '__main__':
    main(sys.argv[1:])