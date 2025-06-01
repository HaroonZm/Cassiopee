def main():
    
    number_of_rows = int(input())
    
    matrix = []
    for _ in range(number_of_rows):
        row_values = list(map(int, input().split()))
        matrix.append(row_values)
    
    columns_as_rows = []
    column_index = 0
    for _ in range(3):
        current_column_values = []
        for row_index in range(number_of_rows):
            current_column_values.append(matrix[row_index][column_index])
        column_index += 1
        columns_as_rows.append(current_column_values)
    
    unique_sums_per_row = [0] * number_of_rows
    for column_idx in range(3):
        for row_idx in range(number_of_rows):
            count_of_duplicates = 0
            for compare_idx in range(number_of_rows):
                if columns_as_rows[column_idx][row_idx] == columns_as_rows[column_idx][compare_idx]:
                    count_of_duplicates += 1
            if count_of_duplicates == 1:
                unique_sums_per_row[row_idx] += columns_as_rows[column_idx][row_idx]
    
    for row_index in range(number_of_rows):
        print(unique_sums_per_row[row_index])

if __name__ == "__main__":
    main()