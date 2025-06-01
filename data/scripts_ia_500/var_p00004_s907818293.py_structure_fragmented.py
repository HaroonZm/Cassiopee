import sys

def read_lines():
    return sys.stdin

def parse_line(line):
    return list(map(int, line.split()))

def compute_denominator(a, b, d, e):
    return a * e - b * d

def compute_x(a, b, c, d, e, f, denominator):
    numerator = c * e - b * f
    return numerator / denominator

def compute_y(a, b, c, d, e, f, denominator):
    numerator = a * f - c * d
    return numerator / denominator

def format_result(x, y):
    return "{0:.3f} {1:.3f}".format(x + 0.0, y + 0.0)

def process_line(line):
    a, b, c, d, e, f = parse_line(line)
    denominator = compute_denominator(a, b, d, e)
    x = compute_x(a, b, c, d, e, f, denominator)
    y = compute_y(a, b, c, d, e, f, denominator)
    result = format_result(x, y)
    print(result)

def main():
    lines = read_lines()
    for line in lines:
        process_line(line)

if __name__ == "__main__":
    main()