def main():
    """
    Main function to compute the probability of reaching the last cell
    of a board game after a given number of turns, considering special
    cells (lose a turn or go back to start), given by the user.
    Input is taken interactively, stop by entering `0` for N.
    """
    while True:
        # Read in the values for number of cells, number of turns, lose positions, and back to start positions.
        N, T, L, B = map(int, raw_input().split())
        if N == 0:
            break  # End input on N == 0

        # Read in the positions where a player should lose their next turn.
        lose = [int(raw_input()) for _ in xrange(L)]
        # Read in the positions where a player should go back to the start.
        back = [int(raw_input()) for _ in xrange(B)]

        # Initialize dynamic programming table:
        # dp[t][i] is the probability of being on cell i after t turns.
        dp = [[0.0] * (N + 1) for _ in xrange(T + 2)]
        dp[0][0] = 1.0  # Start at cell 0 with 100% probability

        # p is the probability of rolling any specific dice number (1 to 6).
        p = 1.0 / 6.0

        # Iterate over all possible turns
        for t in xrange(T):
            # Iterate over all cells except the finish cell (N)
            for i in xrange(N):
                # If this cell is a "lose turn" cell, reduce effective turn (player can't play this turn)
                effective_turn = t - 1 if i in lose else t

                # Try all dice rolls from this position
                for dice in xrange(1, 7):
                    next_pos = i + dice
                    # If moving past the last cell, "bounce back" from the last cell
                    if next_pos > N:
                        next_pos = N - (next_pos % N)
                    # If landing on a "back to start" cell, move to start (cell 0)
                    if next_pos in back:
                        dp[t + 1][0] += p * dp[effective_turn][i]
                    else:
                        dp[t + 1][next_pos] += p * dp[effective_turn][i]
            # Aggregate the probability of already being on cell N (finish), since it's a sink.
            dp[t + 1][N] += dp[t][N]

        # Print the probability of being at the last cell after T turns, with 6 digits after decimal
        print "%.6f" % dp[T][N]

if __name__ == "__main__":
    main()