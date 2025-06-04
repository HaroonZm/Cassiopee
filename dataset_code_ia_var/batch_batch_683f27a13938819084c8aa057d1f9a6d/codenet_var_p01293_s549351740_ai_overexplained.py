# Define the string 'ref' which contains the characters representing card ranks in increasing order of strength,
# from '2' (weakest) through 'A' (Ace, strongest). This string is used later to compare the numeric value of cards.
ref = "23456789TJQKA"

# Define the function 'judge' which determines which player has the winning card in a trick.
# 'hand' is a list of 4 cards (one per player for the trick), 'leader' is the integer index of the player who led (played first).
def judge(hand, leader):
    # Determine the suit that was led by checking the suit of the leading player's card.
    # Each card is a string like 'QC', with hand[leader][1] giving the suit (e.g., 'C', 'D', 'H', 'S').
    led = hand[leader][1]
    
    # Initialize variables:
    # 'mx' will remember the maximum rank (numerical index) of cards of the led suit seen so far.
    mx = -1
    # 'tx' will remember the maximum rank of cards of the trump suit seen so far.
    tx = -1
    # 'winner' is the variable that keeps track of which player's card is currently the winner in this trick.
    winner = -1
    
    # Iterate over all 4 players (they are always indexed 0 to 3).
    for i in xrange(4):
        # 'num' is the numeric rank of the card: use ref.index() to find strength.
        # 'suit' is the suit of the card.
        num, suit = ref.index(hand[i][0]), hand[i][1]
        
        # First, check if the current card is of the trump suit. If so:
        if suit == trump:
            # Compare its rank ('num') to the current best trump card ('tx').
            if num > tx:
                # If this trump card is stronger, update 'tx' and mark this player as the current winner.
                tx = num
                winner = i
        # If no trump card has been seen yet (tx == -1), check if this card can win in the led suit.
        elif tx == -1:
            # Card must match the led suit and beat current max card in that suit.
            if suit == led and num > mx:
                mx = num
                winner = i
    # After all cards have been considered, return the player index of the winner.
    return winner

# Begin an infinite loop to process games until the sentinel '#' is entered.
while 1:
    # Read the trump suit as a string from user input. This specifies the suit that will act as trump.
    trump = raw_input()
    # If the trump suit is '#', break (exit) the loop, ending the program.
    if trump == "#":
        break
    # 'hands' will receive the input for the 4 players. Each input line contains 13 cards
    # (one line per player for North, East, South, West in order).
    hands = [raw_input().split() for i in xrange(4)]
    # Now, 'hands' is a list of lists: each sublist contains the 13 cards for that player.

    # Now, we want to organize the cards by trick (i.e., the four cards that are played at the same time).
    # zip(hands[0], hands[1], hands[2], hands[3]) creates a list of 13 four-card 'hand's (tricks),
    # with one card from each player in playing order.
    hands = zip(hands[0], hands[1], hands[2], hands[3])
    
    # Initialize variables:
    # 'leader' stores the index of the player who led the last trick (starts at 0, meaning North).
    leader = 0
    # 'ns' counts the number of tricks won by North-South (players 0 and 2).
    ns = 0
    # 'ew' counts the number of tricks won by East-West (players 1 and 3).
    ew = 0
    
    # For each trick (group of 4 cards):
    for hand in hands:
        # Determine which player wins this trick, passing the 'hand' and current 'leader'.
        leader = judge(hand, leader)
        # Based on index of winner, increment 'ns' if the winner is North (0) or South (2),
        # 'ew' if the winner is East (1) or West (3).
        if leader in [0, 2]:
            ns += 1
        else:
            ew += 1
    # After all 13 tricks, compare 'ns' and 'ew' to determine the winner.
    # Only scores of 7 or more tricks are counted as "contracts" (typically in bridge);
    # subtract 6 to get the result ("overtricks").
    if ns > ew:
        print "NS", ns - 6
    else:
        print "EW", ew - 6