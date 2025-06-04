def main():
    for input_line in iter(input, '0 0'):
        width, height = map(int, input_line.split())
        dp_matrix = [[[1, 0, 1, 0] for _ in range(height)] for _ in range(width)]
        for x in range(1, width):
            for y in range(1, height):
                prev_row_value_a, prev_row_value_b = dp_matrix[x - 1][y][0:2]
                prev_col_value_c, prev_col_value_d = dp_matrix[x][y - 1][2:]
                dp_matrix[x][y] = [prev_col_value_d, prev_row_value_a + prev_row_value_b, prev_row_value_b, prev_col_value_c + prev_col_value_d]
        result = (sum(dp_matrix[width - 2][height - 1][0:2]) + sum(dp_matrix[width - 1][height - 2][2:])) % 100000
        print(result)
if __name__ == '__main__':
    main()