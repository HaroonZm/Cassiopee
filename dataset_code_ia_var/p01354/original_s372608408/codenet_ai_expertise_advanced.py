import sys
import numpy as np

sys.setrecursionlimit(10**7)
INF = float('inf')
EPS = 1e-13
MOD = 10**9 + 7
DD = [(-1,0),(0,1),(1,0),(0,-1)]
DDN = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [x - 1 for x in map(int, sys.stdin.readline().split())]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip('\n')
def pf(s): print(s, flush=True)

from functools import lru_cache

def main():
    results = []
    while True:
        n, m = map(int, sys.stdin.readline().split())
        if n == 0:
            break
        a = np.array([LF() for _ in range(n)])  # shape (n, m)
        state_num = 1 << n
        dp = np.zeros((state_num, n))  # (mask, person): maximum expected value
        prev = np.zeros(state_num)
        for turn in range(m-1, -1, -1):
            ka = a[:, turn]
            new_dp = np.zeros_like(dp)
            updated = np.zeros(state_num)
            for mask in range(1, state_num):
                best = 0.0
                for person in range(n):
                    if not (mask & (1 << person)): continue
                    prev_mask = mask ^ (1 << person)
                    val = ka[person] * dp[mask, person] + (1 - ka[person]) * prev[prev_mask]
                    if val > new_dp[mask, person]:
                        new_dp[mask, person] = val
                    if val > updated[mask]:
                        updated[mask] = val
            dp = new_dp
            prev = updated
        results.append(f"{prev[-1]:.10f}")
        break
    return '\n'.join(results)

print(main())