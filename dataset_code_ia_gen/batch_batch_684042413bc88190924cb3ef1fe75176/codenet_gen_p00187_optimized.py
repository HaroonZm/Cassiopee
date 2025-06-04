import sys

def is_between(a, b, c):
    # Return True if c is on segment ab
    return min(a[0], b[0]) - 1e-9 <= c[0] <= max(a[0], b[0]) + 1e-9 and min(a[1], b[1]) - 1e-9 <= c[1] <= max(a[1], b[1]) + 1e-9

def line_intersection(p1, p2, p3, p4):
    # Compute intersection of segments p1p2 and p3p4
    # Using parametric form and Cramer's rule
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    A1 = y2 - y1
    B1 = x1 - x2
    C1 = A1*x1 + B1*y1
    A2 = y4 - y3
    B2 = x3 - x4
    C2 = A2*x3 + B2*y3
    det = A1*B2 - A2*B1
    if abs(det) < 1e-14:
        # parallel or coincident
        # Check collinearity by cross product
        v1 = (x2 - x1, y2 - y1)
        v2 = (x3 - x1, y3 - y1)
        cross = v1[0]*v2[1] - v1[1]*v2[0]
        if abs(cross) < 1e-14:
            return 'collinear'
        else:
            return None
    x = (C1*B2 - C2*B1)/det
    y = (A1*C2 - A2*C1)/det
    inter = (x, y)
    if is_between(p1, p2, inter) and is_between(p3, p4, inter):
        return inter
    else:
        return None

def area(a, b, c):
    # Compute area of triangle abc
    return abs((a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])) * 0.5)

def on_same_line(p1, p2, p3):
    # check if three points collinear
    v1 = (p2[0]-p1[0], p2[1]-p1[1])
    v2 = (p3[0]-p1[0], p3[1]-p1[1])
    cross = v1[0]*v2[1] - v1[1]*v2[0]
    return abs(cross) < 1e-14

def main():
    input_lines = sys.stdin.read().strip('\n\r ').split('\n')
    i = 0
    while i + 2 < len(input_lines):
        segs = []
        zero_line_found = False
        for j in range(3):
            if i+j >= len(input_lines):
                zero_line_found = True
                break
            line = input_lines[i+j].strip()
            if line == '0 0 0 0':
                zero_line_found = True
                break
            x1,y1,x2,y2 = map(int,line.split())
            segs.append(((x1,y1),(x2,y2)))
        if zero_line_found or len(segs)<3:
            break
        i += 3

        # Check if any two segments are collinear (same line)
        # Because in such a case, "三角形なし"
        # For each pair, check collinearity of 4 points (2 endpoints of each line)
        p = segs
        def same_line(s1,s2):
            # check if s1,s2 are collinear lines
            return on_same_line(s1[0], s1[1], s2[0]) and on_same_line(s1[0], s1[1], s2[1])
        collinear_pair = any(same_line(p[a],p[b]) for a in range(3) for b in range(a+1,3))
        if collinear_pair:
            print("kyo")
            continue

        # Find three intersection points of the pairs segments:
        # intersection between line 1 and 2, line 2 and 3, line 3 and 1
        inter12 = line_intersection(p[0][0], p[0][1], p[1][0], p[1][1])
        inter23 = line_intersection(p[1][0], p[1][1], p[2][0], p[2][1])
        inter31 = line_intersection(p[2][0], p[2][1], p[0][0], p[0][1])

        # All must be distinct points, must exist, and not None or 'collinear'
        inters = [inter12, inter23, inter31]
        if any(pt is None or pt == 'collinear' for pt in inters):
            print("kyo")
            continue

        # If all intersection points are same single point => no triangle
        x0, y0 = inters[0]
        if all(abs(x0 - x) < 1e-14 and abs(y0 - y) < 1e-14 for (x,y) in inters):
            print("kyo")
            continue

        # Check if points are collinear => area=0 => no triangle
        if on_same_line(inters[0], inters[1], inters[2]):
            print("kyo")
            continue

        tri_area = area(inters[0], inters[1], inters[2])
        if tri_area <= 1e-9:
            print("kyo")
            continue

        if tri_area >= 1900000:
            print("dai-kichi")
        elif tri_area >= 1000000:
            print("chu-kichi")
        elif tri_area >= 100000:
            print("kichi")
        elif tri_area > 0:
            print("syo-kichi")
        else:
            print("kyo")

if __name__=="__main__":
    main()