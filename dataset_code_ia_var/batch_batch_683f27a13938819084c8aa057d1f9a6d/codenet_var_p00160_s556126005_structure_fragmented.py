tbl = [600, 800, 1000, 1200, 1400, 1600]

def get_input():
    return int(input())

def get_package_input():
    return list(map(int, input().split()))

def get_sum(x, y, h):
    return x + y + h

def is_valid_package(s, w):
    return s <= 160 and w <= 25

def calculate_k1(s):
    if s <= 60:
        return 0
    else:
        return (s - 61) // 20 + 1

def calculate_k2(w):
    if w <= 2:
        return 0
    else:
        return (w - 1) // 5 + 1

def get_fee_index(k1, k2):
    return max(k1, k2)

def calculate_package_fee(x, y, h, w):
    s = get_sum(x, y, h)
    if is_valid_package(s, w):
        k1 = calculate_k1(s)
        k2 = calculate_k2(w)
        idx = get_fee_index(k1, k2)
        return tbl[idx]
    else:
        return 0

def calculate_total_fee_for_case(n):
    fee = 0
    for _ in range(n):
        x, y, h, w = get_package_input()
        fee += calculate_package_fee(x, y, h, w)
    return fee

def process_cases():
    while True:
        n = get_input()
        if n == 0:
            break
        total_fee = calculate_total_fee_for_case(n)
        print(total_fee)

process_cases()