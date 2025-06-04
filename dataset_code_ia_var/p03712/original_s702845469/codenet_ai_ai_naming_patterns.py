row_count, col_count = map(int, input().split())
matrix_rows = [list(input()) for _ in range(row_count)]

for row_index in range(-1, row_count + 1):
    if row_index == -1 or row_index == row_count:
        print("#" * (col_count + 2))
    else:
        decorated_row = ["#"] + matrix_rows[row_index] + ["#"]
        print("".join(decorated_row))