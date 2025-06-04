from math import hypot, pow
from sys import stdin

def main():
    n = int(stdin.readline())
    x = list(map(int, stdin.readline().split()))
    y = list(map(int, stdin.readline().split()))
    diffs = [abs(a - b) for a, b in zip(x, y)]
    p1 = sum(diffs)
    p2 = pow(sum(d ** 2 for d in diffs), 0.5)
    p3 = pow(sum(d ** 3 for d in diffs), 1.0 / 3)
    pn = max(diffs)
    print(p1)
    print(p2)
    print(p3)
    print(pn)

if __name__ == '__main__':
    main()