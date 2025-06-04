def compute_max_score():
    """
    Calculates the maximum score achievable in a hand game ("Rock, Paper, Scissors") with constraints.
    The game is played over n rounds with three scoring possibilities (for each winning move).
    Each move cannot be repeated in the same group separated by k rounds.

    The function reads input values for number of rounds, group size, scores for each move, and the opponent's moves.
    It outputs the total score, applying the game constraints.

    Input format (from stdin):
        n k         - Number of rounds and group size (separated by space)
        R S P       - Scores for winning with Rock, Scissors, Paper (separated by space)
        t           - String of opponent moves, each character: 'r', 's', or 'p'

    Output:
        Prints the maximum possible score (as per the rules and constraints).

    Example input:
        5 2
        1 2 3
        rsrps

    Example output:
        10
    """
    # Read and unpack basic input values:
    n, k = map(int, input().split())      # n = total rounds, k = repeat constraint
    R, S, P = map(int, input().split())   # R = points for Rock, S = for Scissors, P = for Paper
    t = input()                           # Opponent's moves as a string (n letters)

    ans = 0       # To accumulate the final score
    win = []      # To track our own move for each round (for possible repeat checking)

    # First pass: Choose the best move against each of the opponent's moves and add score
    for tt in t:
        if tt == 'r':
            # Opponent throws Rock, we win with Paper
            win.append('p')
            ans += P
        elif tt == 's':
            # Opponent throws Scissors, we win with Rock
            win.append('r')
            ans += R
        else:
            # Opponent throws Paper, we win with Scissors
            win.append('s')
            ans += S

    # Second pass: Adjust for not being allowed to make the same move within each k-group consecutively
    for i in range(k):
        # Extract every k-th move starting from index i: this forms a "group"
        l = win[i::k]
        # For each group, check for consecutive identical wins and nullify (subtract) one occurrence as required
        for j in range(1, len(l)):
            if l[j] == l[j-1]:
                if l[j] == 'p':
                    ans -= P
                elif l[j] == 'r':
                    ans -= R
                else:  # l[j] == 's'
                    ans -= S
                l[j] = 'z'  # Mark this move as "used/invalid", so it doesn't cause further subtractions

    print(ans)