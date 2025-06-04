def solve_8_queens(k, preset_positions):
    N = 8
    board = [['.' for _ in range(N)] for _ in range(N)]
    rows_taken = [False] * N
    cols_taken = [False] * N
    diag1_taken = [False] * (2 * N - 1)  # r - c + (N-1)
    diag2_taken = [False] * (2 * N - 1)  # r + c

    # Place preset queens and mark their attack lines
    for r, c in preset_positions:
        board[r][c] = 'Q'
        rows_taken[r] = True
        cols_taken[c] = True
        diag1_taken[r - c + N - 1] = True
        diag2_taken[r + c] = True

    # We want to place queens in rows 0..7 but some rows may already have queens
    # For the rows without queens, we try to place one queen each
    def backtrack(row):
        if row == N:
            return True
        if rows_taken[row]:
            # Queen already placed, skip to next row
            return backtrack(row + 1)
        for col in range(N):
            if not cols_taken[col] and not diag1_taken[row - col + N -1] and not diag2_taken[row + col]:
                board[row][col] = 'Q'
                rows_taken[row] = True
                cols_taken[col] = True
                diag1_taken[row - col + N - 1] = True
                diag2_taken[row + col] = True
                if backtrack(row + 1):
                    return True
                # Backtrack
                board[row][col] = '.'
                rows_taken[row] = False
                cols_taken[col] = False
                diag1_taken[row - col + N - 1] = False
                diag2_taken[row + col] = False
        return False

    backtrack(0)
    return board

def main():
    k = int(input())
    preset_positions = [tuple(map(int, input().split())) for _ in range(k)]
    solution = solve_8_queens(k, preset_positions)
    for row in solution:
        print(''.join(row))

if __name__ == "__main__":
    main()