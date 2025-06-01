def process_hands():
    """
    Process sets of hands input by the user in a continuous loop until a zero input is encountered.
    
    For each set of 5 hands (integers), the function evaluates based on unique values:
    - If the set contains anything other than exactly two unique numbers,
      it prints the number 3 five times.
    - If there are exactly two unique numbers, it follows these rules:
        * If the unique numbers are 1 and 2, print 1 for each '1' in the hands and 2 for each '2'.
        * If the unique numbers are 1 and 3, print 2 for each '1' and 1 for each '3'.
        * Otherwise (unique numbers likely 2 and 3), print 1 for each '2' and 2 for each other.
    
    The function continues indefinitely until the first input of a set is zero.
    """
    while True:
        hands = []
        
        # Read first input for the hand set
        h = int(input())
        # End processing if input is zero
        if h == 0:
            break
        
        # Add the first hand to the list
        hands.append(h)

        # Read the remaining 4 inputs for the current hand set
        for _ in range(4):
            h = int(input())
            hands.append(h)

        # Extract the unique values from the current hand set
        h_uni = list(set(hands))

        # If the number of unique values is not equal to 2, print 3 five times and continue
        if len(h_uni) != 2:
            for _ in range(5):
                print(3)
            continue

        # Sort the unique values to make comparisons easier
        h_uni.sort()

        # If the unique values are [1, 2], print 1 for '1' and 2 for '2'
        if h_uni[0] == 1 and h_uni[1] == 2:
            for h in hands:
                if h == 1:
                    print(1)
                else:
                    print(2)
        # If the unique values are [1, 3], print 2 for '1' and 1 for '3'
        elif h_uni[0] == 1 and h_uni[1] == 3:
            for h in hands:
                if h == 1:
                    print(2)
                else:
                    print(1)
        # If the unique values are neither of the above, assume they are [2, 3]
        # Print 1 for '2' and 2 for '3' (or the other value)
        else:
            for h in hands:
                if h == 2:
                    print(1)
                else:
                    print(2)

process_hands()