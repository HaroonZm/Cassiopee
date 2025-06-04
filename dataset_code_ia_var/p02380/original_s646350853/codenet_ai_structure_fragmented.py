import math

def read_input():
    return input()

def parse_input(input_str):
    return map(int, input_str.split())

def compute_radians(C):
    return math.radians(C)

def square(x):
    return x ** 2

def multiply(x, y):
    return x * y

def compute_c(a2, b2, ab, rC):
    return math.sqrt(a2 + b2 - 2 * ab * math.cos(rC))

def compute_area(ab, rC):
    return ab * math.sin(rC) / 2

def compute_perimeter(a, b, c):
    return a + b + c

def compute_height(b, rC):
    return b * math.sin(rC)

def format_output(S, L, h):
    return f"{S:.5f} {L:.5f} {h:.5f}"

def main():
    inp = read_input()
    a, b, C = parse_input(inp)
    rC = compute_radians(C)
    a2 = square(a)
    b2 = square(b)
    ab = multiply(a, b)
    c = compute_c(a2, b2, ab, rC)
    S = compute_area(ab, rC)
    L = compute_perimeter(a, b, c)
    h = compute_height(b, rC)
    result = format_output(S, L, h)
    print(result)

main()