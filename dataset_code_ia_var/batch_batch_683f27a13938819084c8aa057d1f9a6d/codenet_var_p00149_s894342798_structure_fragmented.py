def initialize_counters():
    return {'al': 0, 'ar': 0, 'bl': 0, 'br': 0, 'cl': 0, 'cr': 0, 'dl': 0, 'dr': 0}

def read_input():
    try:
        return raw_input()
    except EOFError:
        return None

def parse_input(line):
    try:
        l, r = map(float, line.split())
        return l, r
    except Exception:
        return None, None

def categorize_value_left(l, counters):
    if l is None:
        return
    if l >= 1.1:
        counters['al'] += 1
    elif 0.6 <= l < 1.1:
        counters['bl'] += 1
    elif 0.2 <= l < 0.6:
        counters['cl'] += 1
    else:
        counters['dl'] += 1

def categorize_value_right(r, counters):
    if r is None:
        return
    if r >= 1.1:
        counters['ar'] += 1
    elif 0.6 <= r < 1.1:
        counters['br'] += 1
    elif 0.2 <= r < 0.6:
        counters['cr'] += 1
    else:
        counters['dr'] += 1

def process_line(line, counters):
    l, r = parse_input(line)
    categorize_value_left(l, counters)
    categorize_value_right(r, counters)

def process_all_inputs(counters):
    while True:
        line = read_input()
        if line is None:
            break
        process_line(line, counters)

def format_output(counters):
    return "{} {}\n{} {}\n{} {}\n{} {}".format(
        counters['al'], counters['ar'],
        counters['bl'], counters['br'],
        counters['cl'], counters['cr'],
        counters['dl'], counters['dr']
    )

def main():
    counters = initialize_counters()
    process_all_inputs(counters)
    print format_output(counters)

main()