def get_input():
    return input().split()

def parse_n(nm):
    return int(nm[0])

def parse_m(nm):
    return int(nm[1])

def parse_a():
    return input().split()

def convert_a_to_int_list(a):
    return [int(x) for x in a]

def initialize_b():
    return {0: 1}

def initialize_k():
    return 0

def update_k(k, ai, m):
    k += ai
    k = k % m
    return k

def update_b(b, k):
    if k in b:
        b[k] += 1
    else:
        b[k] = 1

def process_b_and_k(n, a, m):
    b = initialize_b()
    k = initialize_k()
    for i in range(n):
        k = update_k(k, a[i], m)
        update_b(b, k)
    return b

def get_b_values(b):
    return b.values()

def initialize_ans():
    return 0

def combinatoric_count(i):
    return i * (i - 1) // 2

def compute_ans(c):
    ans = initialize_ans()
    for i in c:
        ans += combinatoric_count(i)
    return ans

def output_result(ans):
    print(ans)

def main():
    nm = get_input()
    n = parse_n(nm)
    m = parse_m(nm)
    a = parse_a()
    a = convert_a_to_int_list(a)
    b = process_b_and_k(n, a, m)
    c = get_b_values(b)
    ans = compute_ans(c)
    output_result(ans)

main()