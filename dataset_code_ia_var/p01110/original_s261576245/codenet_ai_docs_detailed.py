import copy

def main():
    """
    Main function to process a series of fold operations on a 2D matrix.
    For each test case, reads input parameters, folds, and queries, and outputs the results.
    Repeats until a terminator line of 0 0 0 0 is reached.
    """
    while True:
        # Read initial matrix dimensions (n x m), number of folds (t), and number of queries (p)
        n, m, t, p = map(int, input().split())
        # Terminate if all parameters are zero
        if not n and not m and not t and not p:
            return

        # Lists to hold the fold instructions
        dlist, clist = [], []

        # Read fold direction and offset for each fold
        for _ in range(t):
            d, c = map(int, input().split())
            dlist.append(d)
            clist.append(c)

        # Read the list of coordinates for result queries after folds
        coorlist = [tuple(map(int, input().split())) for _ in range(p)]

        # Initialize the matrix with all elements set to 1
        oldm = [[1 for _ in range(m)] for _ in range(n)]

        # Apply each fold in sequence
        for d, c in zip(dlist, clist):
            if d == 1:  # Fold horizontally (→), over rows
                if 2 * c <= n:
                    # Case when folding from the top, keeping bottom part
                    newm = [[0 for _ in range(m)] for _ in range(n - c)]
                    for i in range(c):
                        for j in range(m):
                            # Fold upper part onto lower part
                            newm[i][j] = oldm[c + i][j] + oldm[c - 1 - i][j]
                    for i in range(c, n - c):
                        for j in range(m):
                            # Middle part remains unchanged
                            newm[i][j] = oldm[c + i][j]
                    n = n - c  # Update row count
                else:
                    # Case when folding from the bottom, keeping top part
                    newm = [[0 for _ in range(m)] for _ in range(c)]
                    for i in range(n - c):
                        for j in range(m):
                            # Fold lower part onto upper part
                            newm[i][j] = oldm[c + i][j] + oldm[c - 1 - i][j]
                    for i in range(n - c, c):
                        for j in range(m):
                            # Top part remains unchanged
                            newm[i][j] = oldm[c - 1 - i][j]
                    n = c  # Update row count
            else:  # Fold vertically (↑), over columns
                if 2 * c <= m:
                    # Case when folding from the left, keeping right part
                    newm = [[0 for _ in range(m - c)] for _ in range(n)]
                    for i in range(n):
                        for j in range(c):
                            # Fold left part onto right part
                            newm[i][j] = oldm[i][c + j] + oldm[i][c - 1 - j]
                    for i in range(n):
                        for j in range(c, m - c):
                            # Middle part remains unchanged
                            newm[i][j] = oldm[i][c + j]
                    m = m - c  # Update column count
                else:
                    # Case when folding from the right, keeping left part
                    newm = [[0 for _ in range(c)] for _ in range(n)]
                    for i in range(n):
                        for j in range(m - c):
                            # Fold right part onto left part
                            newm[i][j] = oldm[i][c + j] + oldm[i][c - 1 - j]
                    for i in range(n):
                        for j in range(m - c, c):
                            # Left part remains unchanged
                            newm[i][j] = oldm[i][c - 1 - j]
                    m = c  # Update column count
            # Update reference to the folded matrix for next iteration/fold
            oldm = newm

        # Output the value at each queried coordinate after all folds are complete
        for c in coorlist:
            print(oldm[c[0]][c[1]])

def visualize(mmap):
    """
    Visualizes a 2D matrix (mmap) by printing each value in a formatted manner.

    Args:
        mmap (list of list of int): The 2D matrix to visualize.

    Returns:
        None
    """
    print("------------------")
    for j in range(len(mmap[0])):
        print('|', end="")
        for i in range(len(mmap)):
            print(mmap[i][len(mmap[0]) - 1 - j], '|', end="")
        print()
    print("------------------")

if __name__ == '__main__':
    main()