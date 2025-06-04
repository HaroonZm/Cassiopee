from sys import stdin
from functools import cache

@cache
def compute_solution(n: int) -> int:
    return n // 3

def main():
    n = int(stdin.readline())
    print(compute_solution(n))

if __name__ == "__main__":
    main()