from functools import lru_cache
from operator import xor

@lru_cache(maxsize=None)
def f(n: int) -> int:
    return (n, 1, n+1, 0)[n % 4]

def main():
    a, b = map(int, input().split())
    print(xor(f(a - 1), f(b)))

if __name__ == "__main__":
    main()