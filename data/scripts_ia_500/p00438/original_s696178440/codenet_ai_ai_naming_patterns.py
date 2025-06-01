import sys
import copy

def main_loop():
    input_line = sys.stdin.readline()
    while input_line.split() != ["0", "0"]:
        process_case(input_line)
        input_line = sys.stdin.readline()

def process_case(line_str):
    field_size = [int(value) for value in line_str.split()]
    obstacle_count = int(sys.stdin.readline())
    obstacle_positions = []
    for _ in range(obstacle_count):
        position_line = sys.stdin.readline()
        position = [int(value) for value in position_line.split()]
        obstacle_positions.append(position)
    print(calculate_paths(field_size, obstacle_positions))

def calculate_paths(field_dimensions, obstacles):
    path_counts = []
    width = field_dimensions[0]
    height = field_dimensions[1]
    for row_index in range(height):
        for col_index in range(width):
            current_position = [col_index + 1, row_index + 1]
            if row_index == 0:
                if current_position in obstacles:
                    path_counts.append(0)
                else:
                    if col_index == 0:
                        path_counts.append(1)
                    else:
                        path_counts.append(path_counts[col_index - 1])
            else:
                if current_position in obstacles:
                    path_counts[col_index] = 0
                else:
                    if col_index != 0:
                        path_counts[col_index] = path_counts[col_index - 1] + path_counts[col_index]
    return path_counts[-1]

if __name__ == "__main__":
    main_loop()