def read_input():
    return int(input())

def read_grid(N):
    return [list(input()) for _ in range(N)]

def transpose(grid):
    return [list(row) for row in zip(*grid)]

def get_row(grid, index):
    return grid[index]

def get_column(transposed, index):
    return transposed[index]

def rotate_column(col, i):
    return col[i:] + col[:i]

def compare_rows(row1, row2):
    return row1 == row2

def check_rotation(S, T, i, N):
    for j in range(N):
        s_row = get_row(S, (i + j - N) % N)
        t_col = get_column(T, j)
        rotated_col = rotate_column(t_col, i)
        if not compare_rows(s_row, rotated_col):
            return False
    return True

def count_valid_rotations(S, T, N):
    count = 0
    for i in range(N):
        if check_rotation(S, T, i, N):
            count += 1
    return count

def compute_result(count, N):
    return count * N

def main():
    N = read_input()
    S = read_grid(N)
    T = transpose(S)
    count = count_valid_rotations(S, T, N)
    result = compute_result(count, N)
    print(result)

main()