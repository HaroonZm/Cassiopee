# Define the reference order of suits as a string.
# "S" stands for Spades, "C" for Clubs, "H" for Hearts, and "D" for Diamonds.
# The order in the string will be used to map suit characters to numerical indices.
ref = "SCHD"

# 'first' is a flag used to determine if it is the first round of printing.
# It starts as 0 (False) and is set to 1 (True) after the first input.
first = 0

# Start an infinite loop that will continue to process input until interrupted or ended by exception.
while 1:
    try:
        # Try to read an integer input from the user using input().
        # This input 'n' is the number of hands to process in this round.
        n = input()
        # If it is not the first time, 'first' will be 1 (True),
        # and it prints a blank line between test cases.
        if first:
            print
        # Set 'first' to 1 (True) to indicate subsequent test cases.
        first = 1
    except:
        # If there is any exception (e.g., EOF), exit the loop.
        break

    # Create a list 'P' of length 4, where each element is a list.
    # For 4 iterations (for each suit), do the following:
    #   - Use 'raw_input()' to read a line from input (assumed to contain 13 whitespace separated numbers).
    #   - Use 'split()' to split it into a list of strings.
    #   - Use 'map(int, ...)' to convert each to an integer, so we have a list of 13 integers.
    # 'P' becomes a list of 4 lists, each containing 13 integers corresponding to the values for the 13 ranks of a suit.
    P = [map(int, raw_input().split()) for i in range(4)]

    # Read another line of input for multipliers (bonuses).
    # Use 'raw_input()', split into a list of strings, and convert all elements to integers.
    # 'H' becomes a list containing multipliers for hand types.
    H = map(int, raw_input().split())

    # Loop 'n' times, each iteration processing a hand of cards.
    for _ in range(n):
        # Read a line from input representing the 5 cards in the hand, as strings.
        # Each card is a 2-character or 3-character string, like "AH" (Ace of Hearts) or "10S" (Ten of Spades).
        # Card ranks: A,Ace; 2-9; T,10; J,Jack; Q,Queen; K,King.
        hand = raw_input()                     # Read the line from standard input.
        hand = hand.replace("A","1")           # Replace 'A' with '1' to denote Ace numerically as 1.
        hand = hand.replace("T","10")          # Replace 'T' with "10" to denote Ten as 10.
        hand = hand.replace("J","11")          # Replace 'J' with "11" to denote Jack as 11.
        hand = hand.replace("Q","12")          # Replace 'Q' with "12" to denote Queen as 12.
        hand = hand.replace("K","13")          # Replace 'K' with "13" to denote King as 13.
        hand = hand.split()                    # Split the string into individual card strings.

        # 'num' will store the numerical rank (1-13) of each card.
        # It takes the string of each card, removes the last character (the suit),
        # and converts the rest to an integer.
        num = [int(i[:-1]) for i in hand]

        # 'suit' stores the numerical index (0-3) of each card's suit.
        # It takes the last character of each card string, and finds its index in 'ref' string.
        # "S"->0, "C"->1, "H"->2, "D"->3
        suit = [ref.index(i[-1]) for i in hand]

        # Calculate the base score 'ans':
        # For each of the 5 cards in the hand,
        # use the suit and rank to look up the corresponding value in 'P' and sum all 5.
        # For example, for the ith card, 'P[suit[i]][num[i]-1]' gives the card's value.
        ans = sum(P[suit[i]][num[i]-1] for i in range(5))

        # Determine what kind of poker hand this is.
        # If all suits are the same, this is a possible Flush or Straight Flush:

        if len(set(suit)) == 1:
            # If the hand is a Royal Flush (A,10,J,Q,K), regardless of order:
            if sorted(num) == [1,10,11,12,13]:
                # Apply the Royal Flush multiplier (index 8 in 'H', 0-based).
                ans *= H[8]
            # If the hand is a straight flush (5 consecutive cards, same suit):
            elif sorted([i - min(num) for i in num]) == [0,1,2,3,4]:
                # Apply the Straight Flush multiplier (index 7).
                ans *= H[7]
            # Otherwise, it's just a flush:
            else:
                # Apply the Flush multiplier (index 4).
                ans *= H[4]
        # If it's a straight (5 consecutive numerical ranks), but not all same suit:
        elif sorted([i - min(num) for i in num]) == [0,1,2,3,4] or sorted(num) == [1,10,11,12,13]:
            # Apply the Straight multiplier (index 3).
            ans *= H[3]
        # Check for Four of a Kind (4 cards have the same rank):
        elif max(num.count(i) for i in set(num)) == 4:
            # Apply the Four of a Kind multiplier (index 6).
            ans *= H[6]
        # Check for Three of a Kind or Full House:
        elif max(num.count(i) for i in set(num)) == 3:
            # If there are only two unique numbers, it is a Full House (3 same + 2 same):
            if len(set(num)) == 2:
                # Apply the Full House multiplier (index 5).
                ans *= H[5]
            else:
                # Otherwise, it's Three of a Kind (index 2).
                ans *= H[2]
        # Check for Pairs:
        elif max(num.count(i) for i in set(num)) == 2:
            # If there are 3 unique numbers, it's two pairs:
            if len(set(num)) == 3:
                # Apply the Two Pair multiplier (index 1).
                ans *= H[1]
            # If there are 4 unique numbers, it's one pair:
            else:
                # Apply the One Pair multiplier (index 0).
                ans *= H[0]
        # If none of the above, score is 0.
        else:
            ans = 0
        # Output the computed score 'ans' for this poker hand.
        print ans