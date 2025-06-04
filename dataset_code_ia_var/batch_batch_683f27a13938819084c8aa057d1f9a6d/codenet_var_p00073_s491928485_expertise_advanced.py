from math import hypot
from sys import stdin

def process_inputs():
    lines = iter(stdin.readline, '')
    for x_str, h_str in zip(lines, lines):
        x, h = map(int, (x_str, h_str))
        if not (x or h):
            break
        t = hypot(h, x / 2)
        print(x * x + 2 * x * t)

if __name__ == "__main__":
    process_inputs()