import itertools

def main():
    """
    Main entry point of the program. Processes the input string and computes the number of possible distinct
    strings reachable via the specified transformation rules.
    """
    S = input()
    N = len(S)

    # Case 1: If all characters are the same, only one pattern is possible.
    if all(S[0] == c for c in S):
        print(1)
        return

    # Case 2: For strings of length 2, handle manually
    if N == 2:
        print(1 if S[0] == S[1] else 2)
        return

    # Case 3: For strings of length 3, execute custom exhaustive search
    if N == 3:
        def another(a, b):
            """
            Given two different characters from 'a', 'b', 'c', returns the third character not among {a, b}.
            
            Args:
                a (str): First character.
                b (str): Second character.

            Returns:
                str: The third character from {'a','b','c'}.
            """
            s = set('abc')
            s -= set([a, b])
            return list(s)[0]

        patterns = set()
        stack = [S]
        # Perform DFS to explore all transformations
        while stack:
            seq = stack.pop()
            patterns.add(seq)
            # Transform first two letters if they're different
            if seq[0] != seq[1]:
                transformed = another(seq[0], seq[1]) * 2 + seq[2]
                if transformed not in patterns:
                    stack.append(transformed)
            # Transform last two letters if they're different
            if seq[1] != seq[2]:
                transformed = seq[0] + another(seq[1], seq[2]) * 2
                if transformed not in patterns:
                    stack.append(transformed)
        print(len(patterns))
        return

    # Case 4: For strings of length >= 4, use dynamic programming
    MOD = 998244353  # Modulo for output to prevent integer overflow

    # dp[sum_mod_3][last_letter][has_adjacent_same] = count
    # sum_mod_3: sum of char values mod 3
    # last_letter: last character as 0 ('a'), 1 ('b'), 2 ('c')
    # has_adjacent_same: 1 if there exists adjacent equal chars, 0 otherwise
    dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(3)]

    # Initialize dp for all possible 4-letter combinations
    # Map 'a', 'b', 'c' to integers 0, 1, 2
    for ptn in itertools.product(range(3), repeat=4):
        # Checks if there is any pair of identical adjacent characters
        has_adjacent = (ptn[0] == ptn[1] or ptn[1] == ptn[2] or ptn[2] == ptn[3])
        sum_mod_3 = sum(ptn) % 3
        last_letter = ptn[3]
        dp[sum_mod_3][last_letter][has_adjacent] += 1

    # Propagate DP through the rest of string positions up to length N
    for n in range(4, N):
        dp_next = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(3)]
        for sum_prev in range(3):
            for last in range(3):
                for has_adj in range(2):
                    for next_letter in range(3):
                        # Update cumulative sum modulo 3
                        sum_new = (sum_prev + next_letter) % 3
                        # Update adjacent flag if new char matches previous
                        has_adj_new = has_adj or (last == next_letter)
                        dp_next[sum_new][next_letter][has_adj_new] += dp[sum_prev][last][has_adj]
                        dp_next[sum_new][next_letter][has_adj_new] %= MOD
        dp = dp_next

    # Compute sum of character values for original string modulo 3
    sum_S = 0
    for c in S:
        sum_S += ord(c) - ord('a')

    # Check if original string has any adjacent identical characters
    has_adj_same = False
    for c1, c2 in zip(S, S[1:]):
        if c1 == c2:
            has_adj_same = True
            break

    # Final answer: sum all dp entries matching the original string's sum modulo 3 and where adjacent repetition exists
    ans = sum([dp[sum_S % 3][i][1] for i in range(3)])
    # If the original string had no adjacent identical chars, add 1 for itself (as it can't be obtained via transformations)
    if not has_adj_same:
        ans += 1
    print(ans % MOD)

if __name__ == "__main__":
    main()