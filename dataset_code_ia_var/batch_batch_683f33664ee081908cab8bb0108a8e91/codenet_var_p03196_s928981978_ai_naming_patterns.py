from fractions import gcd
from random import randint
from functools import reduce
from sys import argv

def brent_factor(N):
    if N % 2 == 0:
        return 2
    rand_y = randint(1, N-1)
    rand_c = randint(1, N-1)
    rand_m = randint(1, N-1)
    g_val = 1
    r_val = 1
    q_val = 1
    while g_val == 1:
        x_val = rand_y
        for _ in range(r_val):
            rand_y = ((rand_y * rand_y) % N + rand_c) % N
        k_val = 0
        while k_val < r_val and g_val == 1:
            ys_val = rand_y
            iter_range = min(rand_m, r_val - k_val)
            for _ in range(iter_range):
                rand_y = ((rand_y * rand_y) % N + rand_c) % N
                q_val = q_val * abs(x_val - rand_y) % N
            g_val = gcd(q_val, N)
            k_val += rand_m
        r_val *= 2
    if g_val == N:
        while True:
            ys_val = ((ys_val * ys_val) % N + rand_c) % N
            g_val = gcd(abs(x_val - ys_val), N)
            if g_val > 1:
                break
    return g_val

def integer_factorization(target_num):
    if target_num <= 0:
        return []
    if target_num == 1:
        return [1]
    remain_num = target_num
    factor_counts = {}
    found_prime = 0
    large_factor_limit = 1000000
    if remain_num % 2 == 0:
        factor_counts[2] = 0
    if remain_num % 3 == 0:
        factor_counts[3] = 0
    while remain_num % 2 == 0:
        factor_counts[2] += 1
        remain_num //= 2
    while remain_num % 3 == 0:
        factor_counts[3] += 1
        remain_num //= 3

    base_factor = 5
    add_step = 2
    while base_factor <= large_factor_limit:
        while remain_num % base_factor == 0:
            if base_factor not in factor_counts:
                factor_counts[base_factor] = 0
            factor_counts[base_factor] += 1
            remain_num //= base_factor
        base_factor += add_step
        add_step = 6 - add_step

    while remain_num > large_factor_limit:
        prev_num = remain_num
        curr_num = remain_num
        while curr_num != found_prime:
            found_prime = curr_num
            curr_num = brent_factor(found_prime)
        if curr_num not in factor_counts:
            factor_counts[curr_num] = 0
        factor_counts[curr_num] += 1
        remain_num //= curr_num
    if remain_num != 1:
        factor_counts[remain_num] = 1
    return factor_counts

def main_routine():
    input_n, input_p = map(int, input().strip().split())
    if input_p == 1:
        print(1)
        return
    prime_factors = integer_factorization(input_p)
    answer_val = 1
    for factor_val in prime_factors.keys():
        prime_factors[factor_val] //= input_n
        answer_val *= factor_val ** prime_factors[factor_val]
    print(answer_val)

if __name__ == "__main__":
    main_routine()