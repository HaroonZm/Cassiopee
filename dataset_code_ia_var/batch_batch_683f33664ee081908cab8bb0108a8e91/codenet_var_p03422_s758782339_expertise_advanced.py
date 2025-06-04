from math import ceil
from sys import stdin

def solve(a: int, k: int) -> int:
    if a < k:
        return 0
    while r := a % k:
        m = a // k + 1
        a -= ((-(-r // m)) * m)
    return a // k

n = int(stdin.readline())
ans = 0
for _ in range(n):
    a, k = map(int, stdin.readline().split())
    ans ^= solve(a, k)
print("Aoki" if ans == 0 else "Takahashi")