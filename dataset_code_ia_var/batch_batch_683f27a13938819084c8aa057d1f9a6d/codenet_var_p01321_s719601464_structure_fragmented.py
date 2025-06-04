def get_input():
    return input()

def should_break(n):
    return n == 0

def parse_int(value):
    return int(value)

def init_min_value():
    return 501

def init_max_value():
    return 0

def get_range(n):
    return range(n)

def read_line():
    return raw_input()

def split_line(line):
    return line.split()

def map_to_ints(strs):
    return map(int, strs)

def sum_ints(ints):
    return sum(ints)

def update_min(curr_min, value):
    return min(curr_min, value)

def update_max(curr_max, value):
    return max(curr_max, value)

def prepare_output(ma, mi):
    return "%d %d"%(ma, mi)

def print_output(output):
    print output

def handle_inner_loop(n):
    mi = init_min_value()
    ma = init_max_value()
    for i in get_range(n):
        line = read_line()
        splitted = split_line(line)
        ints = map_to_ints(splitted)
        s = sum_ints(ints)
        mi = update_min(mi, s)
        ma = update_max(ma, s)
    return ma, mi

def main_loop():
    while True:
        n = get_input()
        n = parse_int(n)
        if should_break(n):
            break
        ma, mi = handle_inner_loop(n)
        output = prepare_output(ma, mi)
        print_output(output)

main_loop()