while True:
    
    height, width = map(int, raw_input().split())
    
    if height == 0 and width == 0:
        break
    
    row_indices = range(height)
    
    column_max_positions = [0] * (height + 1)
    max_rectangle_widths = column_max_positions[:]
    
    previous_row_counts = [0] * width
    
    for current_row_index in row_indices:
        
        current_input_line = raw_input()
        current_row_counts = [0] * width
        
        previous_count = -1
        
        column_last_positions = [-1] * (height + 1)
        
        for current_column_index in range(width):
            
            cell_char = current_input_line[current_column_index]
            
            if cell_char == "*":
                consecutive_empty_cells = 0
            elif cell_char == ".":
                consecutive_empty_cells = previous_row_counts[current_column_index] + 1
            
            current_row_counts[current_column_index] = consecutive_empty_cells
            
            if consecutive_empty_cells > previous_count:
                for fill_index in range(previous_count + 1, consecutive_empty_cells + 1):
                    column_last_positions[fill_index] = current_column_index
            
            elif consecutive_empty_cells < previous_count:
                for fill_index in range(consecutive_empty_cells + 1, previous_count + 1):
                    max_rectangle_widths[fill_index] = max(
                        max_rectangle_widths[fill_index],
                        current_column_index - column_last_positions[fill_index]
                    )
                    column_last_positions[fill_index] = -1
            
            previous_count = consecutive_empty_cells
        
        for fill_index in range(1, previous_count + 1):
            if column_last_positions[fill_index] >= 0:
                max_rectangle_widths[fill_index] = max(
                    max_rectangle_widths[fill_index],
                    width - column_last_positions[fill_index]
                )
        
        previous_row_counts = current_row_counts[:]
    
    max_area = max([
        width_value * height_value
        for height_value, width_value in enumerate(max_rectangle_widths)
    ])
    
    print max_area