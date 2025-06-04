import sys
import math
import os

# Set up input for debugging if the PYDEV environment variable is set
PYDEV = os.environ.get('PYDEV')
if PYDEV == "True":
    # Redirect standard input to read from 'sample-input.txt' for debugging
    sys.stdin = open("sample-input.txt", "rt")

def card_game(c1, c2, c3):
    """
    Determines if, after drawing three unique cards c1, c2, c3 from a deck of cards numbered 1 to 10,
    there are more than three cards remaining in the deck that, when added to c1+c2, result in a sum
    less than or equal to 20.

    Args:
        c1 (int): The value of the first drawn card (from 1 to 10).
        c2 (int): The value of the second drawn card (from 1 to 10).
        c3 (int): The value of the third drawn card (from 1 to 10).

    Returns:
        bool: True if there are more than three such cards remaining; False otherwise.
    """
    # Create a list representing the deck with cards numbered from 1 to 10
    cards = list(range(1, 11))
    
    # Remove the drawn cards from the deck
    for card in [c1, c2, c3]:
        cards.remove(card)
    
    # Calculate the sum of the first two drawn cards
    S = c1 + c2
    cnt = 0  # Counter for the number of valid cards remaining

    # Count the number of remaining cards that do not exceed the sum limit when added to S
    for card in cards:
        if S + card <= 20:
            cnt += 1

    # Return True if more than three such cards exist, otherwise False
    return cnt > 3

# Read and process each line from the input
for line in sys.stdin:
    # Parse the integers c1, c2, c3 from the line
    c1, c2, c3 = [int(_) for _ in line.split()]
    # Output "YES" if the card_game function returns True, otherwise "NO"
    print("YES" if card_game(c1, c2, c3) else "NO")