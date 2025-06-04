def read_input_to_int_list():
    return list(map(int, input().split()))

def main():
    row_count, col_count = read_input_to_int_list()
    max_distance = 0
    grid = [input() for _ in range(row_count)]
    for iterate_direction in range(2):
        left_b_index_list = [0] * row_count
        right_b_index_list = [0] * row_count
        left_rows_with_b = []
        right_rows_with_b = []
        for row_index in range(row_count):
            left_b_position = grid[row_index].find("B")
            right_b_position = grid[row_index].rfind("B")
            left_b_index_list[row_index] = left_b_position
            right_b_index_list[row_index] = right_b_position
            if left_b_position >= 0:
                left_rows_with_b.append(row_index)
            if right_b_position >= 0:
                right_rows_with_b.append(row_index)
        for left_row in left_rows_with_b:
            for right_row in right_rows_with_b:
                horizontal_diff = abs(left_b_index_list[left_row] - right_b_index_list[right_row])
                vertical_diff = abs(left_row - right_row)
                max_distance = max(max_distance, horizontal_diff + vertical_diff)
        if iterate_direction == 0:
            grid = ["".join(column) for column in zip(*grid)]
            row_count, col_count = col_count, row_count
    print(max_distance)

main()