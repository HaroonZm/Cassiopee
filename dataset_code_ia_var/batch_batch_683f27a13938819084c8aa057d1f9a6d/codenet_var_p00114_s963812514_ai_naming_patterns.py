from fractions import gcd as fn_gcd

def fn_lcm(val_a, val_b):
    return val_a * val_b // fn_gcd(val_a, val_b)

def fn_cycle_lengths(seq_a, seq_m):
    for val_a, val_m in zip(seq_a, seq_m):
        curr_exp = 1
        curr_res = val_a % val_m
        while curr_res != 1:
            curr_res = (val_a * curr_res) % val_m
            curr_exp += 1
        yield curr_exp

while True:
    input_vals = list(map(int, raw_input().split()))
    if all(val == 0 for val in input_vals):
        break
    powers = fn_cycle_lengths(input_vals[::2], input_vals[1::2])
    from functools import reduce
    print(reduce(fn_lcm, powers))