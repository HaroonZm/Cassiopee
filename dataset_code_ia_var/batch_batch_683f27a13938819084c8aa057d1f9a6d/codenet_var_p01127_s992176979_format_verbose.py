def find_valid_rectangle(grid_data, rectangles_boundaries):
    
    for rectangle_char, (row_min, col_min, row_max, col_max) in rectangles_boundaries.items():
        
        is_current_rectangle_valid = True
        
        for current_row in range(row_min, row_max + 1):
            
            for current_col in range(col_min, col_max + 1):
                
                grid_cell = grid_data[current_row][current_col]
                
                if not (grid_cell == rectangle_char or grid_cell == "*"):
                    
                    is_current_rectangle_valid = False
                    
        if is_current_rectangle_valid:
            return rectangle_char
            
    return "-"


def verify_rectangles_safety(grid_data, rectangles_boundaries):
    
    while len(rectangles_boundaries) > 0:
        
        rectangle_to_remove = find_valid_rectangle(grid_data, rectangles_boundaries)
        
        if rectangle_to_remove == "-":
            
            print "SUSPICIOUS"
            return
            
        else:
            starting_row, starting_col, ending_row, ending_col = rectangles_boundaries[rectangle_to_remove]
            
            for row in range(starting_row, ending_row + 1):
                
                for col in range(starting_col, ending_col + 1):
                    
                    grid_data[row][col] = "*"
            
            del rectangles_boundaries[rectangle_to_remove]
            
    print "SAFE"


number_of_test_cases = int(raw_input())

for test_case_index in range(number_of_test_cases):
    
    num_rows, num_cols = map(int, raw_input().split())
    
    grid_data = [ ["-"] * num_cols for _ in range(num_rows) ]
    
    rectangles_boundaries = {}
    
    for current_row_index in range(num_rows):
        
        input_row_string = raw_input()
        
        for current_col_index in range(num_cols):
            
            current_character = input_row_string[current_col_index]
            grid_data[current_row_index][current_col_index] = current_character
            
            if current_character not in rectangles_boundaries:
                
                rectangles_boundaries[current_character] = (
                    current_row_index, current_col_index,
                    current_row_index, current_col_index
                )
                
            else:
                prev_row_min, prev_col_min, prev_row_max, prev_col_max = rectangles_boundaries[current_character]
                
                rectangles_boundaries[current_character] = (
                    min(prev_row_min, current_row_index),
                    min(prev_col_min, current_col_index),
                    max(prev_row_max, current_row_index),
                    max(prev_col_max, current_col_index)
                )
    
    verify_rectangles_safety(grid_data, rectangles_boundaries)