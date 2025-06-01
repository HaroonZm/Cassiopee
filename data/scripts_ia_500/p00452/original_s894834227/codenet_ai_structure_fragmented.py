from bisect import bisect

def read_input():
    return map(int, raw_input().split())

def check_termination(n):
    return n == 0

def read_numbers(n):
    return [input() for _ in range(n)]

def append_zero(p):
    p.append(0)
    return p

def generate_sums(p):
    sums = []
    for i in p:
        for j in p:
            sums.append(i + j)
    return sums

def unique_sorted_sums(sums):
    return sorted(set(sums))

def find_bisect_index(p, lmt):
    return bisect(p, lmt)

def max_sum_under_limit(p, s, lmt):
    max_sum = None
    for i in p[:s]:
        idx = bisect(p, lmt - i) - 1
        candidate = i + p[idx]
        if max_sum is None or candidate > max_sum:
            max_sum = candidate
    return max_sum

def main_loop():
    while True:
        n, lmt = read_input()
        if check_termination(n):
            break
        p = read_numbers(n)
        p = append_zero(p)
        sums = generate_sums(p)
        p = unique_sorted_sums(sums)
        s = find_bisect_index(p, lmt)
        result = max_sum_under_limit(p, s, lmt)
        print result

main_loop()