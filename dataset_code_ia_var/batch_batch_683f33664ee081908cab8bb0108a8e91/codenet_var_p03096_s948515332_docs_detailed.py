def solve():
    """
    Main function to compute the number of ways to arrange the input sequence with specific constraints.
    The approaches and procedures follow dynamic programming (DP) with optimizations based on colors
    and avoiding consecutive duplicates.

    Reads:
        - N: number of elements in input.
        - X: list of integers representing colors or values.

    Outputs:
        - Number of possible arrangements modulo 10^9+7.
    """

    # Read the number of elements
    N = int(input())
    # Read each color/value in the sequence
    X = [int(input()) for _ in range(N)]
    MOD = int(1e9) + 7  # Modulus for large numbers

    # Remove consecutive duplicates in X to form a new sequence
    colors = set()       # To track unique colors
    NoDouble = [-1]      # To build new sequence starting with sentinel

    for x in X:
        colors.add(x)
        if x == NoDouble[-1]:
            # Skip consecutive duplicates
            continue
        NoDouble.append(x)
    del NoDouble[0]      # Remove sentinel value
    N = len(NoDouble)    # Reassign N to new sequence length
    C = len(colors)      # Number of unique colors (not used further in this code)

    # ForIdxLastNum[i]: for the i-th item in NoDouble, the index of its previous appearance (-1 if first occurrence)
    ForIdxLastNum = [-1] * N
    # Onetime_colors[c]: For each color c, store the latest index where it's found
    Onetime_colors = [-1] * (2 * 10**5 + 1)  # Handles large color range

    for idx, color in enumerate(NoDouble):
        if Onetime_colors[color] == -1:
            # First appearance of this color
            Onetime_colors[color] = idx
        else:
            # Already appeared before; store previous index for DP reference
            ForIdxLastNum[idx] = Onetime_colors[color]
            Onetime_colors[color] = idx

    # DP[i]: number of ways to arrange the first i elements
    DP = [0] * (N + 1)
    DP[0] = 1  # Base case: 1 way to arrange zero elements (empty sequence)

    for idx, color in enumerate(NoDouble):
        if ForIdxLastNum[idx] == -1:
            # This color hasn't appeared before: same as previous count
            DP[idx + 1] = DP[idx]
        else:
            # Add the cases by extending from the previous occurrence
            lastIdx = ForIdxLastNum[idx]
            DP[idx + 1] = (DP[lastIdx + 1] + DP[idx]) % MOD

    # Output the final answer modulo MOD
    print(DP[N] % MOD)


if __name__ == "__main__":
    solve()