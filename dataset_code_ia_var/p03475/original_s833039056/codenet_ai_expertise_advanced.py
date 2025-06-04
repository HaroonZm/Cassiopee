import sys
import math
from typing import List, Tuple

def solve():
    N = int(input())
    C, S, F = zip(*(map(int, input().split()) for _ in range(N - 1)))
    res = []
    for i in range(N - 1):
        t = 0
        for j in range(i, N - 1):
            if t <= S[j]:
                t = S[j] + C[j]
            else:
                t = S[j] + ((t - S[j] + F[j] - 1) // F[j]) * F[j] + C[j]
        res.append(t)
    res.append(0)
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    solve()