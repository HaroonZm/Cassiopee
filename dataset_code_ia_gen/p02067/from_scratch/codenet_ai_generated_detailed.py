def max_captured_black_stones(L, S):
    # Convert the board state into a list for easier manipulation
    board = list(S)
    
    # Function to find chains on the board
    # Returns a list of tuples (start_index, end_index, color)
    def find_chains(b):
        chains = []
        start = 0
        current_color = b[0]
        for i in range(1, L):
            if b[i] != current_color:
                chains.append((start, i - 1, current_color))
                start = i
                current_color = b[i]
        chains.append((start, L - 1, current_color))
        return chains

    # Function to check if a chain is surrounded by opponent stones
    # chain is a tuple (start, end, color)
    # board b is the current state
    def is_surrounded(chain, b):
        start, end, color = chain
        
        # A chain must be surrounded on both sides
        # by opponent stones to be captured
        opponent = 'B' if color == 'W' else 'W'

        # Check left boundary
        if start == 0:
            return False  # Edge cannot surround

        # Check right boundary
        if end == L - 1:
            return False  # Edge cannot surround

        # Check stones on both sides
        if b[start - 1] == opponent and b[end + 1] == opponent:
            return True
        else:
            return False

    max_captured = 0

    # Iterate over all empty cells to place a white stone
    for pos in range(L):
        if board[pos] != '.':
            continue  # Skip if not empty

        # Place a white stone temporarily
        board[pos] = 'W'

        # After placing, find all chains on the board
        chains = find_chains(board)

        # Check if the white stone forms a white chain that is surrounded
        # We must not allow moves that surround the newly formed white chain
        # Find chains that include the position pos and color white
        invalid_move = False
        for c in chains:
            start, end, color = c
            if color == 'W' and start <= pos <= end:
                # Check if this white chain is surrounded by black stones
                if is_surrounded(c, board):
                    invalid_move = True
                    break
        if invalid_move:
            # Undo the move and skip this position
            board[pos] = '.'
            continue

        # Now find black chains that are surrounded (thus captured)
        captured_stones = 0
        for c in chains:
            start, end, color = c
            if color == 'B' and is_surrounded(c, board):
                captured_stones += (end - start + 1)

        # Update maximum captured if this move is better
        if captured_stones > max_captured:
            max_captured = captured_stones

        # Undo the move for next iteration
        board[pos] = '.'

    return max_captured


# Read input
L_S = input().strip().split()
L = int(L_S[0])
S = L_S[1]

# Compute and print output
print(max_captured_black_stones(L, S))