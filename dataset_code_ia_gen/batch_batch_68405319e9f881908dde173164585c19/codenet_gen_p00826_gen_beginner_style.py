import sys
import math

def ccw(A, B, C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

def intersect(A,B,C,D):
    # Return True if line segments AB and CD intersect
    return (ccw(A,C,D) != ccw(B,C,D)) and (ccw(A,B,C) != ccw(A,B,D))

def line_intersection(p1, p2, p3, p4):
    # Compute intersection point of segments p1p2 and p3p4 assuming they intersect
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    x4,y4 = p4
    denom = (y4 - y3)*(x2 - x1) - (x4 - x3)*(y2 - y1)
    if abs(denom) < 1e-15:
        return None # Parallel or coincident
    t = ((x4 - x3)*(y1 - y3) - (y4 - y3)*(x1 - x3))/denom
    x = x1 + t*(x2 - x1)
    y = y1 + t*(y2 - y1)
    return (x,y)

def point_sub(a,b):
    return (a[0]-b[0], a[1]-b[1])

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def is_on_left(a,b,p):
    # Check if point p is on the left side of directed line a->b
    return cross(point_sub(b,a), point_sub(p,a)) > 0

def dist(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def inside_polygon(polygon, point=(0,0)):
    # Ray casting method to check if point is inside polygon
    # polygon is list of points in order
    cnt = 0
    x, y = point
    n = len(polygon)
    for i in range(n):
        x1,y1 = polygon[i]
        x2,y2 = polygon[(i+1)%n]
        if y1 == y2:
            continue
        if y < min(y1,y2):
            continue
        if y >= max(y1,y2):
            continue
        xint = (y - y1)*(x2 - x1)/(y2 - y1) + x1
        if xint > x:
            cnt +=1
    return (cnt % 2) == 1

def build_graph(lines):
    # Build graph of intersection points
    points = []
    points_map = dict()
    edges = dict()
    # collect all endpoints and intersections
    for i,line in enumerate(lines):
        for x in [ (line[0],line[1]),(line[2],line[3]) ]:
            if x not in points_map:
                points_map[x] = len(points)
                points.append(x)
    intersections = dict()
    n = len(lines)
    for i in range(n):
        for j in range(i+1,n):
            A = (lines[i][0], lines[i][1])
            B = (lines[i][2], lines[i][3])
            C = (lines[j][0], lines[j][1])
            D = (lines[j][2], lines[j][3])
            if intersect(A,B,C,D):
                p = line_intersection(A,B,C,D)
                # add point if new
                if p is None:
                    continue
                # Round to avoid floating point error
                p = (round(p[0],9),round(p[1],9))
                if p not in points_map:
                    points_map[p] = len(points)
                    points.append(p)
                intersections.setdefault(i,[]).append(p)
                intersections.setdefault(j,[]).append(p)
    # now for each line, create sorted points including endpoints and intersections
    graph = dict()
    for i,line in enumerate(lines):
        pts = [(line[0],line[1]), (line[2],line[3])]
        if i in intersections:
            for p in intersections[i]:
                pts.append(p)
        # sort points along the line segment
        p0 = (line[0],line[1])
        p1 = (line[2],line[3])
        def param(t):
            # parameter t from p0 to p1 where p = p0 + t*(p1-p0)
            dx = p1[0]-p0[0]
            dy = p1[1]-p0[1]
            if abs(dx) >= abs(dy):
                if dx == 0:
                    return 0
                return (t[0]-p0[0])/dx
            else:
                if dy == 0:
                    return 0
                return (t[1]-p0[1])/dy
        pts.sort(key=param)
        # create edges between consecutive points
        for k in range(len(pts)-1):
            a = points_map[pts[k]]
            b = points_map[pts[k+1]]
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
    return points, graph

def dfs(graph, start, visited):
    stack = [start]
    visited.add(start)
    while stack:
        u = stack.pop()
        for v in graph.get(u,[]):
            if v not in visited:
                visited.add(v)
                stack.append(v)

def find_faces(points, graph, lines):
    # This is a simple way: 
    # - for each edge, follow edges to make cycles (faces) going clockwise
    # We utilize that no three lines intersect at the same point and intersection points distant enough.
    # This approach may create repeated faces but should be enough for this problem.
    
    # For each vertex, sort neighbors by angle
    n = len(points)
    neighbors_sorted = dict()
    for u in graph:
        # compute angles from u to each neighbor
        ux,uy = points[u]
        nbrs = graph[u]
        def angle(v):
            vx,vy = points[v]
            ang = math.atan2(vy - uy, vx - ux)
            return (ang + 2*math.pi) % (2*math.pi)
        nbrs_sorted = sorted(nbrs, key=angle)
        neighbors_sorted[u] = nbrs_sorted

    faces = []
    visited_edges = set()
    for u in neighbors_sorted:
        for v in neighbors_sorted[u]:
            # check if edge (u,v) visited
            if (u,v) in visited_edges:
                continue
            face = []
            current = u
            prev = v
            face.append(u)
            while True:
                visited_edges.add((current,prev))
                face.append(prev)
                # find index of current in neighbors_sorted[prev]
                nbrs = neighbors_sorted[prev]
                idx = nbrs.index(current)
                # next vertex is neighbor after current counterclockwise
                next_idx = (idx - 1) % len(nbrs)
                nxt = nbrs[next_idx]
                if nxt == face[0] and prev == face[1]:
                    break
                current, prev = prev, nxt
            # remove last duplicated point
            face = face[:-1]
            # check if face size at least 3
            if len(face) < 3:
                continue
            # add face if new (avoid duplicates)
            face_set = set(face)
            repeated = False
            for f in faces:
                if face_set == set(f):
                    repeated = True
                    break
            if not repeated:
                faces.append(face)
    return faces

def polygon_contains_origin(polygon_points):
    # Check if origin is inside polygon
    # polygon_points is list of indices into points array
    polygon = [polygon_points[i] for i in range(len(polygon_points))]
    return inside_polygon(polygon, (0,0))

def is_origin_inside_face(face, points):
    poly = [ points[i] for i in face]
    return inside_polygon(poly, (0,0))

def main():
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx>=len(input_lines):
            break
        n = input_lines[idx].strip()
        idx+=1
        if n == '0':
            break
        n = int(n)
        lines = []
        for _ in range(n):
            x1,y1,x2,y2 = map(int, input_lines[idx].split())
            idx+=1
            lines.append( (x1,y1,x2,y2) )
        points, graph = build_graph(lines)
        faces = find_faces(points, graph, lines)
        # find face that contains origin (0,0)
        trapped = False
        for f in faces:
            poly = [points[i] for i in f]
            if inside_polygon(poly, (0,0)):
                # A face polygon contains the monster point => monster is inside a polygon formed by edges
                trapped = True
                break
        if trapped:
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    main()