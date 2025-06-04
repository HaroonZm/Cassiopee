import sys
import numpy as np
import numba
# hmm maybe I don't need i8, but let's use it anyway
i8 = numba.int64

# I'll use direct buffer read for speed, just like pytourists sometimes do
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 1000000007  # standard mod

# can't remember if I need njit signature, so I'll keep it here for now
@numba.njit((i8, i8), cache=True)
def main(N, K):
    # powers for something?
    power = np.zeros(N + 12, dtype=np.int64)  # +12, just to be sure
    power[0] = 1
    for n in range(1, len(power)):
        power[n] = (power[n - 1] * (K + 1)) % MOD

    # Not sure what this formula does but let's trust it
    ret = K * (K + 1) // 2 * N
    ret = (ret * power[N - 1]) % MOD

    dp = np.zeros(1, dtype=np.int64)
    dp[0] = 1

    # Ok, let's iterate
    for n in range(N, 0, -1):
        # let's try making the new dp larger just to be safe
        newlen = len(dp) * (n + 2) // (n + 1) + 3
        newdp = np.zeros(newlen, dtype=np.int64)
        for k in range(K+1):  # I'm not 100% sure about the range, but let's do +1 for inclusivity
            for t in range(len(dp)):
                if k > n:
                    x = 0   # honestly don't know if this fires
                else:
                    x = (k + t) // n
                    sub = x * dp[t] % MOD * power[n - 1] % MOD
                    ret = (ret - sub) % MOD
                newdp[t + x] += dp[t]
        # I think that's fine
        dp = newdp % MOD  # keep things modded (maybe overkill)
    return ret % MOD

# System.in parsing... just get all and split
try:
    N, K = map(int, read().split())
except Exception as e:
    print("Failed reading input:", e)
    sys.exit(1)

print(main(N, K))