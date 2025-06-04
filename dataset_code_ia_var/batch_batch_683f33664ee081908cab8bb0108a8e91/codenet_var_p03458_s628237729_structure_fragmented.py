import sys
import numpy as np

def get_color_map():
    return {'W': 1, 'B': 0}

def read_input():
    return sys.stdin.read

def read_line():
    return sys.stdin.readline

def parse_n_k(line):
    n, k = map(int, line.split())
    return n, k

def parse_entries(data):
    return [line.split() for line in data.splitlines()]

def convert_entry_to_xy(lst, k, wb):
    x = int(lst[0]) % (2 * k)
    y = (int(lst[1]) + k * wb[lst[2]]) % (2 * k)
    return [x, y]

def build_xy_list(xyc, k, wb):
    return [convert_entry_to_xy(lst, k, wb) for lst in xyc]

def allocate_mat(k):
    return np.zeros((k + 1, 2 * k + 1), dtype='int64')

def allocate_cand(k):
    return np.zeros((k + 1, k + 1), dtype='int64')

def adjust_f0(e, k):
    return e[0] >= k

def adjust_f1(e, k):
    return e[1] >= k

def increment_mat(mat, e, k):
    f0 = adjust_f0(e, k)
    f1 = adjust_f1(e, k)
    row = e[0] - (f0 * k) + 1
    col = e[1] + ((-1) ** f1) * f0 * k + 1
    mat[row, col] += 1

def fill_mat(mat, xy, k):
    for e in xy:
        increment_mat(mat, e, k)

def compute_cumsum(mat):
    mat = np.cumsum(mat, axis=0)
    mat = np.cumsum(mat, axis=1)
    return mat

def compute_candidate(mat, k):
    part1 = mat[k, 2 * k]
    part2 = mat[k, k:2 * k + 1]
    part3 = mat[k, :k + 1]
    part4 = np.reshape(mat[:k + 1, 2 * k], (k + 1, 1))
    part5 = 2 * mat[:, k:2 * k + 1]
    part6 = 2 * mat[:, :k + 1]
    cand = part1 - part2 + part3 - part4 + part5 - part6
    return cand

def get_max_and_min_cand(cand):
    return np.max(cand), np.min(cand)

def print_result(cand, mat, k):
    max_cand, min_cand = get_max_and_min_cand(cand)
    val1 = max_cand
    val2 = mat[k, 2 * k] - min_cand
    print(max(val1, val2))

def main():
    wb = get_color_map()
    line_reader = read_line()
    content_reader = read_input()
    n, k = parse_n_k(line_reader())
    xyc = parse_entries(content_reader())
    xy = build_xy_list(xyc, k, wb)
    mat = allocate_mat(k)
    fill_mat(mat, xy, k)
    mat = compute_cumsum(mat)
    cand = compute_candidate(mat, k)
    print_result(cand, mat, k)

if __name__ == '__main__':
    main()