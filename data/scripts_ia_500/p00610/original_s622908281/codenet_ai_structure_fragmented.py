def read_input():
    line = raw_input()
    return list(map(int, line.split()))

def should_break(N):
    return N == 0

def is_invalid(N, K):
    return N % 2 != 0 or K > 2 ** (N // 2)

def initialize_array_A(N):
    return [0 for _ in range(N)]

def decrement_K(K):
    return K - 1

def calculate_power(base, exp):
    return base ** exp

def fill_A_with_K(A, N, K):
    n = N // 2
    for i in range(1, n + 1):
        power_val = calculate_power(2, n - i)
        val = K // power_val
        A[2 * (i - 1)] = val
        A[2 * (i - 1) + 1] = val
        K %= power_val

def initialize_B(N):
    size = N + 2
    return [[-1 for _ in range(size)] for _ in range(size)]

def copy_A_to_B_row(B, A, N):
    for j in range(1, N + 1):
        B[1][j] = A[j - 1]

def check_equality(B, i, j, offset_i, offset_j):
    return B[i][j] == B[i + offset_i][j + offset_j]

def sum_equals(B, i, j):
    left = check_equality(B, i, j, 0, -1)
    right = check_equality(B, i, j, 0, 1)
    up = check_equality(B, i, j, -1, 0)
    return left + right + up

def checkback(B, i, j):
    samesum = sum_equals(B, i, j)
    if samesum == 2:
        return int(not B[i][j])
    else:
        return B[i][j]

def fill_B_rows(B, N):
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            B[i][j] = checkback(B, i - 1, j)

def convert_B_row_to_string(B_row):
    result = ""
    for val in B_row:
        if val == 0:
            result += '.'
        elif val == 1:
            result += 'E'
    return result

def print_B(B, N):
    for i in range(1, N + 1):
        row_values = B[i][1:N + 1]
        row_string = convert_B_row_to_string(row_values)
        print row_string

def print_newline():
    print "\n",

def main_loop():
    while True:
        N, K = read_input()
        if should_break(N):
            break
        if is_invalid(N, K):
            print "No\n"
            continue
        A = initialize_array_A(N)
        K = decrement_K(K)
        fill_A_with_K(A, N, K)
        B = initialize_B(N)
        copy_A_to_B_row(B, A, N)
        fill_B_rows(B, N)
        print_B(B, N)
        print_newline()

main_loop()