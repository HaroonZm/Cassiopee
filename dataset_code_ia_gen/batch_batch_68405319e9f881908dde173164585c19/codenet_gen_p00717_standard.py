import sys

def normalize(points):
    xs = [x for x, y in points]
    ys = [y for x, y in points]
    minx, miny = min(xs), min(ys)
    return [(x - minx, y - miny) for x, y in points]

def vec_diff(points):
    return [(points[i+1][0]-points[i][0], points[i+1][1]-points[i][1]) for i in range(len(points)-1)]

def rotate(vecs, deg):
    # Rotate by 0,90,180,270 degrees
    if deg == 0:
        return vecs
    if deg == 90:
        return [(-y,x) for x,y in vecs]
    if deg == 180:
        return [(-x,-y) for x,y in vecs]
    if deg == 270:
        return [(y,-x) for x,y in vecs]

def is_all_axis_aligned(vecs):
    return all((x == 0 or y == 0) and (x != 0 or y != 0) for x,y in vecs)

def encode_shape(points):
    # points assumed to have 90 deg turns and axis aligned segments
    # encode as sequence of moves (dx,dy)
    vecs = vec_diff(points)
    if not is_all_axis_aligned(vecs):
        return None
    return vecs

def canonical(vecs):
    # returns a normalized tuple to compare shapes considering rotation and reversal and translation
    # Try all 4 rotations and both directions, pick minimal lex
    candidates = []
    for r in [0,90,180,270]:
        rvecs = rotate(vecs,r)
        # original
        candidates.append(tuple(rvecs))
        # reversed
        candidates.append(tuple(rvecs[::-1]))
    # we want a canonical form which ignores translation (already encoded in relative vectors)
    # lex smallest used
    return min(candidates)

def read_points(m, input_iter):
    points = []
    for _ in range(m):
        x,y = map(int,next(input_iter).split())
        points.append((x,y))
    return points

def same_shape(template, candidate):
    if len(template) != len(candidate):
        return False
    tvecs = encode_shape(template)
    cvecs = encode_shape(candidate)
    if tvecs is None or cvecs is None:
        return False
    return canonical(tvecs) == canonical(cvecs)

def main():
    input_iter = iter(sys.stdin.read().splitlines())
    while True:
        line = next(input_iter)
        if line == '0':
            break
        n = int(line)
        polygons = []
        for _ in range(n+1):
            m = int(next(input_iter))
            pts = read_points(m, input_iter)
            polygons.append(pts)
        template = polygons[0]
        res = []
        for i in range(1,n+1):
            if same_shape(template, polygons[i]):
                res.append(i)
        for r in res:
            print(r)
        print("+++++")

if __name__ == "__main__":
    main()