import sys

def read_input():
    return sys.stdin.readline

def write_output():
    return sys.stdout.write

def parse_first_line(readline):
    line = readline().split()
    return int(line[0]), int(line[1])

def parse_list(readline):
    return list(map(int, readline().split()))

def make_C(A, B, M):
    C = []
    prv = 0
    for i in range(M):
        c_elem = build_C_entry(A, B, i, prv)
        C.append(c_elem)
        prv = A[i+1]
    return C

def build_C_entry(A, B, i, prv):
    return (A[i+1] - prv, 1 << B[i])

def process_main_loop(N, C):
    ans = 0
    for i in range(N-1, -1, -1):
        v = 1 << (i+1)
        C, add = process_round(C, v)
        ans += add
    return ans, C

def process_round(C, v):
    C1 = []
    r = 0
    p = 0
    add = 0
    for c, b in C:
        add, r, p = process_C_entry(c, b, v, C1, add, r, p)
    return C1, add

def process_C_entry(c, b, v, C1, add, r, p):
    local_add = 0
    if r:
        b0, more_add = merge_bits(b, p, v)
        local_add += more_add
        C1 = append_to_C1(C1, 1, b0)
        c -= 1
    if c > 1:
        local_add += check_pair_addition(b, v, c)
        C1 = append_to_C1(C1, c // 2, b)
    if c % 2:
        r = 1
        p = b
    else:
        r = 0
    add += local_add
    return add, r, p

def merge_bits(b, p, v):
    if (b & v) == (p & v) > 0:
        b0 = b | p
        add = 0
    elif b & v:
        b0 = p
        add = 0
    elif p & v:
        b0 = b
        add = 0
    else:
        b0 = b | p
        add = 1
    return b0, add

def check_pair_addition(b, v, c):
    if b & v == 0:
        return c // 2
    return 0

def append_to_C1(C1, count, b):
    if count == 0:
        return C1
    if C1 and C1[-1][1] == b:
        c1, b1 = C1.pop()
        C1.append((count + c1, b))
    else:
        C1.append((count, b))
    return C1

def final_adjustment(C, ans, write):
    c, p = C[0]
    if p & 1 == 0:
        ans += 1
    write("%d\n" % ans)

def solve():
    readline = read_input()
    write = write_output()
    N, M = parse_first_line(readline)
    A = parse_list(readline)
    B = parse_list(readline)
    C = make_C(A, B, M)
    ans, C = process_main_loop(N, C)
    final_adjustment(C, ans, write)

solve()