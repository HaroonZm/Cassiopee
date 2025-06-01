def read_input():
    return map(int, raw_input().split())

def should_break(k):
    return k == 0

def initialize_grid(n):
    return [['.' for _ in range(n)] for _ in range(n)]

def compute_k_binary(k, n):
    return bin(k - 1)[2:].zfill(n // 2)

def invalid_conditions(n, k_bin):
    return n % 2 == 1 or len(k_bin) > n // 2

def fill_first_row(A, k_bin, n):
    for i in range(n // 2):
        if k_bin[i] == '1':
            A[0][i * 2] = 'E'
            A[0][i * 2 + 1] = 'E'

def count_similar_neighbors_in_row(A, i, j, n):
    cnt = 0
    if i > 0 and A[i][j] == A[i - 1][j]:
        cnt += 1
    if j > 0 and A[i][j] == A[i][j - 1]:
        cnt += 1
    if j < n - 1 and A[i][j] == A[i][j + 1]:
        cnt += 1
    return cnt

def fill_row(A, i, n):
    for j in range(n):
        cnt = count_similar_neighbors_in_row(A, i, j, n)
        if cnt == 1:
            A[i + 1][j] = A[i][j]
        elif A[i][j] == '.':
            A[i + 1][j] = 'E'
        else:
            A[i + 1][j] = '.'

def print_row(row):
    print(''.join(row))

def print_no_and_continue():
    print("No\n")

def main_loop():
    while True:
        n, k = read_input()
        if should_break(k):
            break
        A = initialize_grid(n)
        k_bin = compute_k_binary(k, n)
        if invalid_conditions(n, k_bin):
            print_no_and_continue()
            continue
        fill_first_row(A, k_bin, n)
        print_row(A[0])
        for i in range(n - 1):
            fill_row(A, i, n)
            print_row(A[i + 1])
        print()

main_loop()