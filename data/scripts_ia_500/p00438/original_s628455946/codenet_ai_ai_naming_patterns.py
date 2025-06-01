import sys
import copy

def main():
    input_line = sys.stdin.readline()
    while input_line.split() != ["0", "0"]:
        process_case(input_line)
        input_line = sys.stdin.readline()
    return

def process_case(input_line):
    field_dimensions = [int(value) for value in input_line.split()]
    blocked_count = int(sys.stdin.readline())
    blocked_cells = []
    for _ in range(blocked_count):
        blocked_input = sys.stdin.readline()
        blocked_coordinates = [int(value) for value in blocked_input.split()]
        blocked_cells.append(blocked_coordinates)
    print(calculate_paths(field_dimensions, blocked_cells))

def calculate_paths(field_dimensions, blocked_cells):
    path_counts = []
    for row_index in range(field_dimensions[1]):
        for col_index in range(field_dimensions[0]):
            if row_index == 0:
                if [col_index + 1, row_index + 1] in blocked_cells:
                    path_counts.append(0)
                elif col_index == 0:
                    path_counts.append(1)
                else:
                    path_counts.append(path_counts[col_index - 1])
            else:
                if [col_index + 1, row_index + 1] in blocked_cells:
                    path_counts[col_index] = 0
                elif col_index != 0:
                    path_counts[col_index] = path_counts[col_index - 1] + path_counts[col_index]
    return path_counts[-1]

if __name__ == "__main__":
    main()