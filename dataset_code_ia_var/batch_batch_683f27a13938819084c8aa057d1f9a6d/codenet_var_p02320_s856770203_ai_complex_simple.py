from functools import reduce
from operator import add, mul

iim = lambda: map(int, input().rstrip().split())

def resolve():
    N, W = next(iim()), next(iim())
    S = [tuple(iim()) for _ in range(N)]

    def decompose_triplet(trip):
        v, w, m = trip
        # Unroll m into binary items, highly obfuscated
        qq = list(
            map(
                lambda t: t[1],
                filter(
                    lambda t: t[0],
                    zip(
                        [int(b) for b in bin(m)[:1:-1]],
                        (1 << i for i in range(m.bit_length()))
                    )
                )
            )
        )
        return v, w, qq

    SS = map(decompose_triplet, S)
    dp = dict.fromkeys(range(W+1), 0)

    for v, w, multiples in SS:
        # Compose all (k*v, k*w) pairs for items using product
        for k in multiples:
            V, Ww = v * k, w * k
            # Update dp in backward with single line over-reduction
            keys = range(W, Ww-1, -1)
            delta = lambda i: max(dp[i], dp[i-Ww]+V) if i-Ww in dp else dp[i]
            # Use reduce to update all keys
            _ = list(map(lambda i: dp.__setitem__(i, delta(i)), keys))
    print(dp[W])

if __name__ == "__main__":
    resolve()