from functools import reduce
from operator import add, mul
from itertools import accumulate, starmap, product, repeat, islice, chain

iim = lambda: map(int, input().rstrip().split())

def fancy_zeros(n, k):
    return int(n < k)

def fancy_ones(n, k):
    return int(n == 1 or k == 1)

def modinv(a, m):
    return pow(a, m-2, m)

def resolve():
    N, K = iim()
    mod = 10**9 + 7

    print(
        0 if fancy_zeros(N, K) else
        1 if fancy_ones(N, K) else
        next(
            islice(
                (
                    x % mod
                    for x in accumulate(
                        (
                            reduce(add,
                                (
                                    reduce(
                                        add,
                                        (
                                            (
                                                lambda dp, i, k: dp[i-1][k-1] + dp[i-k][k]
                                            )(dp, i, k) if k > 0 and i >= k else 0
                                            for k in range(1, K+1)
                                        ),
                                        0
                                    )
                                    for i in range(1, N+1)
                                ),
                                0
                            ),
                        for dp in (
                            [[int(i == 0 and k == 0) for k in range(K+1)] for i in range(N+1)],
                        )
                        )
                    ),
                ),
                N*(K+1) + K  # Skip to the last generated
            )
        )
    )

if __name__ == "__main__":
    resolve()