def read_input():
    """
    Reads and parses the input from standard input.

    Returns:
        N (int): Number of chess pieces (masu).
        L (int): The highest possible position on the board.
        c (list of tuples): Each tuple contains (position, direction) for a chess piece.
    """
    N, L = list(map(int, input().split()))
    c = []
    for _ in range(N):
        p, d = list(map(int, input().split()))
        c.append((p, d))
    return N, L, c

def initialize_positions_and_directions(c):
    """
    Sorts pieces by position and extracts positions and directions.

    Args:
        c (list of tuples): List of (position, direction) pairs.

    Returns:
        masu (list): Sorted list of positions of pieces.
        dir (list): List of directions corresponding to the sorted positions.
    """
    c.sort()  # Sort the pieces based on position for stable processing
    masu = [p for p, d in c]
    dir = [d for p, d in c]
    return masu, dir

def calculate_max_score(N, L, masu, dir):
    """
    Simulates moving the chess pieces and calculates the maximum possible score.

    Rules:
      - Each piece is moved toward one end of the board depending on its direction.
      - The score is incremented/decremented based on the movement and direction.

    Args:
        N (int): Number of chess pieces.
        L (int): Largest board index.
        masu (list): Current positions of the pieces (sorted).
        dir (list): Directions for each piece (0 for left, 1 for right).

    Returns:
        result (int): The maximum score obtainable.
    """
    result = 0  # Stores the maximum score found
    score = 0   # Current score as pieces are moved leftwards

    # First pass: move all pieces to the left side, adjusting score
    # For a piece at position masu[j], it should move to (j+1)
    for j in range(N):
        if dir[j] == 0:
            # Piece moves left: score += spaces traveled (current position - destination)
            score += masu[j] - j - 1
        elif dir[j] == 1:
            # Piece tries to move left against its direction: score is penalized
            score -= masu[j] - j - 1
        # Update piece's new position
        masu[j] = j + 1
    result = score  # Track the best result so far

    # Second pass: for each possible switch, consider shifting rightward-moving pieces to the rightmost possible positions
    for i in range(N - 1, -1, -1):
        if dir[i] == 1:
            # Rightward-moving piece: positive gain for moving to its rightmost
            score += L - (N - i) - masu[i] + 1
        elif dir[i] == 0:
            # Leftward-moving piece: penalize for moving right, against its direction
            score -= L - (N - i) - masu[i] + 1
        # Move this piece to its rightmost destination
        masu[i] = L - (N - i) + 1
        # Update the maximum score so far
        result = max(result, score)
    return result

def main():
    """
    Entry point of the program. Reads input, processes the positions, and prints the max score.
    """
    N, L, c = read_input()
    masu, dir = initialize_positions_and_directions(c)
    result = calculate_max_score(N, L, masu, dir)
    print(result)

if __name__ == "__main__":
    main()