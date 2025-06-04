from collections import deque
import sys
sys.setrecursionlimit(10**7)

# Directions for adjacency (up, down, left, right)
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(h, w, y, x):
    # Check if position (y,x) is in the grid bounds
    return 0 <= y < h and 0 <= x < w

def get_union(board, h, w, visited, start_y, start_x):
    """
    BFS to get all panels united with the panel at (start_y, start_x)
    They share the same color.
    Return the list of positions (y,x) in this united panel
    """
    color = board[start_y][start_x]
    queue = deque()
    queue.append((start_y, start_x))
    visited[start_y][start_x] = True
    united = [(start_y, start_x)]
    while queue:
        y, x = queue.popleft()
        for dy, dx in DIRS:
            ny, nx = y + dy, x + dx
            if in_bounds(h, w, ny, nx) and not visited[ny][nx]:
                if board[ny][nx] == color:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    united.append((ny, nx))
    return united

def get_united_panels(board, h, w):
    """
    Identify all united panels on the board.
    Return:
        unions: a list of lists of positions
    """
    visited = [[False]*w for _ in range(h)]
    unions = []
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                united = get_union(board, h, w, visited, i, j)
                unions.append(united)
    return unions

def apply_color_change(board, h, w, current_union, new_color):
    """
    Change the color of the united panel at the top-left corner to new_color,
    then fuse with adjacent panels of the same color.

    Parameters:
        board: current color grid (list of lists)
        current_union: list of (y,x) tuples of current united panel
        new_color: target color to change the united panel to

    Returns:
        new_board: new board grid after color change and fusion
        new_union: list of (y,x) tuples of the new united panel at (0,0)
    """
    # Create a deep copy of board to not modify original
    new_board = [row[:] for row in board]

    # Change the color of all panels in current united panel to new_color
    for y, x in current_union:
        new_board[y][x] = new_color

    # Now fuse adjacent panels of same color into a larger united panel
    # BFS from (0,0) to get the new united panel (panels connected matching new_color)
    visited = [[False]*w for _ in range(h)]
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    united = [(0,0)]
    color = new_board[0][0]
    while queue:
        y, x = queue.popleft()
        for dy, dx in DIRS:
            ny, nx = y+dy, x+dx
            if in_bounds(h, w, ny, nx) and not visited[ny][nx]:
                if new_board[ny][nx] == color:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    united.append((ny, nx))

    return new_board, united

def solve_single_case(h, w, target_color, board):
    """
    Solve one case:
    We have 5 color changes max.
    At each step, we can choose a target color different from current united panel color,
    and the united panel at (0,0) will change to that color and fuse with adjacent panels.

    Goal: after 5 color changes, get the largest united panel of target_color at (0,0).

    Approach:
    - BFS or DFS of states with pruning
    - State represented by:
      - board state
      - current united panel positions (to avoid recomputing frequently)
      - number of remaining moves (color changes left)
    - We only change color of the united panel at (0,0).
    - If current color at (0,0) == target_color at the end, record size.
    - Return maximum size.

    Since h,w <=8 and 5 steps, we can do BFS with memoization.

    We'll memoize visited states by:
     - tuple of board rows flattened
     - number of remaining moves

    """

    from copy import deepcopy

    # Initial united panel at (0,0)
    visited_init = [[False]*w for _ in range(h)]
    initial_union = get_union(board, h, w, visited_init, 0, 0)
    # initial color of the united panel
    initial_color = board[0][0]

    max_size = 0
    # visited dictionary: keys are (tuple of board rows as tuples, moves_left)
    visited_states = {}

    # BFS queue elements: (current_board, current_union, moves_left)
    queue = deque()
    queue.append((board, initial_union, 5))
    visited_states[(tuple(tuple(row) for row in board), 5)] = len(initial_union)

    # If initial panel is already the target color, consider it:
    if initial_color == target_color:
        max_size = max(max_size, len(initial_union))

    while queue:
        current_board, current_union, moves_left = queue.popleft()
        if moves_left == 0:
            # no more moves, check if united panel color is target_color
            if current_board[0][0] == target_color:
                max_size = max(max_size, len(current_union))
            continue

        current_color = current_board[0][0]

        # Try all six colors except current_color
        for color_change_to in range(1,7):
            if color_change_to == current_color:
                continue

            # Apply the color change & fusion
            new_board, new_union = apply_color_change(current_board, h, w, current_union, color_change_to)

            # Check if visited
            board_tuple = tuple(tuple(row) for row in new_board)
            state_key = (board_tuple, moves_left - 1)
            union_size = len(new_union)

            # If this state is not visited or found bigger union for same board/moves_left
            # we visit it
            if state_key not in visited_states or union_size > visited_states[state_key]:
                visited_states[state_key] = union_size
                queue.append((new_board, new_union, moves_left - 1))

            # Also update max if color matches target color
            if new_board[0][0] == target_color:
                if union_size > max_size:
                    max_size = union_size

    return max_size

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        idx += 1
        if line == '':
            continue
        h, w, c = map(int, line.split())
        if h == 0 and w == 0 and c == 0:
            break
        board = []
        for _ in range(h):
            row = list(map(int, input_lines[idx].split()))
            idx += 1
            board.append(row)
        # Solve for this case
        ans = solve_single_case(h, w, c, board)
        print(ans)

if __name__ == '__main__':
    main()