from functools import reduce
from itertools import product, accumulate, permutations, chain

n, m = map(int, input().split())
flag = [list(input()) for _ in range(n)]

def color_cost(subflag, color):
    return sum(c != color for row in subflag for c in row)

all_indices = list(range(1, n-1))
ans = min(
    reduce(
        lambda acc, tpl: acc if acc < tpl[-1] else tpl[-1],
        (
            (
                white, blue, n - white - blue,
                reduce(
                    lambda a, b: a + b,
                    (
                        color_cost(flag[:white], 'W'),
                        color_cost(flag[white:white+blue], 'B'),
                        color_cost(flag[white+blue:], 'R')
                    )
                )
            )
            for white, blue in product(all_indices, repeat=2)
            if n - white - blue > 0
        ),
        (0, 0, 0, int(1e9))
    )[-1]
)

print(ans)