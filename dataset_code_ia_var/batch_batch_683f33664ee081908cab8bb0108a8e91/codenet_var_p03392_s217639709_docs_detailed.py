def solve(s):
    """
    Solve the problem for a given string `s` according to specific rules.

    The function processes the input string `s` and returns an integer based on:
    - Special logic for short strings (length 2 or 3).
    - For longer strings, a dynamic programming approach with 3 states, updating for each character.
    - The DP state represents the number of ways to color/arrange with different rules.
    - Uses modulus 998244353 for all computations.

    Args:
        s (str): Input string.

    Returns:
        int: The computed result according to the described rules.
    """
    # Case 1: If string has length 2
    if len(s) == 2:
        # If both characters are the same, only 1 way, else 2
        return 1 if s[0] == s[1] else 2

    # Case 2: If string has length 3
    elif len(s) == 3:
        if s[0] == s[1] == s[2]:
            # All characters same: only one way
            return 1
        elif s[0] == s[1] or s[1] == s[2]:
            # Two adjacent characters are the same
            return 6
        elif s[0] == s[2]:
            # First and last character are the same, middle is different
            return 7
        else:
            # All characters are different
            return 3

    # Case 3: If all characters in string are the same for any length
    if all(a == b for a, b in zip(s, s[1:])):
        return 1

    # Otherwise, use dynamic programming for longer strings

    # Initialize a 3D DP array:
    # dp[m][x][y] where:
    # m: 0 or 1 (flips/operations count)
    # x: current color state (0, 1, or 2)
    # y: previous color state (0, 1, or 2)
    dp = [[[0] * 3 for _ in range(3)] for _ in range(2)]
    # Base cases: initiate first color assignment
    dp[0][0][0] = 1
    dp[0][1][1] = 1
    dp[0][2][2] = 1

    MOD = 998244353  # Problem-specific modulus for all operations

    # Iterate over each position in the string except the first (adjust size accordingly)
    for _ in range(len(s) - 1):
        # Create a new dp array for the next iteration
        ndp = [[[0] * 3 for _ in range(3)] for _ in range(2)]

        # No flip cases (m = 0)
        # Compute all possible transitions for color states
        ndp[0][0][0] = (dp[0][1][0] + dp[0][2][0]) % MOD
        ndp[0][0][1] = (dp[0][1][1] + dp[0][2][1]) % MOD
        ndp[0][0][2] = (dp[0][1][2] + dp[0][2][2]) % MOD

        ndp[0][1][0] = (dp[0][0][2] + dp[0][2][2]) % MOD
        ndp[0][1][1] = (dp[0][0][0] + dp[0][2][0]) % MOD
        ndp[0][1][2] = (dp[0][0][1] + dp[0][2][1]) % MOD

        ndp[0][2][0] = (dp[0][0][1] + dp[0][1][1]) % MOD
        ndp[0][2][1] = (dp[0][0][2] + dp[0][1][2]) % MOD
        ndp[0][2][2] = (dp[0][0][0] + dp[0][1][0]) % MOD

        # Flip/operation cases (m = 1)
        ndp[1][0][0] = (dp[0][0][0] + dp[1][0][0] + dp[1][1][0] + dp[1][2][0]) % MOD
        ndp[1][0][1] = (dp[0][0][1] + dp[1][0][1] + dp[1][1][1] + dp[1][2][1]) % MOD
        ndp[1][0][2] = (dp[0][0][2] + dp[1][0][2] + dp[1][1][2] + dp[1][2][2]) % MOD

        ndp[1][1][0] = (dp[0][1][2] + dp[1][0][2] + dp[1][1][2] + dp[1][2][2]) % MOD
        ndp[1][1][1] = (dp[0][1][0] + dp[1][0][0] + dp[1][1][0] + dp[1][2][0]) % MOD
        ndp[1][1][2] = (dp[0][1][1] + dp[1][0][1] + dp[1][1][1] + dp[1][2][1]) % MOD

        ndp[1][2][0] = (dp[0][2][1] + dp[1][0][1] + dp[1][1][1] + dp[1][2][1]) % MOD
        ndp[1][2][1] = (dp[0][2][2] + dp[1][0][2] + dp[1][1][2] + dp[1][2][2]) % MOD
        ndp[1][2][2] = (dp[0][2][0] + dp[1][0][0] + dp[1][1][0] + dp[1][2][0]) % MOD

        # Move to next dp state
        dp = ndp

    # Calculate the color sum modulo 3, based on the ordinals of the string characters
    color_sum_mod3 = sum(map(ord, s)) % 3

    # Sum up results for all possible colorings with m=1 and the calculated color sum
    result = sum(dp[1][x][color_sum_mod3] for x in range(3))

    # Add 1 if all adjacent characters in the original string are different (i.e., s is a "rainbow" string)
    result += all(a != b for a, b in zip(s, s[1:]))

    # Return the result modulo MOD
    return result % MOD

# Main input/output section
if __name__ == "__main__":
    s = input()
    print(solve(s))