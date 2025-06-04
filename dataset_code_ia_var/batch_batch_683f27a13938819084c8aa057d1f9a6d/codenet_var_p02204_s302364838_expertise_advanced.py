from itertools import cycle
import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    if m == 2:
        patterns = [[1, 2], [2, 1]]
        res = min(sum(x != y for x, y in zip(a, cycle(pattern[:n]))) for pattern in patterns)
        print(res)
        return

    x = sum(1 for i in range(1, n) if a[i] == a[i - 1])
    print(x)

main()