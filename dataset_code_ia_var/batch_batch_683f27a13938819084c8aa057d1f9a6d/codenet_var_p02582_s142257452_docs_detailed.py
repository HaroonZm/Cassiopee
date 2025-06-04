def max_consecutive_R():
    """
    Reads a string from user input and calculates the maximum number of consecutive 'R' characters.
    Returns:
        None. Prints the result:
            3 if there are three consecutive 'R's,
            2 if there are exactly two consecutive 'R's,
            1 if there is at least one single 'R' but not two or three in a row,
            0 if there is no 'R' at all.
    """
    # Read string input from user
    s = input()

    # Count the occurrences of 'RRR' to check for three consecutive 'R's
    r = s.count("RRR")

    # Count the occurrences of 'RR' to check for two consecutive 'R's
    n = s.count("RR")

    # Check for three consecutive 'R's
    if r == 1:
        print(3)
    # Check for two consecutive 'R's only (and not three in a row)
    elif n == 1:
        print(2)
    else:
        # Check if there is at least one 'R' somewhere in the string
        if s.count("R") > 0:
            print(1)
        # No 'R' at all
        else:
            print(0)

# Call the main function to execute the logic
max_consecutive_R()