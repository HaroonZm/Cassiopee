def read_next_line():
    return raw_input()

def parse_n_m(line):
    return map(int, line.split())

def should_break(n):
    return n == 0

def read_n_numbers(n):
    return [int(raw_input()) for _ in range(n)]

def sort_list(lst):
    return sorted(lst)

def compute_sum(lst):
    return sum(lst)

def compute_difference(sum_hana, sum_taro):
    return sum_hana - sum_taro

def initialize_vars():
    return 101, 101

def in_list(val, lst):
    return val in lst

def compute_target(d, i):
    return d / 2.0 + i

def update_values(i, target):
    return i, int(target)

def format_output(t, h):
    return "%d %d" % (t, h)

def should_print(t):
    return t < 101

def main_loop():
    while True:
        line = read_next_line()
        n, m = parse_n_m(line)
        if should_break(n):
            break
        taro_raw = read_n_numbers(n)
        taro = sort_list(taro_raw)
        hana = read_n_numbers(m)
        sum_hana = compute_sum(hana)
        sum_taro = compute_sum(taro)
        d = compute_difference(sum_hana, sum_taro)
        t, h = initialize_vars()
        for i in taro:
            target = compute_target(d, i)
            if in_list(target, hana):
                t, h = update_values(i, target)
                break
        if should_print(t):
            print format_output(t, h)
        else:
            print -1

main_loop()