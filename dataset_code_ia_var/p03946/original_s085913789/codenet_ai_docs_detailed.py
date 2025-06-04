def 解():
    """
    Reads input, processes a sequence of integers, and calculates
    the number of days with the maximum increase between a local minimum
    and a subsequent maximum (i.e., the number of best 'buy-sell' opportunities).

    The main function reads the number of days and the threshold
    (though only the number of days is used in this implementation),
    then reads a price sequence, and finally prints the number
    of times the maximum profit occurs.
    """
    # Read the number of days and the threshold (threshold is unused)
    iN, iT = [int(_) for _ in input().split()]
    # Read the price sequence as a list of integers
    aA = [int(_) for _ in input().split()]
    # Get the length of the price list (for potential future use)
    iL = len(aA)

    # aMaxD stores the maximum profit(s) seen so far, starting with 0
    aMaxD = [0]
    # iMin keeps track of the minimum value observed so far for 'buy'
    iMin = aA[0]
    # iV is the current trend direction (-1 for down, 1 for up, 0 for flat)
    iV = 0

    def checkMax(aMaxD, iMaxD):
        """
        Updates the aMaxD list with the new maximum profit found.

        Args:
            aMaxD (list): Current list of maximum profit(s).
            iMaxD (int): New profit to check.

        Returns:
            list: Updated list of maximum profit(s).
        """
        if aMaxD[0] < iMaxD:
            # Found a new, higher maximum: reset list
            aMaxD = [iMaxD]
        elif aMaxD[0] == iMaxD:
            # Found another instance of current maximum: append to list
            aMaxD.append(iMaxD)
        # If new profit is less than current max, do nothing
        return aMaxD

    # iB is the value on the previous day (initialized to the first day)
    iB = aA[0]
    # Iterate over price sequence starting from the second day
    for iN in aA[1:]:
        # Check for a local peak (downward transition)
        if iB - iN > 0:
            if iV >= 0:
                # When a peak is found, consider max profit from last valley (iMin) to previous peak (iB)
                aMaxD = checkMax(aMaxD, iB - iMin)
            # Set trend as downward
            iV = -1
        # Check for a local valley (upward transition)
        elif iB - iN < 0:
            if iV <= 0:
                # Update minimum value if we move upward from a valley
                iMin = min(iB, iMin)
            # Set trend as upward
            iV = 1
        # Update previous price for next iteration
        iB = iN
    # After loop, check last possible peak at the end of the list
    aMaxD = checkMax(aMaxD, aA[-1] - iMin)
    # Output the number of times the maximum profit was found
    print(len(aMaxD))

解()