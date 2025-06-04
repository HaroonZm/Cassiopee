from functools import lru_cache
from sys import stdin

MOD = 10 ** 9 + 7

@lru_cache(maxsize=None)
def stirling(n, k):
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return (stirling(n - 1, k - 1) + stirling(n - 1, k) * k) % MOD

def main():
    n, k = map(int, stdin.readline().split())
    print(stirling(n, k))

if __name__ == "__main__":
    main()