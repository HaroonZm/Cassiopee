import sys
import math

def can_achieve(r, a):
    n = len(a)
    # DP[i] = set of possible b_i values for coin i with max confusion ratio r
    # To reduce search space, store only minimal and maximal possible values for b_i
    dp = [set() for _ in range(n)]
    # For first coin, b_0 must satisfy |a_0 - b_0|/a_0 <= r => b_0 in [a_0*(1 - r), a_0*(1 + r)]
    low0 = max(1, math.ceil(a[0]*(1 - r)))
    high0 = math.floor(a[0]*(1 + r))
    if low0 > high0:
        return False
    dp[0] = set(range(low0, high0 + 1))
    for i in range(1, n):
        dp[i] = set()
        # compute possible range for b_i
        low = max(1, math.ceil(a[i]*(1 - r)))
        high = math.floor(a[i]*(1 + r))
        if low > high:
            return False
        # For each b_{i-1} in dp[i-1], b_i must be divisible by b_{i-1} and in [low, high]
        # To optimize, collect all b_{i-1} values and for each, find multiples in [low, high]
        possible = set()
        prev_vals = sorted(dp[i-1])
        # To avoid too large sets, if dp[i-1] too big, prune to unique values only or intervals
        for prev in prev_vals:
            # calculate k s.t. k*prev in [low, high]
            k_min = (low + prev - 1) // prev
            k_max = high // prev
            if k_min <= k_max:
                for k in range(k_min, k_max + 1):
                    val = k * prev
                    possible.add(val)
        if not possible:
            return False
        dp[i] = possible
    return bool(dp[-1])

def main():
    input = sys.stdin.readline
    N = int(input())
    a = list(map(int, input().split()))
    left = 0.0
    right = 1.0
    for _ in range(60):
        mid = (left + right) / 2
        if can_achieve(mid, a):
            right = mid
        else:
            left = mid
    print(right)

if __name__ == "__main__":
    main()