def solve():
    """
    Main function that computes a special combinatorial property of a given number.
    Given a number as a string of digits, the function counts the number of ways to arrange digits 
    into new numbers (with the same number of digits and same digit sum) such that the product of (d+1)
    (over all digits 'd') is strictly less than the original number, plus other carefully crafted cases.
    
    This is achieved via dynamic programming and recursion.
    """
    D = input()  # Read input number as a string.
    N = len(D)  # Number of digits in the input number.

    # Convert input string to a list of digits as integers.
    DI = list(map(int, D))

    # Calculate the sum of the digits of the input number.
    su = sum(DI)

    # Calculate the product of (digit+1) for each digit in the input.
    pd = 1
    for d in D:
        pd *= int(d) + 1

    # Prepare memoization tables for two recursive functions.
    memo = [{} for _ in range(N)]
    memo1 = [{} for _ in range(N)]

    def dfs0(i, s, p):
        """
        Explore all numbers of N digits, digit sum 'su', (d+1) product 'p',
        and count if their (d+1) product is strictly less than that for the input number.
        
        Args:
            i (int): Current digit index being processed (0-based).
            s (int): Remaining sum of digits to be assigned.
            p (int): Current product of (digit+1) so far.
        
        Returns:
            int: Number of valid combinations built so far.
        """
        key = (s, p)
        # If we've filled all digits
        if i == N:
            # If sum of digits left > 0, or (if sum is 0 but product incomplete) => valid
            return s > 0 or (s == 0 and p < pd)
        # Check if already computed.
        if key in memo[i]:
            return memo[i][key]
        r = 0
        # For each possible digit for the current position, from 0 up to min(s,9)
        for v in range(min(s, 9) + 1):
            # Recurse for next digit, with s reduced by v and product multiplied by (v+1)
            r += dfs0(i + 1, s - v, p * (v + 1))
        # Memoize and return
        memo[i][key] = r
        return r

    def dfs1(i, s, p, m):
        """
        Count numbers strictly less than D, matching all of the original constraints,
        using digit dynamic programming with an exact bound.
        
        Args:
            i (int): Current digit index being processed.
            s (int): Remaining sum of digits to pick.
            p (int): Remaining product that (d+1) digits need to multiply to.
            m (int): Bound indicator (0 means must match D up to now, 1 means unconstrained).
        
        Returns:
            int: Number of valid numbers found.
        """
        key = (s, p, m)
        # If all digits assigned
        if i == N:
            # Check tight constraint: all digits used, product exactly 1 (all p divided out)
            return s == 0 and p == 1
        # If already computed
        if key in memo1[i]:
            return memo1[i][key]
        r = 0
        # Minimum achievable digit: to prevent choosing digits too small, as later positions can't make up the sum
        b = s - (N - 1 - i) * 9
        # The digit at position i in D (the upper bound when m==0)
        di = DI[i]
        # Try all valid digits for this position
        for v in range(max(b, 0), min(s, 9) + 1):
            # p must be divisible by (v+1) to ensure valid factorization
            if p % (v + 1):
                continue
            if m == 0:
                # Must adhere to the input digit limit
                if di < v:
                    # Can't exceed original digit at this position if tight bound
                    break
                # If current digit equals input digit, keep bound tight; else, it's loose for subsequent digits
                r += dfs1(i + 1, s - v, p // (v + 1), 1 if v < di else 0)
            else:
                # Already loose, so try all digits
                r += dfs1(i + 1, s - v, p // (v + 1), 1)
        # Memoize and return
        memo1[i][key] = r
        return r

    # Count numbers with the same digit sum and length, with product strictly less than pd
    res1 = dfs0(0, su, 1)
    # Count numbers tightly bounded by D, with (d+1) product exactly pd, exclude D itself at the end
    res2 = dfs1(0, su, pd, 0) - 1

    # Total answer: all valid arrangements plus tight ones below original
    ans = res1 + res2
    print(ans)
    
solve()