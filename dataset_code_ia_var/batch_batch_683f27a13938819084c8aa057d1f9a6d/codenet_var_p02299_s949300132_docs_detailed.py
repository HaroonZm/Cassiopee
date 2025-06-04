n = int(input())  # Read the number of vertices of the polygon

g = []
for i in range(n):
    # Read the coordinates of each polygon vertex, forming the polygon list
    g.append([int(i) for i in input().split()])

q = int(input())  # Read the number of queries (points to check containment for)

EPS = 0.001  # A small epsilon value for floating point comparisons

def dot(a, b):
    """
    Compute the dot product of two 2D vectors.

    Args:
        a (list): First vector [x, y].
        b (list): Second vector [x, y].

    Returns:
        int or float: The scalar dot product of vectors a and b.
    """
    return sum([i * j for i, j in zip(a, b)])

def sub(a, b):
    """
    Subtract two 2D vectors (a - b).

    Args:
        a (list): First vector [x, y].
        b (list): Second vector [x, y].

    Returns:
        list: The vector [a[0] - b[0], a[1] - b[1]].
    """
    return [a[0] - b[0], a[1] - b[1]]

def cross(a, b):
    """
    Compute the 2D cross product of vectors a and b.

    Args:
        a (list): First vector [x, y].
        b (list): Second vector [x, y].

    Returns:
        int or float: The scalar result of the cross product.
    """
    return a[0] * b[1] - a[1] * b[0]

def contains(g, p):
    """
    Determine the position of point p with respect to polygon g.

    This function uses the ray casting algorithm:
    - Returns 1 if the point is on an edge of the polygon.
    - Returns 2 if the point is strictly inside the polygon.
    - Returns 0 if the point is outside the polygon.

    Args:
        g (list of list): List of vertices making up the polygon (each a [x, y]).
        p (list): The query point [x, y].

    Returns:
        int: 0 (outside), 1 (on edge), or 2 (inside)
    """
    x = False  # Boolean flag to toggle when ray crosses an edge
    for i in range(n):
        # Get the vectors from the point to the polygon's current edge endpoints
        a = sub(g[i], p)
        b = sub(g[(i + 1) % n], p)
        # Check if point lies exactly on the edge (with floating point tolerance)
        if abs(cross(a, b)) < EPS and dot(a, b) < EPS:
            return 1  # On edge

        # Ensure a[1] <= b[1] for consistent intersection testing
        if a[1] > b[1]:
            a, b = b, a

        # Check if the ray from the point to the right crosses the polygon edge
        if a[1] < EPS and EPS < b[1] and cross(a, b) > EPS:
            x = not x  # Flip the inside/outside flag

    return 2 if x else 0  # 2 for inside, 0 for outside

# Query section: for each point, check if it is inside, on edge, or outside the polygon
for i in range(q):
    x, y = map(int, input().split())
    print(contains(g, [x, y]))