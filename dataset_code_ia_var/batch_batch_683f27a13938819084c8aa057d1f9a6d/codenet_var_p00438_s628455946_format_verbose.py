import sys
import copy

def main():
    current_input_line = sys.stdin.readline()
    
    while current_input_line.split() != ["0", "0"]:
        process_single_case(current_input_line)
        current_input_line = sys.stdin.readline()
    return

def process_single_case(case_input_line):
    # Parse field dimensions from input
    field_dimensions = [int(number) for number in case_input_line.split()]
    
    # Read the number of blocked positions
    blocked_positions_count = int(sys.stdin.readline())
    blocked_positions_list = []
    
    for blocked_index in range(blocked_positions_count):
        blocked_position_line = sys.stdin.readline()
        blocked_position_coordinates = [int(number) for number in blocked_position_line.split()]
        blocked_positions_list.append(blocked_position_coordinates)
    
    result_number_of_paths = calculate_number_of_paths(field_dimensions, blocked_positions_list)
    
    print(result_number_of_paths)

def calculate_number_of_paths(field_dimensions, blocked_positions):
    width_of_field = field_dimensions[0]     # Number of columns
    height_of_field = field_dimensions[1]    # Number of rows
    
    dynamic_path_counts = []
    
    for row_index in range(height_of_field):
        for column_index in range(width_of_field):
            
            current_cell_coordinates = [column_index + 1, row_index + 1]
            
            if row_index == 0:
                if current_cell_coordinates in blocked_positions:
                    dynamic_path_counts.append(0)
                elif column_index == 0:
                    dynamic_path_counts.append(1)
                else:
                    dynamic_path_counts.append(dynamic_path_counts[column_index - 1])
            else:
                if current_cell_coordinates in blocked_positions:
                    dynamic_path_counts[column_index] = 0
                elif column_index != 0:
                    dynamic_path_counts[column_index] = (
                        dynamic_path_counts[column_index - 1] + dynamic_path_counts[column_index]
                    )
    
    if dynamic_path_counts:
        return dynamic_path_counts[-1]
    else:
        return 0

if __name__ == "__main__":
    main()