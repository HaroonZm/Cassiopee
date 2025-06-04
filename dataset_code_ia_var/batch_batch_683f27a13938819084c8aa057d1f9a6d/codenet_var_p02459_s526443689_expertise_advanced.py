from sys import stdin
from collections import defaultdict

def main():
    d = defaultdict(int)
    lines = iter(stdin.read().splitlines())
    q = int(next(lines))
    for line in (next(lines) for _ in range(q)):
        match line.split():
            case ["0", key, value]:
                d[key] = int(value)
            case ["1", key]:
                print(d[key])
main()