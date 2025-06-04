def get_kth(x, a, k):
    if k < a:
        return k
    return k + 1

def get_rkth(x, a, k):
    if x < a:
        return x - k + 1
    if k < (x - a):
        return x - k + 1
    return x - k

def nb(x, b):
    if x < b:
        return x
    return x + 1

def get_half_1(x):
    return (x + 1) / 2

def get_half_2(a, b):
    return b - a

def get_half_3(x, b):
    return nb(x, b) - b

def is_in_valid_range(value, x):
    return value >= 1 and value <= x

def calculate_expression(x, a, b, k):
    left = get_kth(x, a, k)
    right = get_rkth(nb(x, b), b, k)
    return left * right

def check_all_deltas(rep, mv, x, a, b, base_half):
    for delta in xrange(-mv, mv + 1):
        current = base_half + delta
        if is_in_valid_range(current, x):
            expr = calculate_expression(x, a, b, current)
            rep = max(rep, expr)
    return rep

def f(x, a, b):
    mv = 25
    rep = 0
    half1 = get_half_1(x)
    rep = check_all_deltas(rep, mv, x, a, b, half1)
    half2 = get_half_2(a, b)
    rep = check_all_deltas(rep, mv, x, a, b, half2)
    half3 = get_half_3(x, b)
    rep = check_all_deltas(rep, mv, x, a, b, half3)
    return rep

def swap_if_needed(a, b):
    if a > b:
        return b, a
    return a, b

def process_query(a, b):
    a, b = swap_if_needed(a, b)
    lo = 1
    hi = 10**19
    res = 0
    while lo <= hi:
        mid = (lo + hi)//2
        if f(mid, a, b) < a * b:
            lo = mid + 1
            res = mid
        else:
            hi = mid - 1
    print res

def read_int():
    return int(raw_input())

def read_pair():
    return map(int, raw_input().split())

def main():
    q = read_int()
    while q > 0:
        a, b = read_pair()
        process_query(a, b)
        q -= 1

main()