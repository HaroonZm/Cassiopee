from functools import reduce
import sys

def parse_input():
    for line in sys.stdin:
        try:
            yield tuple(map(int, line.strip().split(',')))
        except ValueError:
            continue

def main():
    r = d = 0
    for a, b, c in parse_input():
        d += a == b
        r += a * a + b * b == c * c
    print(r)
    print(d)

if __name__ == "__main__":
    main()