def read_input():
    return raw_input()

def parse_input(line):
    return map(float, line.split())

def increment_left_counters(l, counters):
    if l >= 1.1:
        counters['al'] += 1
    elif 0.6 <= l < 1.1:
        counters['bl'] += 1
    elif 0.2 <= l < 0.6:
        counters['cl'] += 1
    else:
        counters['dl'] += 1

def increment_right_counters(r, counters):
    if r >= 1.1:
        counters['ar'] += 1
    elif 0.6 <= r < 1.1:
        counters['br'] += 1
    elif 0.2 <= r < 0.6:
        counters['cr'] += 1
    else:
        counters['dr'] += 1

def print_counters(counters):
    print "{} {}\n{} {}\n{} {}\n{} {}".format(
        counters['al'], counters['ar'],
        counters['bl'], counters['br'],
        counters['cl'], counters['cr'],
        counters['dl'], counters['dr']
    )

def main():
    counters = {
        'al':0, 'ar':0,
        'bl':0, 'br':0,
        'cl':0, 'cr':0,
        'dl':0, 'dr':0
    }
    while True:
        try:
            line = read_input()
            l, r = parse_input(line)
            increment_left_counters(l, counters)
            increment_right_counters(r, counters)
        except EOFError:
            break
    print_counters(counters)

main()