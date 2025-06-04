def solve():
    """
    Reads input cases for a marathon problem and computes the minimum required time to finish a race
    using dynamic programming with state transitions according to given parameters.
    Input is read from standard input. Each case has:
        - Number of checkpoints (n)
        - n integers (checkpoints positions)
        - A float b (base time cost for a special operation)
        - Four floats r, v, e, f (transition point and speeds)
    The solution finds the minimal time to finish the marathon possibly using shortcuts at checkpoints.
    Terminates when n==0 is entered.
    """
    from bisect import bisect  # For binary search operations (not used in this implementation)
    from itertools import accumulate  # For fast prefix sum computations
    from sys import stdin  # For efficient input reading

    f_i = stdin  # Alias for stdin to read input

    while True:
        # Read the number of checkpoints (n)
        n = int(f_i.readline())
        if n == 0:
            # Exit condition: n==0 signals the end of input
            break

        # Read list of checkpoint positions (increasing positions along the race)
        a = list(map(int, f_i.readline().split()))
        # Read the base penalty time for using a magic ability (float)
        b = float(f_i.readline())
        # Read race parameters: r (transition position), v (base speed), e (extra fatigue), f (base fatigue)
        r, v, e, f = map(float, f_i.readline().split())
        r = int(r)  # r is actually always used as an integer for index calculations

        # Remove the last checkpoint from the list, which is the marathon's final position
        a_n = a.pop()

        # Precompute the time to cross every meter up to the finish line
        # First portion: speed depends on 'f' (up to position r)
        dp = [1 / (v - f * (r - x)) for x in range(r)]
        # Second portion: speed depends on 'e' (beyond position r)
        dp += [1 / (v - e * (x - r)) for x in range(r, a_n)]

        # Transform dp into prefix sums: dp[i] is the minimum time to reach position i from start
        dp = list(accumulate(dp))
        # cost[i]: extra "magic" cost for reaching position i using the magic ability
        cost = tuple(time + b for time in dp)

        # For each magic checkpoint (excluding finish line) in a
        for a_i in a:
            base = dp[a_i - 1]  # Time to reach checkpoint a_i directly
            # For all points past checkpoint a_i, try using the magic ability here to reach there
            for i, tpl in enumerate(zip(dp[a_i:], cost), start=a_i):
                pre, new = tpl
                new += base  # Total new time if using magic at a_i to get here
                if new < pre:
                    # If taking the shortcut leads to a faster result, update the time
                    dp[i] = new

        # Output the best time to finish the full marathon
        print(dp[-1])