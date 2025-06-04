def count_rest_periods():
    """
    This function processes multiple test cases from user input.
    For each test case, it reads three integers: t (number of time units), d (duration of rest period), l (threshold value).
    Then, for t iterations, it reads an integer x.
    If x >= l, a rest period of d is started or reset.
    If not, and there is remaining rest, it is decremented.
    The function counts how many times, except for the last iteration, the system is in a rest period.
    The process repeats until a line "0 0 0" is entered, upon which the function stops.

    Input:
        Multiple test cases; each starts with "t d l" (integers) and then t lines with a single integer each.
        Terminates with "0 0 0".

    Output:
        For each test case, prints the count of time units (except the last one) spent in the rest period.
    """
    while True:
        # Read a single test case consisting of three integers
        t, d, l = map(int, raw_input().split())
        
        # Terminate if all inputs are zero
        if t == 0 and d == 0 and l == 0:
            break

        rest = 0  # Counter for how many steps remain in the current rest period
        ans = 0   # Counter for the number of steps (except last) with active rest period

        for i in xrange(t):
            # Read the current input value
            x = int(raw_input())

            # If the input triggers a new rest period or refreshes the timer
            if x >= l:
                rest = d
            # Else, if in a rest period, decrement the remaining time
            elif rest > 0:
                rest -= 1

            # Count this step if we are in a rest period 
            # and this is not the last step
            if rest > 0 and i < t - 1:
                ans += 1

        # Print the answer for the current test case
        print ans

# Run the function if this file is executed directly
if __name__ == "__main__":
    count_rest_periods()