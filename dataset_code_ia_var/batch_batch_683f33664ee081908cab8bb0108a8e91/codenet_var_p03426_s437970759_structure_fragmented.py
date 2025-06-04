def read_dimensions():
    return list(map(int, input().split()))

def create_index_list(size):
    return [(0, 0) for _ in range(size + 1)]

def read_column():
    return list(map(int, input().split()))

def fill_row_indices(h, w, index):
    for i in range(1, h + 1):
        fill_row(i, w, index)
    return index

def fill_row(i, w, index):
    col = read_column()
    fill_cells(i, w, col, index)

def fill_cells(i, w, col, index):
    for j in range(1, w + 1):
        set_index(col[j - 1], i, j, index)

def set_index(value, row, col, index):
    index[value] = (row, col)

def create_memo(size):
    return [0 for _ in range(size + 1)]

def fill_memo(h, w, d, index, memo):
    for l in range(1, h * w + 1 - d):
        update_memo(l, d, index, memo, h, w)
    return memo

def update_memo(l, d, index, memo, h, w):
    val1 = l
    val2 = l + d
    y_diff = abs(index[val2][0] - index[val1][0])
    x_diff = abs(index[val2][1] - index[val1][1])
    memo[val2] = memo[val1] + y_diff + x_diff

def read_queries():
    return int(input())

def process_queries(q, memo):
    for _ in range(q):
        l, r = read_query()
        print(calc_result(l, r, memo))

def read_query():
    return map(int, input().split())

def calc_result(l, r, memo):
    return memo[r] - memo[l]

def main():
    h, w, d = read_dimensions()
    index = create_index_list(h * w)
    fill_row_indices(h, w, index)
    memo = create_memo(h * w)
    fill_memo(h, w, d, index, memo)
    q = read_queries()
    process_queries(q, memo)

main()