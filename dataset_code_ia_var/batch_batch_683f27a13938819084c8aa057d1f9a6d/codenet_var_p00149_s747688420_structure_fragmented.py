from collections import Counter

def get_input():
    try:
        return input()
    except EOFError:
        return None

def parse_line(line):
    return map(float, line.split())

def get_grade(value):
    if value >= 1.1:
        return "A"
    elif value >= 0.6:
        return "B"
    elif value >= 0.2:
        return "C"
    else:
        return "D"

def update_counter(counter, grade):
    counter[grade] += 1

def process_line(line, dicl, dicr):
    l, r = parse_line(line)
    lx = get_grade(l)
    rx = get_grade(r)
    update_counter(dicl, lx)
    update_counter(dicr, rx)

def process_inputs(dicl, dicr):
    while True:
        line = get_input()
        if line is None:
            break
        process_line(line, dicl, dicr)

def print_result_for_grade(dicl, dicr, grade):
    print(dicl[grade], dicr[grade])

def main_loop():
    dicl = Counter()
    dicr = Counter()
    process_inputs(dicl, dicr)
    for grade in ("A", "B", "C", "D"):
        print_result_for_grade(dicl, dicr, grade)

main_loop()