def read_input():
    from sys import stdin
    return stdin

def read_ints(f_i):
    return list(map(int, f_i.readline().split()))

def compute_difference(bm_i, bw_i):
    if bm_i > bw_i:
        d = bm_i - bw_i
    else:
        d = bw_i - bm_i
    return d

def compute_energy(bm_i, bw_i):
    d = compute_difference(bm_i, bw_i)
    return d * (d - 30) ** 2

def generate_energy_grid(bm, bw):
    e_gen = []
    for m in bm:
        row = []
        for w in bw:
            row.append(compute_energy(m, w))
        e_gen.append(row)
    return e_gen

def initialize_dp(W):
    bit_size = (1 << W)
    dp1 = [-1] * bit_size
    dp2 = [-1] * bit_size
    dp1[0] = 0
    dp2[0] = 0
    return dp1, dp2

def generate_add_bit(W):
    add_bit = []
    for i in range(W):
        add_bit.append(1 << i)
    return add_bit

def update_dp_for_i(i, dp1, dp2, add_bit, e_gen):
    for s1, e1 in enumerate(dp1):
        if e1 == -1:
            continue
        for b, e in zip(add_bit, e_gen[i]):
            if s1 & b:
                continue
            s2 = s1 | b
            e2 = e1 + e
            if e2 > dp2[s2]:
                dp2[s2] = e2

def solve():
    f_i = read_input()
    while True:
        M, W = read_ints(f_i)
        if M == 0:
            break
        
        bm = read_ints(f_i)
        bw = read_ints(f_i)
        
        e_gen = generate_energy_grid(bm, bw)
        
        dp1, dp2 = initialize_dp(W)
        add_bit = generate_add_bit(W)
        
        for i in range(M):
            update_dp_for_i(i, dp1, dp2, add_bit, e_gen)
            dp1 = dp2[:]
        print(max(dp2))

solve()