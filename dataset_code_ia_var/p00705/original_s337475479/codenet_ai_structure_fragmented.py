def read_input():
    return map(int, raw_input().split())

def is_end(n, q):
    return n == 0 and q == 0

def init_counts():
    return [0] * 101

def get_lines(n):
    lines = []
    for _ in xrange(n):
        lines.append(raw_input())
    return lines

def parse_line(line):
    items = map(int, line.split())
    return items[1:]

def update_counts_and_max(data, counts, maxd):
    for d in data:
        counts[d] += 1
        if counts[d] > maxd[0]:
            maxd[0] = counts[d]

def process_n_lines(lines, counts, maxd):
    for line in lines:
        data = parse_line(line)
        update_counts_and_max(data, counts, maxd)

def check_and_print(counts, maxd, q):
    if q <= maxd[0]:
        print counts.index(maxd[0])
    else:
        print 0

def main_loop():
    while True:
        n, q = read_input()
        if is_end(n, q):
            break
        counts = init_counts()
        maxd = [0]
        lines = get_lines(n)
        process_n_lines(lines, counts, maxd)
        check_and_print(counts, maxd, q)

main_loop()