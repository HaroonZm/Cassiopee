from sys import stdin
from collections import defaultdict

def main():
    D = {}
    input_lines = iter(stdin.read().splitlines())
    q = int(next(input_lines))
    for line in (next(input_lines) for _ in range(q)):
        op, *args = line.split()
        if op == '0':
            D[args[0]] = args[1]
        else:
            print(D[args[0]])

if __name__ == "__main__":
    main()