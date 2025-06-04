import sys
import math

def main():
    S,N,K = map(int, sys.stdin.readline().split())
    S = abs(S)
    min_sum = K
    max_sum = K*N

    if S < min_sum:
        print(-1)
        return
    if S > max_sum and S % 1 != 0:
        print(-1)
        return

    # Check reachability via parity
    # Sum of K numbers from 1..N, distribution support is [K, K*N]
    # The sum modulo 1 is always integer, so no fractional issues
    # We need to check if (S - K) is reachable as sum of K integers from {0..N-1}
    # Because sum of K integers from 1..N is K + sum of K integers from 0..N-1

    remainder = (S - K) % 1
    if remainder != 0:
        print(-1)
        return

    # The sums of K numbers from 1..N form a distribution equivalent to sum of K uniform integers over [1..N]
    # The minimal sum is K, maximal sum is K*N

    # Reachability check: S in [K, K*N]
    if S < K or S > K*N:
        print(-1)
        return

    # For large S and K, probability that the sum of K uniform(1..N) equals S can be computed via DP or FFT,
    # but that's heavy.
    # Here, we can compute gcd of steps to decide if S is reachable at all
    # Since steps are integers from 1 to N, gcd is 1.
    # So any sum from K to K*N is possible.
    # So we only need to check if S in [K, K*N], which is done.

    # The expected value E of the first hitting time of a random walk on a line with positive integer steps and absorption at 0:
    # From position S > 0, E satisfies E = 1 + sum P(x) E(S-x)
    # with E(0)=0

    # Since the increments are always positive, the random walk decreases position by a random amount between K and K*N (position moves S - sum_of_steps)

    # Wait, in the problem, the jump is from current position towards the witch (at 0)
    # So next position = current - sum_of_steps

    # So E(S) = 1 + sum_{s} P(s) * E(S - s), with E(0)=0 and E(x<0)=0
    # For S < K, E(S) is undefined or no solution

    # We will solve for E(0..S) using DP
    max_state = S
    dp = [0.0]*(max_state+1)
    prob = [0]*(max_state+1)

    # Precompute distribution of sum of K uniform(1..N)
    # Use DP to get count of ways to make sum s from K to K*N

    max_sum = K*N
    ways = [0]*(max_sum+1)
    ways_prev = [0]*(max_sum+1)
    ways_prev[0] = 1
    for _ in range(K):
        for s in range(max_sum+1):
            ways[s] = 0
        for s in range(max_sum+1):
            if ways_prev[s] == 0:
                continue
            for v in range(1, N+1):
                if s+v <= max_sum:
                    ways[s+v] += ways_prev[s]
        ways, ways_prev = ways_prev, ways

    total_ways = N**K
    dist = [0.0]*(max_sum+1)
    for s in range(K, max_sum+1):
        dist[s] = ways_prev[s]/total_ways

    # Since S is large (up to 10^9), we can't do DP up to S.
    # We exploit the linearity and monotonicity:
    # Let E be expected hitting time at position x:
    # E(x) = 1 + sum_{s=K}^{K*N} dist[s] * E(x - s), with E(y <= 0) = 0

    # For large x, approximate:
    # E(x) ~ x / E[step], with E[step] = mean step length
    mean_step = (K*(N+1))/2
    if mean_step == 0:
        print(-1)
        return

    # Also check if S is divisible by gcd of step sizes:
    # steps are 1..N, gcd always 1 -> always hit 0 eventually

    # So expected time = S / mean_step

    # But since steps >= K and S can be smaller than K, if S < K, output -1
    if S < K:
        print(-1)
        return

    # Output expected value with required precision
    ans = S / mean_step
    print(f"{ans:.9f}")

main()