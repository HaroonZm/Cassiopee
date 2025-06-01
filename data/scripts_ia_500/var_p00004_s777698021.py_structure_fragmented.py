def read_input():
    return input()

def parse_input(input_str):
    return map(int, input_str.split())

def compute_x(a, b, c, d, e, f):
    numerator = c * d - a * f
    denominator = b * d - a * e
    return numerator / denominator

def compute_y(a, b, c, x):
    numerator = c - b * x
    return numerator / a

def format_output(y, x):
    return "{:.3f} {:.3f}".format(y, x)

def print_output(output):
    print(output)

def main_loop():
    while True:
        try:
            input_str = read_input()
            a, b, c, d, e, f = parse_input(input_str)
            x = compute_x(a, b, c, d, e, f)
            y = compute_y(a, b, c, x)
            output = format_output(y, x)
            print_output(output)
        except:
            break

main_loop()