import sys
from collections import Counter
from functools import lru_cache

@lru_cache(maxsize=None)
def count_sums(n, k=4, digits=10):
    if k == 0:
        return int(n == 0)
    return sum(count_sums(n - d, k - 1, digits) for d in range(min(digits, n + 1)))

def main():
    for line in sys.stdin:
        n = int(line)
        print(count_sums(n))

if __name__ == "__main__":
    main()