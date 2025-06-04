def read_input():
    return int(input())

def read_mx(Q):
    return [parse_tuple(input()) for _ in range(Q)]

def parse_tuple(s):
    return tuple(map(int, s.split()))

def get_p1s():
    return [2,3,5,7,11,13,17]

def get_nums():
    return [9,6,4,3,3,3,3]

def get_range_nums(nums):
    return [range(num) for num in nums]

def get_p2s():
    return [19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293]

def create_empty_lists(length):
    return [[] for _ in range(length)]

def is_divisible(a, b):
    return a % b == 0

def classify_mx(mxs, p2s):
    mx1s = []
    mx2ss = create_empty_lists(len(p2s))
    for m, x in mxs:
        assign_to_classification(m, x, p2s, mx1s, mx2ss)
    return mx1s, mx2ss

def assign_to_classification(m, x, p2s, mx1s, mx2ss):
    for i, p2 in enumerate(p2s):
        if is_divisible(m, p2):
            add_to_mx2ss(mx2ss, i, m, x)
            return
    mx1s.append((m, x))

def add_to_mx2ss(mx2ss, idx, m, x):
    mx2ss[idx].append((m, x))

def prod_power(p1s, es):
    result = 1
    for p, e in zip(p1s, es):
        result = multiply_power(result, p, e)
    return result

def multiply_power(current, base, exp):
    return current * (base ** exp)

def calc_A(f, mx1s):
    A = 0
    for m1, x1 in mx1s:
        if is_divisible(f, m1):
            A += x1
    return A

def calc_A2(f, p2, mx2s):
    A2 = 0
    for m2, x2 in mx2s:
        if is_divisible(f * p2, m2):
            A2 += x2
    return A2

def update_A(A, p2, mx2s, f):
    for mx2, mx2_list in zip(p2, mx2s):
        A = add_A2_to_A(A, f, mx2, mx2_list)
    return A

def add_A2_to_A(A, f, p2, mx2_list):
    A2 = calc_A2(f, p2, mx2_list)
    if A2 > 0:
        return A + A2
    return A

def get_max_A(ans, A):
    return max(ans, A)

def process_products(rangeNums, p1s, mx1s, p2s, mx2ss):
    from itertools import product
    ans = 0
    for es in product(*rangeNums):
        f = prod_power(p1s, es)
        A = calc_A(f, mx1s)
        for p2, mx2s in zip(p2s, mx2ss):
            A2 = calc_A2(f, p2, mx2s)
            if A2 > 0:
                A += A2
        ans = get_max_A(ans, A)
    return ans

def main():
    Q = read_input()
    mxs = read_mx(Q)
    p1s = get_p1s()
    nums = get_nums()
    rangeNums = get_range_nums(nums)
    p2s = get_p2s()
    mx1s, mx2ss = classify_mx(mxs, p2s)
    ans = process_products(rangeNums, p1s, mx1s, p2s, mx2ss)
    print(ans)

main()