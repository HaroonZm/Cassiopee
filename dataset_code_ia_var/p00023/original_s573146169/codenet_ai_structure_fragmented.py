import math

def get_n():
    return int(input())

def parse_input():
    return map(float, raw_input().split())

def distance(xa, ya, xb, yb):
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

def condition_sum_radii_less(r, ra, rb):
    return ra + rb < r

def condition_abs_diff_radii_leq(r, ra, rb):
    return abs(ra - rb) <= r

def condition_diff_radii_greater(r, ra, rb):
    return ra - rb > r

def output_result(value):
    print value

def process_case():
    xa, ya, ra, xb, yb, rb = parse_input()
    r = distance(xa, ya, xb, yb)
    if condition_sum_radii_less(r, ra, rb):
        output_result(0)
    elif condition_abs_diff_radii_leq(r, ra, rb):
        output_result(1)
    elif condition_diff_radii_greater(r, ra, rb):
        output_result(2)
    else:
        output_result(-2)

def main():
    n = get_n()
    for _ in range(n):
        process_case()

main()