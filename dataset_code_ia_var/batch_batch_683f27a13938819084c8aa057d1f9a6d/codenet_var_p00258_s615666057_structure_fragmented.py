bc = [bin(i).count('1') for i in range(65536)]  # bitcount

def read_line_as_integers(f_i):
    return list(map(int, f_i.readline().split()))

def read_binary_lines(n, f_i):
    return [int(f_i.readline().replace(' ', ''), 2) for _ in range(n)]

def try_update_dict(d, key, value):
    if key in d:
        if d[key] < value:
            d[key] = value
    else:
        d[key] = value

def process_dp(a, B, bc, dp1):
    dp2 = {}
    for st1, sc1 in dp1.items():
        for b in B:
            cb = st1 & b
            sc2 = sc1 + bc[cb]
            st2 = (st1 - cb) | a
            try_update_dict(dp2, st2, sc2)
    return dp2

def process_A_list(A, B, bc):
    dp1 = {A[0]: 0}
    for a in A[1:] + [0]:
        dp2 = process_dp(a, B, bc, dp1)
        dp1 = dp2
    return dp1

def print_max_dp(dp1):
    print(max(dp1.values()))

def process_single_case(n, c, f_i):
    A = read_binary_lines(n, f_i)
    B = read_binary_lines(c, f_i)
    dp1 = process_A_list(A, B, bc)
    print_max_dp(dp1)

def main_loop():
    from sys import stdin
    f_i = stdin
    while True:
        n_c = read_line_as_integers(f_i)
        if not n_c:
            break  # In case of empty input
        n, c = n_c
        if n == 0:
            break
        process_single_case(n, c, f_i)

def solve():
    main_loop()

solve()