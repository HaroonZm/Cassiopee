def read_input():
    return input()

def parse_nm(line):
    parts = line.split()
    return int(parts[0]), int(parts[1])

def init_blocked(n):
    return [0 for _ in range(n + 1)]

def read_blocked_indices(m):
    indices = []
    for _ in range(m):
        idx = int(read_input())
        indices.append(idx)
    return indices

def update_blocked_array(b, blocked_indices):
    for idx in blocked_indices:
        b[idx] = 1

def init_ways_array(n):
    return [0 for _ in range(n + 1)]

def set_initial_ways(s):
    s[0] = 1

def set_first_step_ways(s, b):
    if b[1] == 0:
        s[1] = 1
    else:
        s[1] = 0

def compute_ways(n, b, s):
    MOD = 1000000007
    for ni in range(2, n + 1):
        if b[ni] == 0:
            s[ni] = (s[ni - 1] + s[ni - 2]) % MOD
        else:
            s[ni] = 0

def output_result(s, n):
    print(s[n])

def main():
    nm_line = read_input()
    n, m = parse_nm(nm_line)
    b = init_blocked(n)
    blocked_indices = read_blocked_indices(m)
    update_blocked_array(b, blocked_indices)
    s = init_ways_array(n)
    set_initial_ways(s)
    set_first_step_ways(s, b)
    compute_ways(n, b, s)
    output_result(s, n)

main()