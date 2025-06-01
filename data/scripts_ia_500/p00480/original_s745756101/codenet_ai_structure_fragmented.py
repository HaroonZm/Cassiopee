def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def create_2d_list(rows, cols, value=0):
    return [[value]*cols for _ in range(rows)]

def initialize_dp_array(N, max_value, first_value):
    d = create_2d_list(N-1, max_value+1)
    d[0][first_value] = 1
    return d

def update_dp_row(d, i, max_value, current_val):
    for j in range(max_value+1):
        left_index = j + current_val
        right_index = j - current_val
        left_count = d[i-1][left_index] if left_index <= max_value else 0
        right_count = d[i-1][right_index] if right_index >= 0 else 0
        d[i][j] = left_count + right_count

def compute_dp(d, N, a, max_value):
    for i in range(1, N-1):
        update_dp_row(d, i, max_value, a[i])

def main():
    N = read_int()
    a = read_int_list()
    max_value = 20
    d = initialize_dp_array(N, max_value, a[0])
    compute_dp(d, N, a, max_value)
    print(d[N-2][a[N-1]])

main()