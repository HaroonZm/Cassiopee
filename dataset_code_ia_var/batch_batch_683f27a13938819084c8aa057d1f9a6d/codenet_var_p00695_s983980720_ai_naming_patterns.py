import sys
if sys.version_info[0] >= 3:
    raw_input = input

def find_max_rectangle_area(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    row_run_lengths = [[0] * col_count for _ in range(row_count)]
    for row_idx in range(row_count):
        consecutive_count = 0
        for col_idx in range(col_count):
            if matrix[row_idx][col_idx] == 1:
                consecutive_count += 1
            else:
                consecutive_count = 0
            row_run_lengths[row_idx][col_idx] = consecutive_count
    max_area = 0
    for col_idx in range(col_count):
        for row_start in range(row_count):
            min_run_length = float('inf')
            for row_end in range(row_start, row_count):
                min_run_length = min(min_run_length, row_run_lengths[row_end][col_idx])
                current_area = min_run_length * (row_end - row_start + 1)
                if current_area > max_area:
                    max_area = current_area
    return max_area

if __name__ == '__main__':
    test_case_count = int(raw_input())
    try:
        for test_case_idx in range(test_case_count):
            input_matrix = [[int(cell_value) for cell_value in raw_input().split()] for _ in range(5)]
            print(find_max_rectangle_area(input_matrix))
            raw_input()
    except EOFError:
        pass