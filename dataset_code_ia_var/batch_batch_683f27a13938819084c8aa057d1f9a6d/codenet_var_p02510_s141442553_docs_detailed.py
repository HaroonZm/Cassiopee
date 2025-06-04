def perform_shuffles():
    """
    Interactively reads card sequence and performs a number of shuffles for each input.
    
    The function repeatedly accepts:
      - A string representing the initial order of cards.
        Input ends if the string is a single hyphen ('-').
      - An integer specifying the number of shuffles to perform.
      - For each shuffle, an integer 'h' representing the cut position:
        The top 'h' cards are moved to the end of the sequence.
    After performing all specified shuffles, the function prints the final card order.
    """
    while True:
        # Read the initial sequence of cards; remove leading/trailing whitespace
        card = input().strip()
        
        # If the input is a single hyphen, terminate the loop
        if card == '-':
            break
        
        # Read the number of shuffles to perform as an integer
        no_shuffles = int(input())
        
        # Perform 'no_shuffles' shuffles as specified
        for _ in range(no_shuffles):
            # Read shuffle value 'h'; this is the cut size
            h = int(input())
            
            # Move the top 'h' cards to the bottom of the deck by slicing
            card = card[h:] + card[:h]
        
        # Output the final card sequence after all shuffles
        print(card)

# Uncomment the following line to execute the function directly.
# perform_shuffles()