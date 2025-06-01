H, W = map(int, input().split())
board = [input() for _ in range(H)]

# Precompute prefix sums of I (Ingots) in each column
prefix_I = [[0]*(H+1) for _ in range(W)]
for j in range(W):
    for i in range(H):
        prefix_I[j][i+1] = prefix_I[j][i] + (1 if board[i][j] == 'I' else 0)

result = 0
# For each pair of rows i < k
for i in range(H-1):
    for k in range(i+1, H):
        # We'll count columns where conditions hold:
        # at row i, column j: 'J'
        # at row i, column l: 'O'
        # and between rows i+1 and k-1, in column j, check 'I's at row k, column j for condition
        # but from the problem condition:
        # Given the quadruple (i,j,k,l), with i<k, j<l:
        # (i,j) = 'J'
        # (i,l) = 'O'
        # (k,j) = 'I'
        # We want to count number of quadruples (i,j,k,l) with these conditions
        # For fixed i and k, find pairs (j,l) with j < l,
        # board[i][j] == 'J', board[i][l] == 'O', and board[k][j] == 'I'.
        # Wait, given the constraints:
        # Actually, the problem states:
        # At (i,j): 'J'
        # At (i,l): 'O'
        # At (k,j): 'I'
        # with i<k and j<l
        # So, for fixed i and k, for columns:
        # Need to count #(j,l) with j<l, board[i][j]=='J', board[i][l]=='O', and board[k][j]=='I'

        # So for fixed i and k, we can:
        # Create arrays J_cols: indices j where board[i][j]=='J' and board[k][j]=='I'
        # Arrays O_cols: indices l where board[i][l]=='O'
        # Then for each pair (j,l) with j<l and j in J_cols, l in O_cols, count 1.

        # To speed this up, we use prefix sums over number of O columns to the right

        J_positions = []
        O_positions = []
        for col in range(W):
            if board[i][col] == 'J' and board[k][col] == 'I':
                J_positions.append(col)
            if board[i][col] == 'O':
                O_positions.append(col)

        # We'll use two pointers to count pairs (j,l) with j in J_positions, l in O_positions, and j < l
        # Sort is not needed because they are already in ascending order by column index
        count_O = 0
        idx_o = 0
        len_o = len(O_positions)
        for j_pos in J_positions:
            # Move idx_o so that O_positions[idx_o] > j_pos
            while idx_o < len_o and O_positions[idx_o] <= j_pos:
                idx_o += 1
            count_O += len_o - idx_o
        result += count_O

print(result)