def get_input_string():
    return input()

def compute_length(s):
    return len(s)

def create_zero_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def chars_equal(s, i, t, j):
    return s[i] == t[j]

def fill_lcs_matrix(S, T, L):
    for i in range(len(S)):
        fill_matrix_row(S, T, L, i)

def fill_matrix_row(S, T, L, i):
    for j in range(len(T)):
        process_matrix_cell(S, T, L, i, j)

def process_matrix_cell(S, T, L, i, j):
    if chars_equal(S, i, T, j):
        set_lcs_value_match(L, i, j)
    else:
        set_lcs_value_nomatch(L, i, j)

def set_lcs_value_match(L, i, j):
    L[i+1][j+1] = L[i][j] + 1

def set_lcs_value_nomatch(L, i, j):
    L[i+1][j+1] = max(L[i][j+1], L[i+1][j], L[i+1][j+1])

def initialize_lcs_matrix(S, T):
    return create_zero_matrix(len(S)+1, len(T)+1)

def build_lcs(S, T, L):
    x = len(S)
    y = len(T)
    res = ''
    while lcs_while_condition(x, y):
        x, y, c = lcs_while_step(S, T, L, x, y)
        res += c
    return reverse_string(res)

def lcs_while_condition(x, y):
    return x*y

def lcs_while_step(S, T, L, x, y):
    if x > 0 and y > 0 and chars_equal(S, x-1, T, y-1):
        return x-1, y-1, S[x-1]
    else:
        if x > 0 and (y == 0 or L[x-1][y] > L[x][y-1]):
            return x-1, y, ''
        else:
            return x, y-1, ''

def reverse_string(s):
    return s[::-1]

def print_result(result):
    print(result)

def main():
    S = get_input_string()
    T = get_input_string()
    L = initialize_lcs_matrix(S, T)
    fill_lcs_matrix(S, T, L)
    lcs = build_lcs(S, T, L)
    print_result(lcs)

main()