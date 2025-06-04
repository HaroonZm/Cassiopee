import sys

def read_input():
    return [line for line in sys.stdin]

def is_row_count_line(line):
    return len(line.strip()) == 1 and line.strip().isdigit()

def parse_row(line):
    return [int(x) for x in line.strip().split()]

def extract_matrix(lines, start, row_count):
    return [parse_row(lines[start + i]) for i in range(row_count)]

def find_min_index(row):
    if len(row) < 1:
        return 0
    return min_index_traverse(row)

def min_index_traverse(row):
    min_idx = 0
    for idx in range(len(row)):
        if row[idx] < row[min_idx]:
            min_idx = idx
    return min_idx

def scan_column_above(matrix, col, row_idx):
    max_val = matrix[row_idx][col]
    max_found = max_val
    for r in range(row_idx, -1, -1):
        if matrix[r][col] > max_found:
            max_found = matrix[r][col]
    return max_found

def scan_column_below(matrix, col, row_idx):
    max_val = matrix[row_idx][col]
    max_found = max_val
    for r in range(row_idx, len(matrix)):
        if matrix[r][col] > max_found:
            max_found = matrix[r][col]
    return max_found

def is_max_in_column(matrix, row_idx, col):
    max_above = scan_column_above(matrix, col, row_idx)
    max_below = scan_column_below(matrix, col, row_idx)
    return matrix[row_idx][col] == max(max_above, max_below)

def process_matrix(matrix):
    for i in range(len(matrix)):
        min_col = find_min_index(matrix[i])
        if is_max_in_column(matrix, i, min_col):
            output_value(matrix[i][min_col])
            return
    output_value(0)

def output_value(val):
    print(val)

def process_input_lines(lines):
    i = 0
    while i < len(lines):
        if is_row_count_line(lines[i]):
            row_count = int(lines[i])
            matrix = extract_matrix(lines, i + 1, row_count)
            process_matrix(matrix)
            i += row_count + 1
        else:
            i += 1

def main():
    lines = read_input()
    process_input_lines(lines)

main()