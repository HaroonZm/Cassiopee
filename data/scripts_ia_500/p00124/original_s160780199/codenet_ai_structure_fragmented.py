def parse_args(args):
    s = args[0]
    a = args[1]
    b = args[2]
    c = args[3]
    return s, a, b, c

def compute_value(a, c):
    return int(a)*3 + int(c)

def process_entry(args):
    s, a, b, c = parse_args(args)
    value = compute_value(a, c)
    return s, value

def read_input_line():
    return raw_input().split()

def read_multiple_lines(count):
    lines = []
    for _ in xrange(count):
        line = read_input_line()
        lines.append(line)
    return lines

def map_func_on_lines(lines):
    return map(process_entry, lines)

def sort_entries(entries):
    entries.sort(key=lambda x: -x[1])

def format_entry(entry):
    s, p = entry
    return "{},{}".format(s, p)

def print_entries(entries):
    print "\n".join(map(format_entry, entries))

def read_integer():
    return input()

def main_loop():
    n = read_integer()
    while True:
        lines = read_multiple_lines(n)
        entries = map_func_on_lines(lines)
        sort_entries(entries)
        print_entries(entries)
        n = read_integer()
        if n == 0:
            break
        print

main_loop()