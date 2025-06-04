import sys
from operator import mul
from itertools import starmap

sys.setrecursionlimit(10**7)

INF_INT = 10**20
INF_FLOAT = float('inf')
MOD = 10**9 + 7
DIRS_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRS_8 = DIRS_4 + [(-1, 1), (1, 1), (1, -1), (-1, -1)]
DIRS_9 = DIRS_8 + [(0, 0)]

def solve():
    N, A, B = map(int, sys.stdin.readline().split())
    low, high = starmap(lambda op1, op2: op1*(N-1) + op2, [(A, B), (B, A)])
    ans = max(0, high - low + 1)
    print(ans)

if __name__ == '__main__':
    solve()