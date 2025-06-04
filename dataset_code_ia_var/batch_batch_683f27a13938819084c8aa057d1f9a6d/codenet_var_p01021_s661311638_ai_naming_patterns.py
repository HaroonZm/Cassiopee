from math import gcd

def compute_result():
    input_n, input_m = map(int, input().split())
    input_list_a = list(map(int, input().split()))
    input_list_b = list(map(int, input().split()))
    
    gcd_a = input_list_a[0]
    for idx_a in range(1, input_n):
        gcd_a = gcd(gcd_a, input_list_a[idx_a])
    
    lcm_b = input_list_b[0]
    for idx_b in range(1, input_m):
        gcd_b = gcd(lcm_b, input_list_b[idx_b])
        lcm_b = lcm_b * input_list_b[idx_b] // gcd_b
    
    if gcd_a % lcm_b != 0:
        print(0)
        return
    factor_num = gcd_a // lcm_b
    divisor_count = 1
    current_factor = 2
    while current_factor * current_factor <= factor_num:
        exponent = 1
        while factor_num % current_factor == 0:
            exponent += 1
            factor_num //= current_factor
        divisor_count *= exponent
        current_factor += 1
    if factor_num > 1:
        divisor_count *= 2
    print(divisor_count)

compute_result()