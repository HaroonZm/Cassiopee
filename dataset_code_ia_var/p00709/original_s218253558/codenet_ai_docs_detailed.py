import sys

# Assign input/output stream functions for faster I/O
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    The main function to process a test case of the problem.

    Reads the width (W) and height (H) of a grid, loads the grid from input,
    and then computes the minimum number of certain submatrices (squares) whose union covers every '1' in the input matrix.
    The algorithm uses dynamic programming and bitmasks to achieve this.
    
    Returns:
        bool: False if the matrix has width zero (end of dataset), True otherwise.
    """
    # Read the dimensions of the matrix
    W, H = map(int, readline().split())
    if W == 0:
        return False  # Exit when the width is 0 (problem input convention)

    # Load the matrix from input; MP[i][j] is 1 if cell is filled, 0 otherwise
    MP = [list(map(int, input().split())) for i in range(H)]

    # C[i][j]: For each cell, number of consecutive 1s downwards starting at (i, j)
    C = [[0]*W for _ in range(H)]
    for j in range(W):
        cur = 0
        for i in range(H-1, -1, -1):
            if MP[i][j]:
                cur += 1
            else:
                cur = 0
            C[i][j] = cur

    # D[i][j]: Maximum size of a square whose top-left corner is at (i, j)
    D = [[0]*W for _ in range(H)]
    # E[i][j]: Helper array for dynamic propagation of square sizes during greedy covering
    E = [[0]*W for _ in range(H)]
    for i in range(H):
        st = []  # Stack for maintaining monotonically increasing histogram
        for j in range(W):
            c = C[i][j]  # The column height at (i, j)
            last = j
            # Update the possible maximum square size ending before current j
            while st and c <= st[-1][0]:
                p, k = st.pop()  # Height, position
                last = k
                d = min(j - k, p)
                for e in range(k, j-d+1):
                    D[i][e] = max(D[i][e], d)
            st.append((c, last))
        # Finalize the remainings in the stack
        while st:
            p, k = st.pop()
            d = min(W - k, p)
            if d:
                for e in range(k, W-d+1):
                    D[i][e] = max(D[i][e], d)
        st.append((W, 0))  # Dummy for stability

    # S: Positions (indices) of grid cells where a square can be placed
    # Z: Maximum square size at each position S[i]
    S = []
    Z = [0]*(W*H)  # Z[x]: maximum square size for coordinate index x
    ALL = 0  # Bitmask representing all filled positions to be covered

    # Prepare coverage data: build ALL, find all square starts and their sizes
    for i in range(H):
        for j in range(W):
            index = i*W + j  # Flatten 2D index
            if MP[i][j]:
                ALL |= 1 << index  # Mark position as needing coverage
            if E[i][j] < D[i][j]:
                S.append(index)   # Candidate square position
                Z[index] = D[i][j]
            E[i][j] = e = max(E[i][j], D[i][j])
            # Update E for "spreading" the square to adjacent positions, controlling overlap
            if e > 1:
                if i+1 < H:
                    E[i+1][j] = max(E[i+1][j], e-1)
                if j+1 < W:
                    E[i][j+1] = max(E[i][j+1], e-1)
                if i+e-1 < H and j+e-1 < W:
                    E[i+e-1][j+e-1] = max(E[i+e-1][j+e-1], 1)

    SN = len(S)  # Number of candidate squares
    L = max(W, H)  # Maximum possible side length

    # T[d]: Bitmask for a full square of size d aligned at the (0,0) cell (W*H mask)
    T = [0]*(L+1)
    for d in range(1, L+1):
        v = 0
        for i in range(d):
            for j in range(d):
                v |= 1 << (i*W + j)
        T[d] = v

    # For each square candidate, store its coverage mask and the single cell mask at S[i]
    BS = [0]*SN  # BS[i]: Bitmask for square at S[i] of size Z[S[i]]
    CS = [0]*SN  # CS[i]: Bitmask for S[i] itself
    for i in range(SN):
        s = S[i]
        BS[i] = T[Z[s]] << s  # Move base mask for square to the correct cell
        CS[i] = 1 << s        # Cell mask

    # Memoization array for DP; one dict per candidate square
    memo = [{} for _ in range(SN)]

    def dfs(i, state):
        """
        Recursively try to cover all target cells using placements of squares,
        minimizing the total number placed.

        Args:
            i (int): index in S
            state (int): bitmask of cells already covered

        Returns:
            int: minimal number of squares to add to cover all required cells from this state
        """
        if i == SN:
            # All square positions examined: success if all covered
            if state == ALL:
                return 0
            return W*H  # Impossible: too many squares (will be minimized away)
        if state in memo[i]:
            return memo[i][state]
        r = W*H  # Start with worst-case value
        # Skip this square if its origin is already covered
        if state & CS[i]:
            r = min(r, dfs(i+1, state))
        # Try placing this square if it adds any new covered cell
        if state & BS[i] != BS[i]:
            r = min(r, dfs(i+1, state | BS[i]) + 1)
        memo[i][state] = r
        return r

    # Output result
    write("%d\n" % dfs(0, 0))
    return True

# Main loop: keep processing test cases until solve() returns False
while solve():
    ...