def read_n():
    return int(input())

def should_exit(n):
    return n == 0

def read_item_data():
    return list(map(int, input().split()))

def sum_dimensions(x, y, h):
    return x + y + h

def calculate_amount(dim_sum, w):
    if dim_sum <= 60 and w <= 2:
        return 600
    elif dim_sum <= 80 and w <= 5:
        return 800
    elif dim_sum <= 100 and w <= 10:
        return 1000
    elif dim_sum <= 120 and w <= 15:
        return 1200
    elif dim_sum <= 140 and w <= 20:
        return 1400
    elif dim_sum <= 160 and w <= 25:
        return 1600
    return 0

def process_item():
    x, y, h, w = read_item_data()
    dim_sum = sum_dimensions(x, y, h)
    return calculate_amount(dim_sum, w)

def process_batch(n):
    s_m = 0
    for _ in range(n):
        s_m += process_item()
    return s_m

def main_loop():
    while True:
        n = read_n()
        if should_exit(n):
            break
        res = process_batch(n)
        print(res)

main_loop()