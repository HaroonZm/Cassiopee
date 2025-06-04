import sys
import collections

# Directions as vectors
DIRS = {
    '+x': (1,0,0),
    '-x': (-1,0,0),
    '+y': (0,1,0),
    '-y': (0,-1,0),
    '+z': (0,0,1),
    '-z': (0,0,-1)
}

def parse_description(elements):
    n = int(elements[0])
    elems = elements[1:1+n]

    labels = {}
    paths = []
    i = 0

    # label -> coordinate
    label_points = {}

    # The first path starts at origin
    origin = (0,0,0)
    curr_path_points = []
    curr_pos = origin
    curr_path_points.append(curr_pos)

    prev_label = None

    while i < n:
        e = elems[i]
        if e in DIRS:
            v = DIRS[e]
            new_pos = (curr_pos[0]+v[0], curr_pos[1]+v[1], curr_pos[2]+v[2])
            curr_path_points.append(new_pos)
            curr_pos = new_pos
            i += 1
        else:
            # positive integer label
            label = int(e)
            if label not in label_points:
                # First occurrence: label current point
                label_points[label] = curr_pos
                i += 1
            else:
                # Second or more occurrence: start new path at label point
                if curr_path_points:
                    paths.append(curr_path_points)
                start_point = label_points[label]
                curr_path_points = [start_point]
                curr_pos = start_point
                i += 1
    if curr_path_points:
        paths.append(curr_path_points)

    return paths

def edges_from_paths(paths):
    edges = set()
    points = set()
    for path in paths:
        for i in range(len(path)):
            points.add(path[i])
        for i in range(len(path)-1):
            a = path[i]
            b = path[i+1]
            # undirected edge as tuple sorted
            edge = (a,b) if a < b else (b,a)
            if edge in edges:
                # duplicate edge -> invalid but problem says input valid, so ignore
                pass
            edges.add(edge)
    return edges, points

def vectors_sub(p1, p0):
    return (p1[0]-p0[0], p1[1]-p0[1], p1[2]-p0[2])

def vectors_add(p1, p2):
    return (p1[0]+p2[0], p1[1]+p2[1], p1[2]+p2[2])

def vectors_eq(p1, p2):
    return p1[0]==p2[0] and p1[1]==p2[1] and p1[2]==p2[2]

def matrices_mul(m1, m2):
    # 3x3 matrices multiplication
    res = tuple(
        tuple(
            sum(m1[i][k]*m2[k][j] for k in range(3)) for j in range(3)
        ) for i in range(3)
    )
    return res

def matrix_vec_mul(m,v):
    return (
        m[0][0]*v[0]+m[0][1]*v[1]+m[0][2]*v[2],
        m[1][0]*v[0]+m[1][1]*v[1]+m[1][2]*v[2],
        m[2][0]*v[0]+m[2][1]*v[1]+m[2][2]*v[2])

# all 24 rotation matrices of cube
def generate_rotations():
    rots = []
    # basic axis vectors
    axes = [(1,0,0),(0,1,0),(0,0,1)]
    # from https://stackoverflow.com/a/16467849 reference, generate 24 rotation matrices
    def cross(a,b):
        return (
            a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

    from itertools import permutations, product
    perms = permutations([0,1,2]) # axes permutations
    signs = product([1,-1],repeat=3)
    for perm in perms:
        for sign in signs:
            x = [0,0,0]
            y = [0,0,0]
            z = [0,0,0]
            x[perm[0]] = sign[0]
            y[perm[1]] = sign[1]
            z[perm[2]] = sign[2]
            # check right-handedness: x cross y == z
            cx = cross(tuple(x),tuple(y))
            if cx == tuple(z):
                m = (tuple(x),tuple(y),tuple(z))
                rots.append(m)
    return rots

ROTATIONS = generate_rotations()

def transform(edges, rot, translate):
    # edges is set of undirected edges (point tuples)
    new_edges = set()
    for a,b in edges:
        a1 = matrix_vec_mul(rot,a)
        b1 = matrix_vec_mul(rot,b)
        a2 = (a1[0]+translate[0], a1[1]+translate[1], a1[2]+translate[2])
        b2 = (b1[0]+translate[0], b1[1]+translate[1], b1[2]+translate[2])
        edge = (a2,b2) if a2 < b2 else (b2,a2)
        new_edges.add(edge)
    return new_edges

def normalize_points(points):
    # translate so min x,y,z -> 0, or translate to origin chosen point
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    zs = [p[2] for p in points]
    return (min(xs),min(ys),min(zs))

def edges_equal(e1,e2):
    if len(e1) != len(e2):
        return False
    # edges are sets of pairs of points
    return e1 == e2

def read_description():
    elements = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if line == '':
            continue
        elements += line.split()
        if len(elements) == 0:
            continue
        n = int(elements[0])
        if len(elements) >= n+1:
            break
    # In some cases line after n contains all elements, else read further
    while len(elements) < n+1:
        line = sys.stdin.readline()
        if not line:
            break
        elements += line.strip().split()
    return elements

def main():
    while True:
        first_line = sys.stdin.readline()
        if not first_line:
            break
        first_line = first_line.strip()
        if first_line == '0':
            break
        # read first key description
        n = int(first_line)
        desc1 = [first_line]
        while len(desc1) < n+1:
            line = sys.stdin.readline()
            if not line:
                break
            desc1 += line.strip().split()
        # read second key description
        first_line2 = sys.stdin.readline()
        if not first_line2:
            break
        n2 = int(first_line2.strip())
        desc2 = [first_line2.strip()]
        while len(desc2) < n2+1:
            line = sys.stdin.readline()
            if not line:
                break
            desc2 += line.strip().split()

        paths1 = parse_description(desc1)
        paths2 = parse_description(desc2)

        edges1, points1 = edges_from_paths(paths1)
        edges2, points2 = edges_from_paths(paths2)

        # if number of edges differ, definitely different
        if len(edges1) != len(edges2):
            print("DIFFERENT")
            continue

        # Try all rotations to match edges
        # Choose an anchor point in key1: origin is always in points1 (first path start)
        # For key2, try all points as anchor
        found = False
        pts1 = list(points1)
        pts2 = list(points2)

        # We want to map points1 to points2, try aligning origin (0,0,0) in first to some point in second
        # Identify origin in first (path1 starting point)
        origin1 = paths1[0][0]

        for rot in ROTATIONS:
            # rotate all points in key2 by rot
            rotated_points2 = [matrix_vec_mul(rot,p) for p in pts2]
            rotated_edges2 = set()
            for a,b in edges2:
                a2 = matrix_vec_mul(rot,a)
                b2 = matrix_vec_mul(rot,b)
                edge = (a2,b2) if a2 < b2 else (b2,a2)
                rotated_edges2.add(edge)
            # try all possible translations aligning origin1 to rotated point in rotated_points2
            pt_set2 = set(rotated_points2)
            for p2 in rotated_points2:
                # translation vector to map p2 -> origin1
                t = (origin1[0]-p2[0], origin1[1]-p2[1], origin1[2]-p2[2])
                # translate rotated edges2 by t
                transformed_edges2 = transform(edges2, rot, t)
                if edges_equal(edges1, transformed_edges2):
                    found = True
                    break
            if found:
                break
        print("SAME" if found else "DIFFERENT")

if __name__=="__main__":
    main()