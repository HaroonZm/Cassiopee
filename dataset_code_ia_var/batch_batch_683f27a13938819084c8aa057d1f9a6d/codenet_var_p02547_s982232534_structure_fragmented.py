def get_input():
    return input()

def parse_int(value):
    return int(value)

def parse_pair(values):
    return map(int, values.split())

def should_increment_streak(d1, d2):
    return d1 == d2

def reset_streak():
    return 0

def increment_streak(s):
    return s + 1

def check_finished(s):
    return s == 3

def set_flag_true():
    return 1

def main_logic_loop(n):
    s = 0
    f = 0
    for _ in range(n):
        line = get_input()
        d1, d2 = parse_pair(line)
        if should_increment_streak(d1, d2):
            s = increment_streak(s)
        else:
            s = reset_streak()
        if check_finished(s):
            f = set_flag_true()
    return f

def print_result(f):
    if f == 1:
        print('Yes')
    else:
        print('No')

def main():
    n = get_input()
    n = parse_int(n)
    f = main_logic_loop(n)
    print_result(f)

main()