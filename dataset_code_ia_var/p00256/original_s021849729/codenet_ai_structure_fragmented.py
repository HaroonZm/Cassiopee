from datetime import date, timedelta

def get_start_date():
    return date(2012, 12, 21)

def read_input():
    return input()

def should_break(s):
    return s == '#'

def parse_dot_separated(s):
    return list(map(int, s.split('.')))

def is_gregorian_date(d):
    return len(d) == 3

def reduce_years(d):
    r = 0
    while d[0] > 3000:
        d[0] -= 400
        r += 365 * 400 + 97
    return d, r

def construct_date(d):
    return date(d[0], d[1], d[2])

def calc_days_between(ed, st):
    return (ed - st).days

def compute_long_count_components(r):
    ki = r % 20
    r //= 20
    w = r % 18
    r //= 18
    t = r % 20
    r //= 20
    ka = r % 20
    r //= 20
    b = r % 13
    return b, ka, t, w, ki

def format_long_count(b, ka, t, w, ki):
    return f"{b}.{ka}.{t}.{w}.{ki}"

def process_gregorian(d, st):
    d, r = reduce_years(d)
    ed = construct_date(d)
    r += calc_days_between(ed, st)
    b, ka, t, w, ki = compute_long_count_components(r)
    return format_long_count(b, ka, t, w, ki)

def combine_values(d):
    r = d[0]
    r *= 20
    r += d[1]
    r *= 20
    r += d[2]
    r *= 18
    r += d[3]
    r *= 20
    r += d[4]
    return r

def add_days_to_start(st, days):
    return st + timedelta(days=days)

def format_gregorian(ed):
    return f"{ed.year}.{ed.month}.{ed.day}"

def process_long_count(d, st):
    r = combine_values(d)
    ed = add_days_to_start(st, r)
    return format_gregorian(ed)

def main_loop():
    st = get_start_date()
    while True:
        s = read_input()
        if should_break(s):
            break
        d = parse_dot_separated(s)
        if is_gregorian_date(d):
            output = process_gregorian(d, st)
            print(output)
        else:
            output = process_long_count(d, st)
            print(output)

main_loop()