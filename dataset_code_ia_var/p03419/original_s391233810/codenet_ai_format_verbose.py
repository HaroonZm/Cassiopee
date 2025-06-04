number_of_rows, number_of_columns = map(int, input().split())

if number_of_rows == 1 and number_of_columns == 1:
    
    print(1)

elif number_of_rows == 1 or number_of_columns == 1:
    
    largest_dimension = max(number_of_rows, number_of_columns)
    number_of_internal_cells = largest_dimension - 2
    print(number_of_internal_cells)

else:
    
    number_of_internal_rows = number_of_rows - 2
    number_of_internal_columns = number_of_columns - 2
    total_internal_cells = number_of_internal_rows * number_of_internal_columns
    print(total_internal_cells)