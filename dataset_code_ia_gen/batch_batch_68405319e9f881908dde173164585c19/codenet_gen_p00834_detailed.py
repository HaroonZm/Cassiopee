import sys
import math

def dist_sq(x1, y1, x2, y2):
    """Calculate squared distance between two points in 2D plane."""
    dx = x1 - x2
    dy = y1 - y2
    return dx*dx + dy*dy

def circles_intersect(c1, c2):
    """
    Check if two circles intersect or touch.
    c1, c2: tuples (x, y, r)
    They intersect or touch if distance between centers <= sum of radii.
    """
    d_sq = dist_sq(c1[0], c1[1], c2[0], c2[1])
    r_sum = c1[2] + c2[2]
    # Intersect or tangent if d <= r1+r2 and d >= |r1-r2|
    # But since no tangent spheres or discs at same z (at least 0.01 diff),
    # here just do <= r_sum^2
    return d_sq <= r_sum * r_sum

class UnionFind:
    """Union-Find (Disjoint Set Union) data structure for connected components."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        # Union by rank heuristic
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

def connected_components(circles):
    """
    Given a list of circles (x,y,r), calculate how many connected components
    considering two circles connected if intersect or touch.
    """
    n = len(circles)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i+1, n):
            if circles_intersect(circles[i], circles[j]):
                uf.union(i, j)
    roots = set(uf.find(i) for i in range(n))
    return len(roots)

def sphere_circle_intersection(z, sphere):
    """
    At height z, calculate circle cross-section of sphere.
    Return (x,y,radius) if circle exists (z in sphere),
    else None if plane outside sphere.
    Sphere: (X, Y, Z, R).
    The circle radius is sqrt(R^2 - (z-Z)^2)
    """
    X, Y, Z, R = sphere
    dz = abs(z - Z)
    if dz > R:
        return None
    r = math.sqrt(R*R - dz*dz)
    return (X, Y, r)

def sphere_vertical_range(sphere):
    """Return tuple (z_min, z_max) vertical extents of a sphere."""
    X, Y, Z, R = sphere
    return (Z - R, Z + R)

def spheres_intersection_z(s1, s2):
    """
    Compute z-coordinates where two spheres intersect in a plane.
    The intersection of two spheres is a circle.
    The z coordinates where the spheres' cross-sectional circles intersect are roots of:
    (x - X1)^2 + (y - Y1)^2 + (z - Z1)^2 = R1^2
    (x - X2)^2 + (y - Y2)^2 + (z - Z2)^2 = R2^2

    For each fixed z, the cross section is two circles in XY plane:
    Circle1: center (X1,Y1), radius r1 = sqrt(R1^2 - (z-Z1)^2)
    Circle2: center (X2,Y2), radius r2 = sqrt(R2^2 - (z-Z2)^2)
    They intersect if distance between centers <= r1 + r2 and >= abs(r1 - r2).

    We want z such that the two circles intersect at this height.
    The condition is:
    |r1 - r2| <= d_xy <= r1 + r2
    where d_xy = sqrt((X1-X2)^2 + (Y1-Y2)^2) fixed.

    Let D = distance between centers in XY plane squared.
    For each z, define
    r1(z) = sqrt(R1^2 - (z-Z1)^2)
    r2(z) = sqrt(R2^2 - (z-Z2)^2)

    The condition reduces to solving equations for z:
    (r1(z) + r2(z))^2 = D or (r1(z) - r2(z))^2 = D

    Convert this to a quartic or easier polynomial to solve.

    Let's solve for z exactly using the derived formula:
    We look for z such that circles touch/intersect, i.e.
    (r1 + r2)^2 = D or (r1 - r2)^2 = D.

    r1^2 = R1^2 - (z-Z1)^2
    r2^2 = R2^2 - (z-Z2)^2

    For sum:
    (r1 + r2)^2 = r1^2 + r2^2 + 2 r1 r2 = D
    Substitute r1^2 and r2^2:
    R1^2 - (z-Z1)^2 + R2^2 - (z-Z2)^2 + 2 r1 r2 = D
    2 r1 r2 = D - [R1^2 + R2^2 - (z-Z1)^2 - (z-Z2)^2]

    For difference:
    (r1 - r2)^2 = r1^2 + r2^2 - 2 r1 r2 = D
    Substitute similarly and solve.

    To avoid heavy algebra, do a numerical approach since N=100 max.
    We'll find z in [max(z_min1,z_min2), min(z_max1,z_max2)] where intersection(s) occur.

    Because no tangent spheres at same z differ at least 0.01, 
    we can do a few checks for candidate z by solving from equations.

    Instead, use the algebraic approach below.
    """

    X1, Y1, Z1, R1 = s1
    X2, Y2, Z2, R2 = s2
    # Distance squared between centers XY
    D = dist_sq(X1, Y1, X2, Y2)
    if D == 0 and R1 == R2 and Z1 == Z2:
        # Identical spheres -> infinite intersection? No per problem constraints
        return []
    # We'll solve equations (r1 + r2)^2 = D and (r1 - r2)^2 = D for z

    # Define f(z) = value to find roots for:
    # Using (r1 + r2)^2 - D = 0 and (r1 - r2)^2 - D = 0 to find intersection z

    # Let's define:
    # s = z
    # A = R1^2, B = R2^2
    # p = Z1, q = Z2

    # For (r1 + r2)^2 = D:
    # (sqrt(A - (s-p)^2) + sqrt(B - (s-q)^2))^2 = D
    # A - (s-p)^2 + B - (s-q)^2 + 2 sqrt[(A - (s-p)^2)(B - (s-q)^2)] = D
    # Rearrange:
    # 2 sqrt[(A - (s-p)^2)(B - (s-q)^2)] = D - A - B + (s-p)^2 + (s-q)^2
    # Square both sides:
    # 4 (A - (s-p)^2)(B - (s-q)^2) = [ D - A - B + (s-p)^2 + (s-q)^2 ]^2

    # For (r1 - r2)^2 = D:
    # (sqrt(A - (s-p)^2) - sqrt(B - (s-q)^2))^2 = D
    # A - (s-p)^2 + B - (s-q)^2 - 2 sqrt[(A - (s-p)^2)(B - (s-q)^2)] = D
    # Rearrange:
    # -2 sqrt[(A - (s-p)^2)(B - (s-q)^2)] = D - A - B + (s-p)^2 + (s-q)^2
    # Square both sides:
    # Same as above but sign changes cancel in square, so same equation is:
    # 4 (A - (s-p)^2)(B - (s-q)^2) = [ D - A - B + (s-p)^2 + (s-q)^2 ]^2

    # So both conditions reduce to solving this quartic polynomial in s, 
    # but roots of the polynomial give the points where the boundaries of intersection happen.

    # We'll solve the polynomial numerically using numpy roots.

    # Define polynomial coefficients for roots of above equation, or use numeric solver.
    # But we can precompute values and find roots with numpy.polyroots.

    import numpy as np

    A = R1*R1
    B = R2*R2
    p = Z1
    q = Z2

    # Let t = s, for clarity

    # Define function f(t):
    # 4*(A - (t-p)^2)*(B - (t-q)^2) - (D - A - B + (t-p)^2 + (t-q)^2)^2 = 0

    # Expand in powers of t:
    # It's a quartic in t.

    # Let u = (t-p)^2 = (t^2 - 2pt + p^2)
    # Let v = (t-q)^2 = (t^2 - 2qt + q^2)

    # Compute coefficients stepwise:

    # Expand 4*(A - u)*(B - v) = 4*(AB - A v - B u + u v)
    # Expand (D - A - B + u + v)^2 = (C + u + v)^2 with C = D - A - B

    # So
    # f(t) = 4AB - 4 A v - 4 B u + 4 u v - (C + u + v)^2 = 0

    # We'll write u = t^2 - 2pt + p^2
    # and v = t^2 - 2qt + q^2
    # then expand and collect terms to get coefficients of t^4, t^3, t^2, t, const

    # Define expressions:
    # u = t^2 - 2 p t + p^2
    # v = t^2 - 2 q t + q^2
    # C = D - A - B

    # Expand f(t):
    # f(t) = 4AB - 4 A v - 4 B u + 4 u v - (C + u + v)^2

    # First compute components:
    # 4 A v = 4 A (t^2 - 2 q t + q^2)
    # 4 B u = 4 B (t^2 - 2 p t + p^2)
    # 4 u v = 4 (t^2 - 2 p t + p^2)(t^2 - 2 q t + q^2)

    # And (C + u + v)^2 = (C + u + v)*(C + u + v) = Let's define w = C + u + v

    # Use sympy to help? But let's hand expand for numeric coding

    # Let's define polynomial coefficients in numpy poly order (highest degree first):
    # terms of t^4, t^3, t^2, t^1, t^0

    # Expand and collect coefficients:

    # u = t^2 - 2 p t + p^2
    # v = t^2 - 2 q t + q^2
    # u v = (t^2 - 2 p t + p^2)(t^2 - 2 q t + q^2)

    # Expand u v:
    # t^2 * t^2 = t^4
    # t^2 * (-2 q t) = -2 q t^3
    # t^2 * q^2 = q^2 t^2
    # (-2 p t) * t^2 = -2 p t^3
    # (-2 p t)* (-2 q t) = 4 p q t^2
    # (-2 p t)* q^2 = -2 p q^2 t
    # p^2 * t^2 = p^2 t^2
    # p^2 * (-2 q t) = -2 p^2 q t
    # p^2 * q^2 = p^2 q^2

    # Sum terms by degree:
    # t^4: 1
    # t^3: -2 q - 2 p = -2(p+q)
    # t^2: q^2 + 4 p q + p^2 = p^2 +4 p q + q^2
    # t^1: -2 p q^2 -2 p^2 q = -2 p q (q+p)
    # t^0: p^2 q^2

    # Next calculate coefficients of other terms similarly.

    # We write f(t) = 4AB - 4 A v - 4 B u + 4 u v - (C + u + v)^2

    # Compute polynomial coefficients for each term:

    # Term 1: 4AB is constant

    # Term 2: -4 A v = -4 A (t^2 - 2 q t + q^2)
    # Coefficients: t^2: -4 A
    # t^1: 8 A q
    # t^0: -4 A q^2

    # Term 3: -4 B u = -4 B (t^2 - 2 p t + p^2)
    # Coefficients: t^2: -4 B
    # t^1: 8 B p
    # t^0: -4 B p^2

    # Term 4: 4 u v
    # from above:
    # t^4: 4 * 1 = 4
    # t^3: 4 * (-2 (p+q)) = -8(p+q)
    # t^2: 4 * (p^2 + 4 p q + q^2) = 4 p^2 +16 p q +4 q^2
    # t^1: 4 * (-2 p q (p+q)) = -8 p q (p+q)
    # t^0: 4 * p^2 q^2 = 4 p^2 q^2

    # Term 5: -(C + u + v)^2
    # C + u + v = C + t^2 - 2 p t + p^2 + t^2 - 2 q t + q^2 = C + 2 t^2 - 2 (p+q) t + (p^2 + q^2)

    # Call M = C + 2 t^2 - 2 (p+q) t + (p^2 + q^2)

    # Expand M^2:
    # (a + b + c + d)^2 where
    # a = C (const),
    # b = 2 t^2
    # c = -2 (p+q) t = -2 S t (with S = p+q)
    # d = (p^2 + q^2) = P

    # M = a + b + c + d (relabel for clarity):

    # M = C + 2 t^2 - 2 S t + P

    # Expand M^2:

    # M^2 = (C + 2 t^2 + P - 2 S t)^2
    # = (C + P + 2 t^2 - 2 S t)^2
    # = (const + t^2 term + t term)^2

    # Square:
    # = (C + P)^2 + 4 (C+P) t^2 -4 (C + P) S t + 4 t^4 - 8 S t^3 + 4 S^2 t^2

    # Wait, expand carefully by distributive law:

    # (w + x + y)^2 = w^2 + x^2 + y^2 + 2 wx + 2 wy + 2 xy

    # Let w = C + P (const)
    # x = 2 t^2
    # y = -2 S t

    # w^2 = (C + P)^2
    # x^2 = (2 t^2)^2 = 4 t^4
    # y^2 = (-2 S t)^2 = 4 S^2 t^2
    # 2 wx = 2 * (C + P) * 2 t^2 = 4 (C+P) t^2
    # 2 wy = 2 * (C + P) * (-2 S t) = -4 (C+P) S t
    # 2 xy = 2 * (2 t^2)* (-2 S t) = 2 * 2 * (-2S) t^3 = -8 S t^3

    # Sum terms by degree of t:
    # t^4: 4
    # t^3: -8 S
    # t^2: 4 S^2 + 4 (C+P) = 4 S^2 + 4 C + 4 P
    # t^1: -4 (C+P) S
    # t^0: (C + P)^2

    S = p + q
    P = p*p + q*q
    C = D - A - B

    # Now sum all terms:

    # f(t) = 4AB 
    #       + (-4A) t^2 + (8A q) t + (-4A q^2)