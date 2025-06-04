def vector_sub(a, b):
    return [a[i] - b[i] for i in range(3)]

def dot(a, b):
    return sum(a[i] * b[i] for i in range(3))

def cross(a, b):
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

def is_point_in_triangle(p, a, b, c):
    # Check if point p lies inside triangle abc (including boundary)
    v0 = vector_sub(c, a)
    v1 = vector_sub(b, a)
    v2 = vector_sub(p, a)

    dot00 = dot(v0, v0)
    dot01 = dot(v0, v1)
    dot02 = dot(v0, v2)
    dot11 = dot(v1, v1)
    dot12 = dot(v1, v2)

    denom = dot00 * dot11 - dot01 * dot01
    # In case of degenerate triangle
    if denom == 0:
        return False

    u = (dot11 * dot02 - dot01 * dot12) / denom
    v = (dot00 * dot12 - dot01 * dot02) / denom

    return (u >= 0) and (v >= 0) and (u + v <= 1)

def point_in_triangle_3d(p, a, b, c):
    # Use barycentric coordinates in 3D by projecting to the triangle's plane
    # Compute normal vector of triangle plane
    ab = vector_sub(b, a)
    ac = vector_sub(c, a)
    normal = cross(ab, ac)

    # Check if p is in the same plane (allow small tolerance)
    ap = vector_sub(p, a)
    if abs(dot(ap, normal)) > 1e-9:
        return False

    return is_point_in_triangle(p, a, b, c)

def is_point_on_segment(p, a, b):
    # Check if p lies on the segment ab (including endpoints)
    ap = vector_sub(p, a)
    bp = vector_sub(p, b)
    ab = vector_sub(b, a)
    cross_prod = cross(ap, ab)
    if any(abs(x) > 1e-9 for x in cross_prod):
        return False
    # Check if dot products are in range
    if dot(ap, ab) < -1e-9:
        return False
    if dot(bp, vector_sub(a,b)) < -1e-9:
        return False
    return True

def segment_intersects_triangle(p1, p2, a, b, c):
    d = vector_sub(p2, p1)
    ab = vector_sub(b, a)
    ac = vector_sub(c, a)
    normal = cross(ab, ac)

    denom = dot(normal, d)
    if abs(denom) < 1e-15:
        # Line is parallel to plane
        # Check if segment lies in the plane and intersects triangle
        ap1 = vector_sub(p1, a)
        if abs(dot(normal, ap1)) > 1e-9:
            return False
        # Segment lies in the plane - check overlap
        # Project to 2D to check intersection
        # Because the problem states no degenerate cases, we can return False here
        return False

    t = dot(normal, vector_sub(a, p1)) / denom
    if t < -1e-9 or t > 1 + 1e-9:
        return False

    intersection = [p1[i] + t * d[i] for i in range(3)]

    # If intersection is at endpoints, it counts as hitting barrier
    if any(abs(intersection[i] - p1[i]) < 1e-9 for i in range(3)) or any(abs(intersection[i] - p2[i]) < 1e-9 for i in range(3)):
        return True

    return point_in_triangle_3d(intersection, a, b, c)

def main():
    UAZ = list(map(int, input().split()))
    enemy = list(map(int, input().split()))
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    v3 = list(map(int, input().split()))

    # If enemy is inside triangle
    if point_in_triangle_3d(enemy, v1, v2, v3):
        print("MISS")
        return

    # Check if segment UAZ->enemy intersects the barrier triangle
    if segment_intersects_triangle(UAZ, enemy, v1, v2, v3):
        print("MISS")
        return

    print("HIT")

if __name__ == "__main__":
    main()