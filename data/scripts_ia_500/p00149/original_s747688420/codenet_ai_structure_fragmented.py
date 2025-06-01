from collections import Counter

def read_input_line():
    return input()

def parse_input_line(line):
    parts = line.split()
    return parts

def convert_to_floats(parts):
    return map(float, parts)

def get_check_result(value):
    if value >= 1.1:
        return "A"
    elif value >= 0.6:
        return "B"
    elif value >= 0.2:
        return "C"
    else:
        return "D"

def increment_counter(counter, key):
    counter[key] += 1

def process_line(line, dicl, dicr):
    parts = parse_input_line(line)
    l, r = convert_to_floats(parts)
    lx = get_check_result(l)
    rx = get_check_result(r)
    increment_counter(dicl, lx)
    increment_counter(dicr, rx)

def print_results(dicl, dicr):
    for alpha in ("A", "B", "C", "D"):
        print(dicl[alpha], dicr[alpha])

def main():
    dicl = Counter()
    dicr = Counter()
    while True:
        try:
            line = read_input_line()
            process_line(line, dicl, dicr)
        except EOFError:
            break
    print_results(dicl, dicr)

main()