def main():
    """
    Main function to compute and print the result based on modification of input integers N and M.

    Steps:
        1. Decrements the input values N and M by 1, storing them as n and m.
        2. Applies conditional logic:
            - If both n and m are zero, sets ans to 1.
            - If exactly one of n or m is zero, sets ans to (n + m - 1).
            - Otherwise, sets ans to (n - 1) * (m - 1).
        3. Prints the result ans.

    Returns:
        None
    """
    # Decrement both input values by 1 to obtain n and m
    n = N - 1
    m = M - 1

    # Conditional logic to determine 'ans' value based on n and m
    if not n and not m:
        # Case: both n and m are zero
        ans = 1
    elif not n or not m:
        # Case: only one of n or m is zero
        ans = n + m - 1
    else:
        # Case: both n and m are non-zero
        ans = (n - 1) * (m - 1)

    # Output the result
    print(ans)

# Read space-separated integers from standard input and assign to N and M
N, M = [int(x) for x in input().split()]

if __name__ == "__main__":
    main()