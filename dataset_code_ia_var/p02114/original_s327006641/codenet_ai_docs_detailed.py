from collections import deque

def main():
    """
    Main function to count clusters of 'o' cells in a square grid.
    Each cluster is a group of connected 'o' cells (connected orthogonally),
    and the final output is the number of clusters divided by 3.
    """
    # Read the size of the square grid
    n = int(input())
    # Read the grid rows into a list of strings
    A = [input() for _ in range(n)]

    # Counter for the number of connected clusters found
    cnt = 0
    # List of direction vectors: up, left, down, right (orthogonal neighbors)
    dd = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    # 'used' keeps track of already visited cells to prevent reprocessing
    used = {}

    # Traverse each cell in the grid
    for i in range(n):
        for j in range(n):
            # Skip cells that are blocked ('x') or already visited
            if A[i][j] == 'x' or (i, j) in used:
                continue
            # Perform a breadth-first search (BFS) starting from the current cell
            bfs(j, i, n, A, used, dd)
            # Each BFS from an unvisited 'o' cell finds a new cluster
            cnt += 1

    # Output the quotient of cluster count divided by 3
    print(cnt // 3)

def bfs(start_x, start_y, n, grid, used, directions):
    """
    Performs breadth-first search (BFS) to mark all cells in a connected
    cluster of 'o' cells, starting from the given coordinates.

    Args:
        start_x (int): Starting cell x-coordinate (column index).
        start_y (int): Starting cell y-coordinate (row index).
        n (int): Size of the square grid.
        grid (List[str]): The grid itself, list of row strings.
        used (dict): Dictionary to track visited cells as keys (row, col).
        directions (List[List[int]]): List of direction vectors for neighbors.

    Returns:
        None. Modifies 'used' in place.
    """
    # Initialize a queue for BFS with the starting cell (x, y)
    deq = deque([(start_x, start_y)])
    # Mark the starting cell as visited
    used[(start_y, start_x)] = 1

    while deq:
        # Get coordinates of the current cell
        x, y = deq.popleft()
        # Explore all four orthogonal directions
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            # Check that neighbor is within grid bounds
            if 0 <= nx < n and 0 <= ny < n:
                # Check that neighbor is an 'o' cell and unvisited
                if grid[ny][nx] == 'o' and (ny, nx) not in used:
                    # Mark as visited and enqueue for further exploration
                    used[(ny, nx)] = 1
                    deq.append((nx, ny))

if __name__ == "__main__":
    main()