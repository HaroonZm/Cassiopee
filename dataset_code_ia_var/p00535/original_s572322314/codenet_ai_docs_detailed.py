from heapq import heappush, heappop

def read_input():
    """
    Read the board's height and width, then the board's content from standard input.

    Returns:
        h (int): Board height.
        w (int): Board width.
        raw_board (list of str): Each string represents a row of the board.
    """
    h, w = map(int, input().split())
    raw_board = [input() for _ in range(h)]
    return h, w, raw_board

def initialize_board(h, w, raw_board):
    """
    Initialize and pad the board. Convert cell values for further processing.

    Args:
        h (int): Board height.
        w (int): Board width.
        raw_board (list of str): Board rows as strings.

    Returns:
        mp (list of list): 2D list representing the padded board. Numbers and zeros are int.
        que (list of tuple): Priority queue with cells initialized at zero.
    """
    # Initialize the board with padding (-1)
    mp = [[-1] + list(row) + [-1] for row in raw_board]
    mp.insert(0, [-1] * (w + 2))    # Top padding row
    mp.append([-1] * (w + 2))       # Bottom padding row

    que = []  # Priority queue for zero-cells (cells to process)

    for y in range(1, h + 1):           # 1-based due to padding
        for x in range(1, w + 1):       # 1-based due to padding
            cell = mp[y][x]
            if "1" <= cell <= "9":
                mp[y][x] = int(cell)    # Convert string digits to int
            elif cell == ".":
                mp[y][x] = 0            # Free cell as zero
                heappush(que, (0, x, y))# Initialize queue with zero cells

    return mp, que

def solve_minesweeper_like(mp, que):
    """
    Simulate the auto-reveal process on the board using BFS, updating the board in-place.

    Args:
        mp (list of list): 2D padded board (int values, -1 for border)
        que (list of tuple): Priority queue with cells to process (turn, x, y)

    Returns:
        turn (int): The last step (turn) at which a new cell became zero.
    """
    # All 8 directions around a cell
    vec = (
        (0, 1),   # right
        (0, -1),  # left
        (1, 1),   # down-right
        (1, 0),   # down
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, 0),  # up
        (-1, -1)  # up-left
    )

    turn = 0  # Most recent turn (step) at which a cell was processed

    # Process the queue using a min-heap (priority queue) for BFS with turn-order
    while que:
        turn, x, y = heappop(que)
        for dx, dy in vec:
            nx, ny = x + dx, y + dy
            if mp[ny][nx] > 0:
                mp[ny][nx] -= 1     # Reveal: decrement counts for adjacent numbers
                if mp[ny][nx] == 0: # If becomes zero, schedule for revealing
                    heappush(que, (turn + 1, nx, ny))

    return turn

def main():
    """
    Main execution flow: Reads input, initializes the board, processes cell reveals,
    and prints the minimum number of steps needed.
    """
    h, w, raw_board = read_input()
    mp, que = initialize_board(h, w, raw_board)
    result = solve_minesweeper_like(mp, que)
    print(result)

if __name__ == "__main__":
    main()