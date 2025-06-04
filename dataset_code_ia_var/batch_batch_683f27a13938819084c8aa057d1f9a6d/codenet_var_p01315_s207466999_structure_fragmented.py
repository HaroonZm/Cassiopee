import sys

def read_input():
    try:
        n = int(input())
        return n
    except Exception:
        return 0

def read_data_line():
    line = sys.stdin.readline().strip()
    return line

def parse_line(line):
    tokens = line.split()
    label = tokens[0]
    numbers = list(map(int, tokens[1:]))
    return label, numbers

def compute_efficiency(numbers):
    p, a, b, c, d, e, f, s, m = numbers
    numerator = f * s * m - p
    denominator = a + b + c + m * (d + e)
    efficiency = 1.0 * numerator / denominator
    return efficiency

def process_entry(line):
    label, numbers = parse_line(line)
    efficiency = compute_efficiency(numbers)
    return efficiency, label

def process_case(n):
    data = []
    for i in range(n):
        line = read_data_line()
        entry = process_entry(line)
        data.append(entry)
    return data

def sort_data(data):
    return sorted(data, key=lambda x: (-x[0], x[1]))

def print_labels(sorted_data):
    for entry in sorted_data:
        print(entry[1])

def print_case_separator():
    print('#')

def process():
    while True:
        n = read_input()
        if n == 0:
            break
        data = process_case(n)
        sorted_data = sort_data(data)
        print_labels(sorted_data)
        print_case_separator()

class Main(object):
    def __init__(self):
        pass
    def solve(self):
        process()

if __name__ == '__main__':
    m = Main()
    m.solve()