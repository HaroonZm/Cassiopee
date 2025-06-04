from collections import Counter

def parse_input_line():
    return list(map(int, input().split()))

def read_n_m():
    n, m = parse_input_line()
    return n, m

def initialize_sx(n, m):
    return [[0]*n for _ in range(m)]

def create_tx():
    line = parse_input_line()
    return line[1:]

def assign_to_sx(sx, i, tx, n):
    for ti in tx:
        sx[i][n-ti] = 1 << (ti-1)

def read_sx(n, m):
    sx = initialize_sx(n, m)
    for i in range(m):
        tx = create_tx()
        assign_to_sx(sx, i, tx, n)
    return sx

def read_px():
    return parse_input_line()

def get_all_combinations(n):
    return range(1 << n)

def process_si(si):
    return sum(si)

def count_ones_in_binary(num):
    return Counter(bin(num)[2:])['1']

def compute_c(i, sum_si):
    return count_ones_in_binary(i & sum_si)

def get_temp_c_list(n, sx, i):
    temp_c_list = []
    for si in sx:
        sum_si = process_si(si)
        c = compute_c(i, sum_si)
        temp_c_list.append(c % 2)
    return temp_c_list

def check_px_equal(temp_c_list, px):
    return temp_c_list == px

def count_valid_ans(n, sx, px):
    ans = 0
    for i in get_all_combinations(n):
        temp_c_list = get_temp_c_list(n, sx, i)
        if check_px_equal(temp_c_list, px):
            ans += 1
    return ans

def solve(n, m, sx, px):
    return count_valid_ans(n, sx, px)

def main():
    n, m = read_n_m()
    sx = read_sx(n, m)
    px = read_px()
    print(solve(n, m, sx, px))

if __name__ == '__main__':
    main()