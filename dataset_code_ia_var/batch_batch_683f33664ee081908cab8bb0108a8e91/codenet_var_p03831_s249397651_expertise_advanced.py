import sys
from typing import List

def input_ints() -> List[int]:
    return list(map(int, sys.stdin.readline().split()))

def main():
    n, a, b = input_ints()
    X = input_ints()
    from itertools import pairwise, accumulate, repeat

    # Using accumulate for a functional style; no explicit dp list manipulation
    def cost(prev, xi_xj):
        dist_cost = (xi_xj[1] - xi_xj[0]) * a
        return min(prev + dist_cost, prev + b)

    result = list(
        accumulate(
            pairwise(X),
            func=cost,
            initial=0
        )
    )

    print(result[-1])

if __name__ == "__main__":
    main()