def read_input():
    return int(input())

def read_sequence():
    return list(map(int, input().split()))

def initialize_defaultdict():
    from collections import defaultdict
    return defaultdict(int)

def initialize_answer():
    return 0

def initialize_empty_list():
    return []

def compute_l(i, s):
    return i + s

def compute_r(i, s):
    return i - s

def update_defaultdict(d, key):
    d[key] += 1

def update_answer(ans, d, key):
    return ans + d[key]

def process_element(i, s, d, ans):
    l = compute_l(i, s)
    r = compute_r(i, s)
    update_defaultdict(d, l)
    ans = update_answer(ans, d, r)
    return ans

def process_sequence(src, d, ans):
    for idx, val in enumerate(src, 1):
        ans = process_element(idx, val, d, ans)
    return ans

def print_output(result):
    print(result)

def main():
    N = read_input()
    src = read_sequence()
    ans = initialize_answer()
    d = initialize_defaultdict()
    e = initialize_empty_list()
    result = process_sequence(src, d, ans)
    print_output(result)

main()