from sys import stdin
from math import inf

def solve(r, stones):
    n = len(stones)
    W = stones
    total_states = 1 << n
    memo = [{} for _ in range(total_states)]
    # memo[mask]: dict weight -> width

    # Initialize: single stones
    for i, w in enumerate(W):
        memo[1 << i][w] = 0.0

    for mask in range(1, total_states):
        if bin(mask).count('1') == 1:
            continue
        submask = (mask - 1) & mask
        while submask:
            left = submask
            right = mask ^ left
            if right == 0:
                submask = (submask - 1) & mask
                continue

            for wL, widthL in memo[left].items():
                for wR, widthR in memo[right].items():
                    Wsum = wL + wR
                    # Calculate distances a and b
                    a = wR / Wsum
                    b = wL / Wsum
                    width = widthL + widthR + a + b
                    # Insert (Wsum, width) into memo[mask], keep only widest for each weight
                    d = memo[mask]
                    if wL+wR not in d or d[wL+wR] < width:
                        d[wL+wR] = width
            submask = (submask - 1) & mask
        # Keep only max width per weight in memo[mask]
        # No need because previous update already keeps max

    # Extract max width among all weights in memo[total_states-1] not exceeding r
    res = -1
    for width in memo[total_states-1].values():
        if width < r and width > res:
            res = width
    return res

def main():
    input = iter(stdin.read().strip().split())
    T = int(next(input))
    for _ in range(T):
        r = float(next(input))
        s = int(next(input))
        stones = [int(next(input)) for __ in range(s)]
        ans = solve(r, stones)
        if ans < 0:
            print(-1)
        else:
            print(ans)

if __name__ == "__main__":
    main()