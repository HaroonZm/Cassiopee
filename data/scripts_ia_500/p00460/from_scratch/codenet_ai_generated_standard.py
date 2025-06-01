import sys
sys.setrecursionlimit(10**7)

MOD = 100000

def solve(N, M, S):
    total = N * N
    # dp[pos][last][sum] = number of ways to choose pos numbers > last with sum = sum
    # Because sum can be up to 3000, we handle sum dimension
    # Use rolling dp for pos and last to reduce memory.
    # We know that numbers are strictly increasing sequence of length total from [1..M], sum to S.
    # After choosing, fill the matrix column-wise:
    # Because of the conditions:
    # - Numbers strictly increasing overall
    # - Numbers in each column strictly ascend by rows
    # - The card is filled in column order, so reading column by column, the numbers assigned form a strictly increasing sequence.
    # So, the problem reduces to counting strictly increasing sequences of length total with elements in [1..M] and sum S.

    # dp[pos][k]: map from sum -> count of sequences of length pos ending at k
    # Huge state - optimize:
    # We'll use dp[pos][last][sum], but last can be from 0 to M,
    # For each pos, we build for next pos by choosing next number > last.
    # Implement dp with 2D dp: dp[last][sum]

    from collections import defaultdict

    dp_prev = [defaultdict(int) for _ in range(M+2)]
    # Base case: pos=0, sum=0, last=0 (no number chosen)
    dp_prev[0][0] = 1

    for _ in range(total):
        dp_cur = [defaultdict(int) for _ in range(M+2)]
        for last in range(M+1):
            dp_dict = dp_prev[last]
            if not dp_dict:
                continue
            for s, cnt in dp_dict.items():
                start = last + 1
                # number can be chosen from start to M
                # To speed up, we iterate from start to M, add cnt to dp_cur[num][s+num]
                # Check s+num <= S
                for num in range(start, M+1):
                    ns = s + num
                    if ns > S:
                        break
                    dp_cur[num][ns] = (dp_cur[num][ns] + cnt) % MOD
        dp_prev = dp_cur

    ans = 0
    for last in range(1, M+1):
        ans = (ans + dp_prev[last][S]) % MOD
    return ans

for line in sys.stdin:
    N, M, S = map(int, line.split())
    if N == 0 and M == 0 and S == 0:
        break
    print(solve(N, M, S))