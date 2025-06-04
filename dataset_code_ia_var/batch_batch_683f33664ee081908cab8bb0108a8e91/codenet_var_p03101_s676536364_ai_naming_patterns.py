def calculate_remaining_cells():
    total_rows, total_columns = map(int, input().split())
    remove_rows, remove_columns = map(int, input().split())
    remaining_cells = (total_rows - remove_rows) * (total_columns - remove_columns)
    print(remaining_cells)

calculate_remaining_cells()