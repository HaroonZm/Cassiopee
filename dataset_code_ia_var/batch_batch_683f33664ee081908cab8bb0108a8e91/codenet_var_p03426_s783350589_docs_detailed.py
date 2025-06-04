def sol():
    """
    Reads grid dimensions and values, precomputes distances for "jumping" on the grid with step d,
    and answers a number of range queries regarding accumulated moves between cells labeled l and r.
    Input:
        First line: h w d (integers) - grid height, width, and jump distance
        Next h lines: w integers each - grid cell values (each integer between 1 and h*w)
        Next line: q (integer) - number of queries
        Next q lines: each two integers l r - query range
    Output:
        For each query, prints one integer: the computed answer for that query.
    """
    # Read grid height h, width w, and jump distance d
    h, w, d = map(int, input().split())
    
    # Read grid values and store as a 2D list 'a'
    a = []
    for _ in range(h):
        row = [int(i) for i in input().split()]
        a.append(row)
    
    # Build a dictionary mapping each grid value to its (row, col) position
    t = {}  # key: value, value: (row, col) position in the grid
    for i in range(h):
        for j in range(w):
            t[a[i][j]] = (i, j)
    
    # Precompute answers for all positions
    # ans[i]: accumulated distance from i to i+d to i+2d ... up to max value <= h*w
    ans = [0] * (h * w + 1)
    # Start backward: for each i, calculate ans[i-d] based on ans[i] and manhattan distance
    for i in range(h * w, d, -1):
        # Get current position (row o, col p) of value i
        o, p = t[i]
        # Get position of value i-d
        prev_o, prev_p = t[i - d]
        # Calculate the move cost (Manhattan distance)
        move_cost = abs(o - prev_o) + abs(p - prev_p)
        # Accumulate total moves needed from i-d upwards
        ans[i - d] = ans[i] + move_cost
    
    # Read number of queries
    q = int(input())
    # For each query, compute and print the result
    for _ in range(q):
        l, r = map(int, input().split())
        # The answer is the total move cost from value l to value r in steps of d
        # Since ans[i] accumulates costs to the "end", ans[l] - ans[r] gives the required sum
        print(ans[l] - ans[r])

if __name__ == "__main__":
    sol()