from string import digits, ascii_uppercase

def parse(S, N, R):
    """
    Parse and evaluate an expression S describing a sequence of transformations
    on a list of indices ranging from 0 to N-1, where each letter in S corresponds
    to a predefined permutation in R. The expression may contain exponents and
    summations (union/intersection defined by '+').

    Parameters:
    - S (str): The input expression string to parse.
    - N (int): The size of the permutation (the number of elements).
    - R (dict): A dictionary mapping uppercase letters 'A'-'Z' to lists representing permutations.

    Returns:
    - list[int]: The resulting permutation after evaluating the expression.
    """
    # Append a sentinel character to mark the end of the string
    S = S + "$"
    cur = 0  # Current position index in the string S

    def expr():
        """
        Parse an expression, which may be composed of one or more terms joined by '+'.
        Each term corresponds to a permutation resulting from either a letter or a powered
        permutation.

        Returns:
        - list[int]: The permutation resulting from evaluating the entire expression.
        """
        nonlocal cur
        # Initialize the result as the identity permutation (range(N))
        r0 = list(range(N))
        while True:
            # Evaluate the next term
            r = term()
            # Combine the current result r0 by applying the permutation r on it
            r0 = [r0[e] for e in r]
            # If the next character is not '+', end parsing this expression
            if S[cur] != '+':
                break
            # Move past the '+' character and continue to next term
            cur += 1
        return r0

    def term():
        """
        Parse a term in the expression, which can either be a number followed by
        a parenthesized expression (interpreted as exponentiation of a permutation),
        or a single uppercase letter representing a permutation.

        Returns:
        - list[int]: The permutation resulting from evaluating the term.
        """
        nonlocal cur
        if S[cur] in digits:
            # If the term starts with digits, interpret as exponent k applied to an expression
            k = number()  # parse the exponent number k
            if S[cur] == '(':
                cur += 1  # skip '('
                r = expr()  # parse the inner expression
                cur += 1  # skip ')'
            else:
                # No parentheses, interpret as exponent applied to identity (no-op)
                r = identity()
            # Apply exponentiation of permutation r to the power k
            r = power(r, k)
        else:
            # Term is a single letter representing a permutation in R
            r = identity()
        return r

    def power(r, k):
        """
        Compute the k-th power (composition) of the permutation r using binary exponentiation.

        Parameters:
        - r (list[int]): The permutation to raise to a power.
        - k (int): The exponent.

        Returns:
        - list[int]: The permutation r raised to the k-th power.
        """
        r0 = list(range(N))  # Start from the identity permutation
        r1 = r[:]  # Copy of r for repeated squaring
        while k:
            if k & 1:
                # Apply the current permutation r1 to r0 when the bit is set
                r0 = [r0[e] for e in r1]
            # Square the permutation r1 (compose r1 by itself)
            r1 = [r1[e] for e in r1]
            k >>= 1  # Shift bits to the right to process next bit
        return r0

    def number():
        """
        Parse a number starting at the current position in S.

        Returns:
        - int: The parsed integer.
        """
        nonlocal cur
        v = 0
        # Accumulate digit characters to build the number
        while S[cur] in digits:
            v = 10 * v + int(S[cur])
            cur += 1
        return v

    def identity():
        """
        Parse a single uppercase letter from S and return its associated permutation from R.

        Returns:
        - list[int]: The permutation corresponding to the letter at position cur.
        """
        nonlocal cur
        r = R[S[cur]]
        cur += 1
        return r

    # Parse the entire expression starting from the beginning of S
    return expr()

def main():
    """
    Main function that reads input data, builds the permutation dictionary,
    parses and evaluates each expression, and prints the resulting permutations.
    """
    # Read N (size) and K (number of named permutations)
    N, K = map(int, input().split())
    R = {}  # Dictionary to store permutations by their letter names

    # For each named permutation:
    for _ in range(K):
        p, h = input().split()  # 'p' is letter, 'h' is the number of lines describing swaps
        h = int(h)
        r = list(range(N))  # Start from the identity permutation
        # For h - 1 lines, read line of indicators describing swaps between adjacent elements
        for _ in range(h - 1):
            g = list(map(int, input().split()))
            # Perform swaps between adjacent elements in r depending on g[j]
            for j in range(N - 1):
                if g[j]:
                    r[j], r[j + 1] = r[j + 1], r[j]
        R[p] = r  # Store the resulting permutation mapped to letter 'p'

    # Number of expressions to evaluate
    E = int(input())
    for _ in range(E):
        S = input()  # Read expression string
        res = parse(S, N, R)  # Parse and evaluate the expression
        # Print the resulting permutation with 1-based indexing
        print(*map(lambda x: x + 1, res))

# Entry point for the program
main()