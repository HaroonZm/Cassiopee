from collections import defaultdict

def parse_input():
    """
    Generator that reads input values from the user.

    Yields:
        int: The number of men for each test case.
    """
    while True:
        n = int(raw_input())
        if n == 0:
            break
        yield n

def read_schedule(n):
    """
    Reads the schedule and lifting values for n men.

    Args:
        n (int): Number of men.

    Returns:
        tuple: A tuple containing two lists.
            - L (list of int): The list of weights each man can lift.
            - T (list of int): The list of bitmasks representing each man's time slots.
    """
    L = [0] * n  # Lifting capacities for each man
    T = [0] * n  # Bitmask representing time availability for each man

    for man in xrange(n):
        m, l = map(int, raw_input().split())
        L[man] = l
        t = 0  # Bitmask for current man
        for _ in xrange(m):
            s, e = map(int, raw_input().split())
            # Set bits between s and e (hours normalized from 6 to 18 -> 0 to 12)
            t |= 2**(e-6) - 2**(s-6)
        T[man] = t
    return L, T

def compute_max_weight(L, T):
    """
    Computes the maximum total weight that can be lifted without time conflicts.

    Args:
        L (list of int): The list of weights each man can lift.
        T (list of int): The list of bitmasks representing each man's time slots.

    Returns:
        int: The maximum total weight.
    """
    dp = defaultdict(int)  # dp[bitmask]: maximum weight achievable with selected time slots

    for l, t in zip(L, T):
        # Create a list of current keys to avoid runtime error due to dictionary size change
        existing_masks = list(dp.keys())
        # Try combining the current man with all previous combinations if time slots do not overlap
        for bit in existing_masks:
            if bit & t == 0:  # No overlap in scheduled time
                new_mask = bit | t
                dp[new_mask] = max(dp[new_mask], dp[bit] + l)  # Update max weight for new mask
        # Update for mask including only current man's time slots
        dp[t] = max(dp[t], l)

    # Return the best achievable weight
    return max(dp.values())

def main():
    """
    Main function to handle the reading of inputs, computation,
    and output for each test case until input is terminated.
    """
    # Process each test case
    for n in parse_input():
        L, T = read_schedule(n)
        result = compute_max_weight(L, T)
        print result

# Entry point
if __name__ == "__main__":
    main()