import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

def main():
    """
    Main function to read input, build the graph representation of the grid,
    compute the shortest path from the top-left to the bottom-right cell,
    and print the minimum number of color changes required.
    """
    # Read grid dimensions from input
    H, W = map(int, input().split())
    
    # Read the grid itself, each element is a string representing a row
    s = []
    for _ in range(H):
        s.append(input())
    
    def co_num(h, w):
        """
        Convert grid coordinates (h, w) into a unique vertex number for graph representation.
        
        Args:
            h (int): Row index of the cell (0-based).
            w (int): Column index of the cell (0-based).
        
        Returns:
            int: Unique number representing the cell at (h, w).
        """
        return h * W + w
    
    # Lists to store the row indices, column indices, and distances for the sparse adjacency matrix
    row = []
    col = []
    dist = []
    
    # Build the adjacency matrix by adding edges between adjacent cells (down and right directions)
    for h in range(H):
        for w in range(W):
            # Add an edge to the cell below (if it exists)
            if h != H - 1:
                row.append(co_num(h, w))
                col.append(co_num(h + 1, w))
                # Edge cost is 0 if the symbols are the same, else 1 (color change)
                dist.append(0 if s[h+1][w] == s[h][w] else 1)
            # Add an edge to the right cell (if it exists)
            if w != W - 1:
                row.append(co_num(h, w))
                col.append(co_num(h, w + 1))
                # Edge cost is 0 if the symbols are the same, else 1 (color change)
                dist.append(0 if s[h][w+1] == s[h][w] else 1)
    
    # Build a sparse adjacency matrix for the graph (directed, from each cell to its right and down neighbors)
    adjacency_matrix = csr_matrix((dist, (row, col)), shape=[H * W, H * W])
    
    # Run Dijkstra's algorithm to find the shortest path from the start (top-left cell) to the end (bottom-right cell)
    # The cost here is the minimal number of color changes along any path from start to goal
    d = int(dijkstra(adjacency_matrix, directed=True, indices=0)[H * W - 1])
    
    # Determine the number of color changes required based on the starting and ending cell type
    # A color change corresponds to moving from '.' to '#' or vice versa
    if s[0][0] == '.' and s[-1][-1] == '.':
        # If both start and goal are '.', the total number of transitions halves the edge cost
        print(d // 2)
    else:
        # If either or both ends are '#', an additional transition is counted
        print(d // 2 + 1)

if __name__ == "__main__":
    main()