from sys import stdin

WIN_PATTERNS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
)

def check(board):
    for koma in 'ox':
        if any(all(board[i] == koma for i in pattern) for pattern in WIN_PATTERNS):
            return koma
    return 'd'

print('\n'.join(check(line.strip()) for line in stdin if line.strip()))