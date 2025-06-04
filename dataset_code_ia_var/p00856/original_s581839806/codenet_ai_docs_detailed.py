def solve(N, T, L, B):
    """
    Simulates a board game where a piece is moved by dice rolls, with the addition of special routes:
    - Normal positions, ladder positions (move again next turn), and backward positions (return to start).
    Calculates the probability of reaching the goal within a given turn limit.

    Parameters:
    N (int): The goal position on the board (positions indexed from 0 to N).
    T (int): The number of turns (time limit).
    L (int): Number of ladder positions on the route (positions where you move in the next turn).
    B (int): Number of backward positions (positions where landing sends you back to the start).

    Reads:
    For each ladder, an input line containing its position.
    For each backward, an input line containing its position.
    """
    # route[x] = -1 : normal place, 0 : ladder, 1 : backward
    route = [-1] * (N + 1)  # Initialize all positions as normal

    # Read and mark ladder positions from input
    for _ in range(L):
        x = int(input())  # ladder position
        route[x] = 0      # mark as ladder

    # Read and mark backward positions from input
    for _ in range(B):
        y = int(input())  # backward position
        route[y] = 1      # mark as backward

    ans = 0  # Accumulate the probability of reaching the goal

    # before[i]: probability to be at position i in the current round
    before = [0] * (N + 1)
    before[0] = 1  # Start the game at position 0 with probability 1

    # beforebefore[i]: probability to be at position i in the NEXT round (for ladder jump)
    beforebefore = [0] * (N + 1)

    # Loop for each turn
    for _ in range(T):
        now = [0] * (N + 1)      # Probability to reach each position in this turn
        future = [0] * (N + 1)   # Probability for positions to be used in two steps (ladders)

        # For each current position on the board
        for i in range(N):
            # Simulate each possible dice roll (1 to 6)
            for j in range(1, 7):
                X = i + j
                # If the piece moves off the board, it bounces back
                if X >= N + 1:
                    X = N - (X - N)
                # Handle each position type
                if route[X] == -1:   # Normal cell
                    now[X] += before[i] / 6
                elif route[X] == 0:  # Ladder: wait one more turn before resuming
                    future[X] += before[i] / 6
                else:                # Backward: sent to start
                    now[0] += before[i] / 6

        ans += now[-1]  # Accumulate the probability of reaching the goal (Nth position)

        # Prepare for the next turn:
        # before = probability distribution for the next turn
        before = [0] * (N + 1)
        for i in range(N + 1):
            # Add: now[i] (positions just landed this round)
            # Add: beforebefore[i] (positions that waited one turn due to a ladder)
            before[i] = now[i] + beforebefore[i]

        # Ladder candidates for the turn after next
        beforebefore = future

    # Output the total probability (to six decimal places) of ending on the goal within T turns
    print("{:9f}".format(ans))


def main():
    """
    Reads input in the expected format and repeatedly solves the problem for each dataset.
    Terminates when 'N' (the board size) is 0.
    Expected input lines:
      N T L B
      [L lines with positions for ladders]
      [B lines with positions for backward cells]
    """
    while True:
        N, T, L, B = map(int, input().split())
        if N == 0:
            return   # Terminate on N == 0
        solve(N, T, L, B)


if __name__ == '__main__':
    main()