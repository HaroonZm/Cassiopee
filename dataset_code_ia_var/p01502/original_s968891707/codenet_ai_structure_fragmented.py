def read_int():
    return int(raw_input())

def read_line():
    return raw_input()

def split_line(line):
    return line.split()

def map_ints(strs):
    return map(int, strs)

def read_matrix_row():
    line = read_line()
    strs = split_line(line)
    row = map_ints(strs)
    return row

def read_matrix(n):
    mat = []
    for i in xrange(n):
        row = read_matrix_row()
        mat.append(row)
    return mat

def get_min(a, b):
    return min(a, b)

def accumulate_ans(ans, val):
    return ans + val

def calc_pair_sum(C, i, j):
    return get_min(C[i][j], C[j][i])

def loop_j(C, i, n):
    ans = 0
    for j in xrange(i + 1, n):
        pair_sum = calc_pair_sum(C, i, j)
        ans = accumulate_ans(ans, pair_sum)
    return ans

def loop_i(C, n):
    total = 0
    for i in xrange(n):
        ans_i = loop_j(C, i, n)
        total = accumulate_ans(total, ans_i)
    return total

def main():
    N = read_int()
    C = read_matrix(N)
    ans = loop_i(C, N)
    print ans

main()