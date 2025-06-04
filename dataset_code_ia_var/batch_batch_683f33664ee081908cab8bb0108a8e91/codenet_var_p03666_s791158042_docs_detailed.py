def can_reach_target(n, a, b, c, d):
    """Determine whether it is possible to obtain the integer b starting from a, 
    after performing (n-1) additions where each addition is either c or d.

    Args:
        n (int): The number of operations (including the initial value).
        a (int): The starting integer.
        b (int): The target integer to reach.
        c (int): The minimum allowed increment at each step.
        d (int): The maximum allowed increment at each step.

    Returns:
        str: 'YES' if it is possible to reach b from a in n-1 steps, 'NO' otherwise.
    """
    # Initialize the answer as 'NO' by default
    ans = 'NO'
    # The maximum value achievable: add the maximum possible increment (d) at each step
    maxi = a + d * (n - 1)
    # The minimum value achievable: add the minimum possible increment (c) at each step
    mini = a + c * (n - 1)
    # Check if b is within the initial possible range
    if mini <= b <= maxi:
        ans = 'YES'
    else:
        # Try all possible combinations by reducing both ends of the range in each iteration,
        # simulating choosing one 'c' and one 'd' less at certain positions, to cover all valid sums.
        for i in range(1, n):
            # Decrease the possible maximum and minimum by (d + c) for each alternative arrangement
            maxi = maxi - d - c
            mini = mini - d - c
            # Check if the current range includes b
            if mini <= b <= maxi:
                ans = 'YES'
                break
    return ans

if __name__ == "__main__":
    # Parse user input as five integers: n, a, b, c, and d
    n, a, b, c, d = map(int, input().split())
    # Evaluate whether it is possible to reach b and print the result
    print(can_reach_target(n, a, b, c, d))