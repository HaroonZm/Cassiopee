def perform_shuffling():
    """
    Reads sequences of card decks and shuffle instructions from standard input,
    performs the specified shuffles, and prints the resulting deck.
    Input format:
        - Each deck (as a string) is read from input.
        - A deck string of '-' indicates the end of input and terminates processing.
        - For each deck, an integer m is read (the number of shuffles).
        - Then m lines follow, each containing an integer h.
          Each h indicates the number of cards from the top to be moved to the bottom.
    Example:
        Input:
            abcdef
            2
            3
            1
            -
        Output:
            defabc
    """

    while True:
        # Read the deck string from input
        deck = raw_input()
        if deck == '-':
            # If input is '-', terminate the processing
            break
        else:
            # Read number of shuffles to perform
            m = int(raw_input())
            # Perform shuffling m times
            for i in range(m):
                # For each shuffle, read the number of cards h to cut from the top
                h = int(raw_input())
                # Shuffle: move first h cards to the end of the deck
                deck = deck[h:] + deck[:h]
            # Output the final deck order after all shuffles
            print deck

# Execute the shuffling process
perform_shuffling()