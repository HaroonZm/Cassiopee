num_rows = 40
num_cols = 40
threshold = 5

print(num_rows)
matrix = [[] for row_idx in range(num_rows)]
for row_idx in range(num_rows):
    for col_idx in range(num_cols):
        if row_idx == col_idx:
            matrix[row_idx].append("N")
        elif row_idx < threshold:
            if col_idx >= threshold:
                matrix[row_idx].append("Y")
            else:
                matrix[row_idx].append("Y")
        else:
            if col_idx >= threshold:
                matrix[row_idx].append("N")
            else:
                matrix[row_idx].append("Y")

for row in matrix:
    print("".join(row))