from sys import stdin
from itertools import combinations

def main():
    n = int(stdin.readline())
    parity = n % 2
    offset = n - 2 + (parity ^ 1)
    print((n * (n - 2) // 2) if parity == 0 else (((n - 1) * (n - 2) + (n - 1)) // 2))
    forbidden = {frozenset({i, offset - i}) for i in range(n) if i < (offset - i) < n}
    for i, j in combinations(range(n), 2):
        if frozenset({i, j}) not in forbidden:
            print(i + 1, j + 1)

if __name__ == "__main__":
    main()