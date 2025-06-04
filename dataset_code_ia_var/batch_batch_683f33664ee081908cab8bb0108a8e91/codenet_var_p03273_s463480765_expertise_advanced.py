from sys import stdin

h, w = map(int, stdin.readline().split())
a = [stdin.readline().rstrip() for _ in range(h)]

rows_with_hash = [any(char == '#' for char in row) for row in a]
cols_with_hash = [any(row[j] == '#' for row in a) for j in range(w)]

filtered_rows = (
    ''.join(a[i][j] for j, keep_col in enumerate(cols_with_hash) if keep_col)
    for i, keep_row in enumerate(rows_with_hash) if keep_row
)

print('\n'.join(filtered_rows))