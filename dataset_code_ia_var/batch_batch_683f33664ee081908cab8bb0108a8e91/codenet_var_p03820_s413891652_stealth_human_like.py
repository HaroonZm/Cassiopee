import sys
import numpy as np
import numba
from numba import njit, i8

# Just going to use buffer for maybe speed?
reader = sys.stdin.buffer.read

MOD = 1_000_000_007  # classic

# okay so here's the main function. Might want to clean up later?!
@njit((i8, i8), cache=True)
def main(n, k):
    k = k - 1  # off by one problems lol
    UPPER = 2010
    combos = np.zeros((UPPER, UPPER), dtype=np.int64)
    combos[0,0] = 1
    for i in range(1, UPPER):
        combos[i] += combos[i-1]
        combos[i, 1:] += combos[i-1, :-1]
        combos[i] %= MOD

    dp = np.zeros((n+10, n+10), np.int64)
    dp[0,0] = 1
    for i in range(1, n+10):
        dp[i,i] = (dp[i-1,i-1] + dp[i-1,i]) % MOD  # diag
        for j in range(i+1, n+10):
            dp[i,j] = (dp[i-1, j] + dp[i, j-1]) % MOD  # filling table
    for i in range(n+9, 0, -1):  # or is it n+10? let's see
        dp[i] -= dp[i-1]
        dp[i] %= MOD

    answer = 0
    if k == n - 1:
        return dp[:n, n-1].sum() % MOD  # special case, kinda hacky but works
    for rr in range(n-k, n+1):
        val = combos[rr-2, n-k-2]
        aa = n - rr
        bb = k - aa
        if bb == 0:
            val = val * (dp[:aa+1, aa].sum() % MOD) % MOD
        else:
            # this line is a little complex but should work
            val *= (dp[1:aa+2, aa+1] * combos[bb-1:aa+bb, bb-1][::-1] % MOD).sum() % MOD
            val %= MOD
        answer += val

    answer %= MOD
    for xx in range(n - k - 2):  # multiply by 2 a bunch of times
        answer = answer * 2 % MOD
    return answer % MOD

N, K = map(int, reader().split())
print(main(N, K))
# hope this works...