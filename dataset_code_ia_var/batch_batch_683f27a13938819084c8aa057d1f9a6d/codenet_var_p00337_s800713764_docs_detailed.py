def quickhull(l, r, s, k, il, ir):
    """
    Recursively computes the convex hull points between points l and r.
    
    Given two points l and r, the list s of points (to be processed), a list k collecting hull points
    (as (point, index) tuples), and interval indices il and ir, this function identifies the "outermost"
    points from s with respect to segment l-r, and makes recursive calls to find additional hull points.
    
    Args:
        l (tuple): Left/beginning point of current segment (x, y).
        r (tuple): Right/ending point of segment (x, y).
        s (list): List of candidate points [(x, y), ...].
        k (list): Accumulator for hull points found so far [(point, index), ...].
        il (int): Index of l in the original order.
        ir (int): Index of r in the original order.
    
    Returns:
        tuple: Ordered list of hull points.
    """
    if not s:
        # Base case: no points to consider further between l and r.
        return

    su = []  # Points on one side of the line l-r (upper hull)
    sd = []  # Points on the other side (lower hull)
    a = (r[0] - l[0], r[1] - l[1])  # Vector from l to r
    
    # Partition points according to which side of l-r they lie on
    for x, y in s:
        b = (x - l[0], y - l[1])
        cro = cross(a, b)
        if cro > 0:
            su.append((x, y))  # Left of l->r (upper hull)
        elif cro < 0:
            sd.append((x, y))  # Right of l->r (lower hull)

    ind = (ir - il) / 2  # Midpoint index as heuristic for ordering

    # Process points on the upper side (if any)
    if su:
        c, d = direction(l, r, su[0])
        p = su[0]
        # Find the most extreme point with respect to l-r
        for i in range(1, len(su)):
            c_, d_ = direction(l, r, su[i])
            if c * d_ < c_ * d:
                c, d = c_, d_
                p = su[i]
        i = ir + ind
        k.append((tuple(p), i))
        b = (l[0] - p[0], l[1] - p[1])
        c_vec = (p[0] - r[0], p[1] - r[1])
        s1 = []
        s2 = []
        # Further partition points with respect to the new triangle l-p-r
        for x, y in su:
            b_ = (x - p[0], y - p[1])
            c_ = (x - r[0], y - r[1])
            cro_b, cro_c = cross(b, b_), cross(c_vec, c_)
            if cro_b >= 0 and cro_c >= 0:
                continue  # Point is inside triangle, not on the hull
            else:
                if cro_b < 0:
                    s1.append((x, y))
                elif cro_c < 0:
                    s2.append((x, y))
        # Recursive hull on left and right partitions
        quickhull(l, p, s1, k, il, i)
        quickhull(r, p, s2, k, ir, i)

    # Process points on the lower side (if any)
    if sd:
        c, d = direction(l, r, sd[0])
        p = sd[0]
        # Find the most extreme point with respect to l-r for lower hull
        for i in range(1, len(sd)):
            c_, d_ = direction(l, r, sd[i])
            if c * d_ < c_ * d:
                c, d = c_, d_
                p = sd[i]
        i = il + ind
        k.append((tuple(p), i))
        b = (l[0] - p[0], l[1] - p[1])
        c_vec = (p[0] - r[0], p[1] - r[1])
        s1 = []
        s2 = []
        # Partition lower points with respect to l-p and p-r
        for x, y in sd:
            b_ = (x - p[0], y - p[1])
            c_ = (x - r[0], y - r[1])
            cro_b, cro_c = cross(b, b_), cross(c_vec, c_)
            if cro_b <= 0 and cro_c <= 0:
                continue  # Inside triangle
            else:
                if cro_b > 0:
                    s1.append((x, y))
                elif cro_c > 0:
                    s2.append((x, y))
        # Recursively process
        quickhull(l, p, s1, k, il, i)
        quickhull(p, r, s2, k, i, ir)
    
    # After all, sort by position index and return the points in order
    k.sort(key=lambda x: x[1])
    return tuple(zip(*k))[0]

def cross(a, b):
    """
    Computes the 2D cross product of two vectors a and b.
    
    Args:
        a (tuple): Vector (x, y)
        b (tuple): Vector (x, y)
        
    Returns:
        int: Cross product a x b
    """
    return a[0] * b[1] - a[1] * b[0]

def direction(l, r, p):
    """
    Quantifies the signed distance and squared length relevant for convex hull point selection.
    
    Used in QuickHull to pick the farthest/outmost point relative to segment l-r.
    
    Args:
        l (tuple): Left endpoint (x, y)
        r (tuple): Right endpoint (x, y)
        p (tuple): Point to test (x, y)
    
    Returns:
        tuple: (squared area with respect to line l-r, squared norm of line l-r)
    """
    a = r[1] - l[1]
    b = l[0] - r[0]
    # Compute signed distance (up to scale) and squared length of lr
    return (a * (p[0] - l[0]) + b * (p[1] - l[1])) ** 2, a ** 2 + b ** 2

def root(x):
    """
    Finds the representative (root) of the set containing x in a Disjoint Set Union (Union Find) structure.
    
    Uses path compression for efficiency.
    
    Args:
        x (int): Node number
        
    Returns:
        int: Root representative of the set
    """
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]

def unite(x, y):
    """
    Unions the sets containing x and y in a Disjoint Set Union, using union by rank.
    
    Args:
        x (int): Node index
        y (int): Node index
    """
    x = root(x)
    y = root(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

from collections import defaultdict

# Read number of points and number of additional segments/edges
n, r = [int(x) for x in input().split()]

# Read n points (each with x, y coordinates)
s = [[int(x) for x in input().split()] for i in range(n)]
f = defaultdict(int)  # Map each point (x, y) to its index for fast lookup

for i in range(n):
    x, y = s[i]
    f[(x, y)] = i  # Map point to its index

# Copy and sort points for hull construction
q = [[s[i][j] for j in range(2)] for i in range(n)]
q.sort()

v = []  # List of extra given segments, as (index1, index2, cost)
for i in range(r):
    a, b = [int(x) for x in input().split()]
    a -= 1  # Convert to 0-based index
    b -= 1
    # Edge cost is Euclidean distance between points
    c = ((s[a][0] - s[b][0]) ** 2 + (s[a][1] - s[b][1]) ** 2) ** 0.5
    v.append((a, b, c))

# Sort edges/segments by their length (for later MST/greedy connection)
v.sort(key=lambda x: x[2])

# Get the lexicographically smallest and largest points for hull endpoints
l = tuple(q.pop(0))
r = tuple(q.pop(-1))

# Build convex hull list; indexes 0 and n mark start/end
lis = quickhull(l, r, q, [(l, 0), (r, n)], 0, n)

# Initialize Union Find structures for up to n+1 sets (with extra for hull super-node)
par = [i for i in range(n + 1)]  # Parent array
rank = [0] * (n + 1)  # Ranks for union by rank

# Make all convex hull points belong to the same component (root n)
for p in lis:
    par[f[p]] = n  # Assign hull points to supercomponent
    rank[n] = 1

l = 0  # Total minimal path/cost to be computed (used as output)

# Add the perimeter of the convex hull to total length
for i in range(len(lis)):
    l += ((lis[i - 1][0] - lis[i][0]) ** 2 + (lis[i - 1][1] - lis[i][1]) ** 2) ** 0.5

# Kruskal's-like process: connect remaining points using lowest-cost given edges
for x, y, c in v:
    if root(x) != root(y):
        l += c
        unite(x, y)

print(l)  # Output the total minimal path/cost