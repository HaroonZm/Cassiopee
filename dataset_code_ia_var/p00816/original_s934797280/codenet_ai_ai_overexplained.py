def shred(num, bit):
    # Convert the input number (which may be an integer or string) into a string,
    # then create a list of its individual digit characters for manipulation
    num = list(str(num))
    # Initialize the index variable 'i' to 0; this will keep track of our current position in the digit list
    i = 0
    # The loop continues as long as 'bit' is nonzero; 'bit' will be used as a bitmask to control which digits to join
    while bit:
        # Check if least significant bit of 'bit' is set (i.e., bit % 2 == 1, which is same as bit & 1)
        if bit & 1:
            # If the condition is true, we combine (concatenate) the digit at position 'i'
            # with the next digit at position 'i+1'
            num[i] += num.pop(i+1)
            # After this operation, num[i+1] is removed, and its character is appended to num[i]
        else:
            # If the LSB is not set, move to the next digit
            i += 1
        # Right-shift 'bit' by one to analyze the next bit, for the next digit separation
        bit >>= 1
    # Once all bits have been processed, return the list 'num', possibly containing joined numbers as strings
    return num

def testcase_ends():
    # Read input, splitting into two separate values, 't' and 'num'
    # (In Python 2, input must be fetched with raw_input(), not input())
    t, num = map(int, raw_input().split())
    # If both 't' and 'num' are zero, this signals the terminating condition of input
    if t == 0 and num == 0:
        return 1  # Returning 1 signals main loop to break/end

    # Initialize an empty list to store possible candidate segmentations that lead to the maximal sum within constraint
    cutcand = []
    # Variable to keep track of the current highest sum found, initialized to -1 so any real sum will be higher
    curmax = -1
    # Examine every possible pattern of splitting the input number into contiguous segments
    # 'len(str(num)) - 1' is the number of places between digits where a split may or may not occur
    for i in range(1 << (len(str(num)) - 1)):
        # Use bit pattern 'i' to control which digits to join/split
        cut = shred(num, i)
        # Convert each segment back to integer and sum
        sumcut = sum(map(int, cut))

        # Ignore any segmentation whose total sum exceeds the target 't'
        if sumcut > t:
            continue
        # If the sum matches the current maximum, append this candidate
        elif sumcut == curmax:
            cutcand.append(cut)
        # If the sum exceeds all seen so far, discard old ones and store just this one
        elif sumcut > curmax:
            cutcand = [cut]
            curmax = sumcut

    # After examining all possibilities, decide on the output based on the results collected
    if len(cutcand) > 1:
        # If multiple segmentations are best, but yields ambiguity, print 'rejected'
        print 'rejected'
    elif len(cutcand) == 1:
        # If exactly one optimal segmentation exists, print the maximum sum and the joined segments separated by spaces
        print curmax, ' '.join(cutcand[0])
    else:
        # If there is no valid segmentation (sum never <= t), print 'error'
        print 'error'

    # Return 0 to signal to the main loop to continue
    return 0

def main():
    # Infinite loop to repeatedly process test cases until terminated
    while True:
        # Call testcase_ends(); if it returns true (1), we stop processing
        if testcase_ends():
            return 0  # exit the program

# Standard Python boilerplate to only run 'main()' if this script is run, not imported as a module
if __name__ == '__main__':
    main()