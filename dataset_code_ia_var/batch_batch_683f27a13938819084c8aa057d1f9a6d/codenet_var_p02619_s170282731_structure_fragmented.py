def read_d():
    return int(input())

def read_c():
    return list(map(int, input().split()))

def read_s(d):
    return [read_s_row() for _ in range(d)]

def read_s_row():
    return list(map(int, input().split()))

def read_t():
    return int(input())

def initialize_sat():
    return 0

def initialize_last():
    return [0] * 26

def update_last(last, t_idx, day):
    last[t_idx] = day
    return last

def add_score(sat, s_row, t_idx):
    return sat + s_row[t_idx]

def penalize_score(sat, c, day, last):
    for j in range(26):
        sat -= c[j] * (day - last[j])
    return sat

def print_result(sat):
    print(sat)

def process_day(i, s_row, sat, last, c):
    t = read_t()
    t_idx = t - 1
    day = i + 1
    sat = add_score(sat, s_row, t_idx)
    last = update_last(last, t_idx, day)
    sat = penalize_score(sat, c, day, last)
    print_result(sat)
    return sat, last

def main():
    d = read_d()
    c = read_c()
    s = read_s(d)
    sat = initialize_sat()
    last = initialize_last()
    for i in range(d):
        sat, last = process_day(i, s[i], sat, last, c)

main()