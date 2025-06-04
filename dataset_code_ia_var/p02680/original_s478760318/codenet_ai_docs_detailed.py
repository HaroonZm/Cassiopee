def read_input():
    """
    Reads a single line of input and returns the split integers as a tuple.
    """
    return map(int, input().split())

def main():
    """
    Main function to solve a generalized grid region/area-filling problem.
    The code reads input specifying ranges and barriers on a grid, processes coordinate compression,
    populates prefix sum arrays for barriers, and finally uses BFS to compute the area of a region.

    The result is printed: either the computed area or 'INF' if the area is infinite.
    """

    # Constants and initial values
    INF = int(1e21)  # Large value to represent infinity
    r = range        # Reference to range for brevity

    # Read number of rectangles (n) and number of barriers (m)
    n, m = read_input()
    
    # f: initial interval boundaries, X, Y: sets for unique coordinates (for compression)
    f = [-INF, INF]
    X = set([0] + f)
    Y = set(X)

    # R: rectangles as edges, H: horizontal barriers (edges)
    R = [((f, INF)), ((f, -INF))]
    H = [((INF, f)), ((-INF, f))]

    # Read rectangles and update R, X, Y
    for _ in r(n):
        a, b, c = read_input()  # rectangle from [a, b] at coordinate c
        R.append(((a, b), c))
        Y.add(c)
        X.add(a)
        X.add(b)
    
    # Read barriers and update H, X, Y
    for _ in r(m):
        a, b, c = read_input()  # barrier at a, from [b, c]
        H.append((a, (b, c)))
        X.add(a)
        Y.add(b)
        Y.add(c)
    
    # Coordinate compression: mapping from compressed index to actual value
    s = dict(enumerate(sorted(X)))
    K = len(s)  # Total unique (X) coordinates
    t = dict(enumerate(sorted(Y)))
    L = len(t)  # Total unique (Y) coordinates

    # Reverse mapping (from value to compressed index)
    h = {v: k for k, v in s.items()}
    w = {v: k for k, v in t.items()}

    # Prepare prefix sum arrays for rectangle vertical edges(U), horizontal edges(V), and visited flags (v)
    V = [[0] * (K + 1) for _ in range(L + 1)]
    U = [row[:] for row in V]
    visited = [row[:] for row in V]

    # Mark vertical region boundaries in U
    for (a, b), c in R:
        U[w[c]][h[a]] += 1
        U[w[c]][h[b]] -= 1

    # Prefix sums for rectangles (fill horizontally)
    for i in r(L):
        for j in r(K):
            U[i][j+1] += U[i][j]
    
    # Mark horizontal region boundaries/barriers in V
    for d, (e, f) in H:
        V[w[e]][h[d]] += 1
        V[w[f]][h[d]] -= 1

    # Prefix sums for barriers (fill vertically)
    for j in r(K):
        for i in r(L):
            V[i+1][j] += V[i][j]
    
    # BFS (queue) for area filling, starting from (0,0) in compressed coordinates
    queue = [(h[0], w[0])]
    visited[w[0]][h[0]] = 1
    area = 0

    # Four possible movement directions (left, right, down, up)
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.pop()
        # Area is the rectangle from this x/y to the next in the sorted list
        area += (s[x] - s[x + 1]) * (t[y] - t[y + 1])
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check bounds and not previously visited
            if 0 <= nx < K and 0 <= ny < L and not visited[ny][nx]:
                # Check if not blocked vertically or horizontally
                vertical_block = U[(dy > 0) + y][x] if dx == 0 else 0
                horizontal_block = V[y][(dx > 0) + x] if dy == 0 else 0
                if vertical_block == 0 and horizontal_block == 0:
                    queue.append((nx, ny))
                    visited[ny][nx] = 1

    # If computed area exceeds infinity bound, report "INF"
    if area > INF:
        area = 'INF'
    
    print(area)

if __name__ == "__main__":
    main()