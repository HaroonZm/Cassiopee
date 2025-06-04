import sys
from math import isclose, sqrt

def main():
    readline = sys.stdin.buffer.readline

    N = int(readline())

    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))

    diffs = [abs(a - b) for a, b in zip(A, B)]

    l1 = float(sum(diffs))
    l2 = sqrt(sum(d ** 2 for d in diffs))
    l3 = sum(d ** 3 for d in diffs) ** (1 / 3)
    l_inf = float(max(diffs, default=0))

    print(l1, l2, l3, l_inf, sep='\n')

if __name__ == "__main__":
    main()