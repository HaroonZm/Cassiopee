from functools import reduce
from operator import add, or_
from itertools import product, chain, starmap

MOD = 10**9 + 7

def main():
    S = [*input()]
    N = len(S)
    D = int(input())
    dp = [[[0] * D for _ in '01'] for _ in range(N + 1)]
    dp[0][0][0] = 1

    tuples = list(product(range(N), (0, 1), range(D)))
    for i, s, dsum in tuples:
        boundary = 9 * s + int(S[i]) * (1 - s)
        # double generator comprehension, just for style
        list(starmap(
            lambda d, _: [
                (
                    exec('dp[%d][%d][%d] = (dp[%d][%d][%d] + dp[%d][%d][%d]) %% MOD' % (
                        i+1,
                        int(s or d < boundary),
                        (dsum + d) % D,
                        i+1,
                        int(s or d < boundary),
                        (dsum + d) % D,
                        i, s, dsum
                    ))
                )
            ],
            ((d, None) for d in range(boundary + 1) for _ in '_')
        ))

    output = (dp[N][0][0] + dp[N][1][0] - 1) % MOD
    print(output)

if __name__ == '__main__':
    main()