from math import log2, ceil
from sys import stdin

def solve():
    n, k = map(int, stdin.readline().split())
    result = sum((1/n) * 0.5**max(0, ceil(log2(k/i))) for i in range(1, n+1))
    print(result)

if __name__ == "__main__":
    solve()