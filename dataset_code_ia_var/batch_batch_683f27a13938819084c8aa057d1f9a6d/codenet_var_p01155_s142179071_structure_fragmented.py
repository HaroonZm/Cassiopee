import math

def read_input():
    return [int(x) for x in raw_input().split()]

def is_zero_pair(pair):
    return pair[0] == 0

def initialize_ruinmin():
    return 10000**2 * 3

def get_divisor_pairs(n):
    pairs = []
    max_div = int(math.sqrt(n))
    for i in range(1, 101):
        if n % i == 0 and max_div >= i:
            pairs.append([i, n // i])
    return pairs

def sorted_combined_pair(apair, bpair):
    return sorted(apair + bpair)

def calculate_ruin(sorted_pair):
    return (sorted_pair[1] - sorted_pair[0]) ** 2 + \
           (sorted_pair[2] - sorted_pair[1]) ** 2 + \
           (sorted_pair[3] - sorted_pair[2]) ** 2

def min_ruin(anum, bnum, ruinmin):
    for apair in anum:
        for bpair in bnum:
            abset = sorted_combined_pair(apair, bpair)
            ruin = calculate_ruin(abset)
            ruinmin = min(ruinmin, ruin)
    return ruinmin

def process_pair(a, b):
    anum = get_divisor_pairs(a)
    bnum = get_divisor_pairs(b)
    ruinmin = initialize_ruinmin()
    return min_ruin(anum, bnum, ruinmin)

def main_loop():
    while True:
        ab_pair = read_input()
        if is_zero_pair(ab_pair):
            break
        a, b = ab_pair
        result = process_pair(a, b)
        print result

main_loop()