from collections import defaultdict

def read_dimensions():
    return map(int, input().split())

def read_mass(H):
    return [input() for _ in range(H)]

def create_grid(H, W, value=0):
    return [[value for _ in range(W)] for _ in range(H)]

def process_row_indicators(mass, H, W):
    values_row = defaultdict(int)
    ind_row = create_grid(H, W, 0)
    ind = 0
    for i in range(H):
        ind = increment_ind(ind)
        for j in range(W):
            ind, ind_row[i][j], values_row = process_row_cell(mass, i, j, ind, ind_row, values_row)
    return ind_row, values_row

def increment_ind(ind):
    return ind + 1

def process_row_cell(mass, i, j, ind, ind_row, values_row):
    if is_black_cell(mass[i][j]):
        ind = increment_ind(ind)
    else:
        values_row = increment_value_dict(values_row, ind)
        ind_row[i][j] = ind
    return ind, ind_row[i][j], values_row

def is_black_cell(chr):
    return chr == '#'

def increment_value_dict(dct, key):
    dct[key] += 1
    return dct

def process_col_indicators(mass, H, W):
    values_col = defaultdict(int)
    ind_col = create_grid(H, W, 0)
    ind = 0
    for j in range(W):
        ind = increment_ind(ind)
        for i in range(H):
            ind, ind_col[i][j], values_col = process_col_cell(mass, i, j, ind, ind_col, values_col)
    return ind_col, values_col

def process_col_cell(mass, i, j, ind, ind_col, values_col):
    if is_black_cell(mass[i][j]):
        ind = increment_ind(ind)
    else:
        values_col = increment_value_dict(values_col, ind)
        ind_col[i][j] = ind
    return ind, ind_col[i][j], values_col

def compute_max_sum(H, W, ind_row, values_row, ind_col, values_col):
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = update_max(ans, ind_row, values_row, ind_col, values_col, i, j)
    return ans

def update_max(ans, ind_row, values_row, ind_col, values_col, i, j):
    val = values_row[ind_row[i][j]] + values_col[ind_col[i][j]] - 1
    return max(ans, val)

def main():
    H, W = read_dimensions()
    mass = read_mass(H)
    ind_row, values_row = process_row_indicators(mass, H, W)
    ind_col, values_col = process_col_indicators(mass, H, W)
    ans = compute_max_sum(H, W, ind_row, values_row, ind_col, values_col)
    print(ans)

main()