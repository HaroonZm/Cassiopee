from functools import reduce
from itertools import combinations, chain, starmap, product
from operator import or_, and_, xor

def resolve():
    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    full = 1 << n

    cost = list(
        map(
            lambda bits:
                sum(
                    map(
                        lambda ij: ab[ij[0]][ij[1]],
                        filter(lambda ij: (bits >> ij[0]) & 1 and (bits >> ij[1]) & 1,
                               combinations(range(n), 2)
                        )
                    )
                ),
            range(full)
        )
    )

    dp = [0 for _ in range(full)]

    for s in range(1, full):
        bitset = list(chain.from_iterable(
            starmap(
                lambda sz, _:
                    filter(lambda t: bin(t).count('1') == sz and t & s == t,
                           range(1, s+1)
                    ),
                product(range(1, bin(s).count('1')+1), [0])
            )
        ))
        _ = any([
            setattr(dp, '__setitem__', lambda idx, val:
                dp.__setitem__(idx, max(dp[idx], val))) or
            [dp.__setitem__(s, max(dp[s], dp[s-t] + cost[t])) for t in filter(lambda t: t > 0 and (t & s) == t, bitset)]
            for _ in [0]
        ])

    print(dp[-1])

if __name__ == "__main__":
    resolve()