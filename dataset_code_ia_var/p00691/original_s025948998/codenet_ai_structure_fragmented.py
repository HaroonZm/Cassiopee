def generate_table(limit):
    return [i**3 for i in range(limit)]

def get_input():
    return int(input())

def find_max_sum(tbl, z):
    ma = 0
    for x in range(z-1, 0, -1):
        y = find_best_y(tbl, z, x)
        if check_break_condition(tbl, x, y):
            break
        ma = update_max(ma, tbl, x, y)
    return ma

def find_best_y(tbl, z, x):
    from bisect import bisect_left
    return bisect_left(tbl, tbl[z]-tbl[x])-1

def check_break_condition(tbl, x, y):
    return tbl[y] > tbl[x]

def update_max(ma, tbl, x, y):
    return max(ma, tbl[x]+tbl[y])

def compute_and_print_result(tbl, z):
    ma = find_max_sum(tbl, z)
    print(tbl[z]-ma)

def main_loop(tbl):
    while True:
        z = get_input()
        if should_break(z):
            break
        process_input(tbl, z)

def process_input(tbl, z):
    compute_and_print_result(tbl, z)

def should_break(z):
    return z == 0

def main():
    tbl = generate_table(1111)
    main_loop(tbl)

main()