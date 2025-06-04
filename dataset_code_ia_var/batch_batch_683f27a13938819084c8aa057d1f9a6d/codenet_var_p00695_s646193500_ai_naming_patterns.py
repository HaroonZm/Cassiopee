import sys
if sys.version_info[0] >= 3: raw_input = input

def compute_max_rectangle_area(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    hist_matrix = [[0] * num_cols for _row in range(num_rows)]
    for row_idx in range(num_rows):
        consecutive_count = 0
        for col_idx in range(num_cols):
            if matrix[row_idx][col_idx] == 1:
                consecutive_count += 1
            else:
                consecutive_count = 0
            hist_matrix[row_idx][col_idx] = consecutive_count
    max_area = 0
    for col_idx in range(num_cols):
        for row_start in range(num_rows):
            min_height = float('inf')
            for row_end in range(row_start, num_rows):
                min_height = min(min_height, hist_matrix[row_end][col_idx])
                rectangle_area = min_height * (row_end - row_start + 1)
                max_area = max(max_area, rectangle_area)
    return max_area

if __name__ == '__main__':
    input_case_count = int(raw_input())
    try:
        for case_index in range(input_case_count):
            input_matrix = [[int(cell_value) for cell_value in raw_input().split()] for _ in range(5)]
            print(compute_max_rectangle_area(input_matrix))
            raw_input()
    except EOFError:
        pass