total_number_of_rows, total_number_of_columns, number_of_left_block_columns, number_of_top_block_rows = map(int, input().split())

for current_row_index in range(number_of_top_block_rows):
    
    left_block_segment = ['0'] * number_of_left_block_columns
    right_block_segment = ['1'] * (total_number_of_columns - number_of_left_block_columns)
    
    complete_row = ''.join(left_block_segment + right_block_segment)
    
    print(complete_row)

for current_row_index in range(total_number_of_rows - number_of_top_block_rows):
    
    left_block_segment = ['1'] * number_of_left_block_columns
    right_block_segment = ['0'] * (total_number_of_columns - number_of_left_block_columns)
    
    complete_row = ''.join(left_block_segment + right_block_segment)
    
    print(complete_row)