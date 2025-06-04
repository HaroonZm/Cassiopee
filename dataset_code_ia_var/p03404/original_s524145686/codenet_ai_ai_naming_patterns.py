def run_procedure():
    num_white, num_black = [int(item) for item in input().split()]

    grid_width = 100
    grid_height = 50

    row_template = [0] * grid_width
    grid_matrix = [list(row_template) for _ in range(grid_height)]

    num_white -= 1

    if num_white > 0:
        num_black -= 1

        for row_idx in range(0, grid_height, 2):
            for col_idx in range(0, grid_width, 2):
                grid_matrix[row_idx][col_idx + 1] = 1
                grid_matrix[row_idx + 1][col_idx] = 1
                grid_matrix[row_idx + 1][col_idx + 1] = 1
                num_white -= 1
                if num_white == 0:
                    break
            if num_white == 0:
                break

    if num_black > 0:
        for row_idx in range(24, grid_height, 2):
            for col_idx in range(0, grid_width, 2):
                grid_matrix[row_idx][col_idx] = 1
                num_black -= 1
                if num_black == 0:
                    break
            if num_black == 0:
                break

    print(f'{grid_height} {grid_width}')
    for row in grid_matrix:
        print(''.join(['#' if cell_value else '.' for cell_value in row]))

if __name__ == '__main__':
    run_procedure()