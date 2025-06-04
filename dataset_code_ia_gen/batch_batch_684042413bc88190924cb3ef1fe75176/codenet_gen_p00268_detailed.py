import sys
import math
from collections import deque, defaultdict

sys.setrecursionlimit(10**7)

def ccw(a, b, c):
    """Calculate the cross product sign to determine the orientation of three points"""
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def intersect(a1, a2, b1, b2):
    """Check whether two line segments a1a2 and b1b2 intersect"""
    c1 = ccw(a1, a2, b1)
    c2 = ccw(a1, a2, b2)
    c3 = ccw(b1, b2, a1)
    c4 = ccw(b1, b2, a2)
    return c1 * c2 < 0 and c3 * c4 < 0

def inside_polygon(poly, p):
    """Check if point p is inside polygon poly (convex polygon) using ray casting method"""
    x, y = p
    inside = False
    n = len(poly)
    px, py = poly[0]
    for i in range(n+1):
        nx, ny = poly[i % n]
        if ((ny > y) != (py > y)) and (x < (px - nx) * (y - ny) / (py - ny) + nx):
            inside = not inside
        px, py = nx, ny
    return inside

def build_faces(C, W, pillars, walls):
    """
    - Construct the graph of edges (walls).
    - Find all faces (rooms and the outside) of the planar graph.
    - The polygon is convex, so outer face is well defined.
    We find faces by traversing edges in order. 
    Return: list of faces, each face is a list of vertex indices in CCW order.
    """

    # Build adjacency list with sorted edges in CCW order for each vertex.
    # Sorting edges in CCW order allows us to walk faces by following next edge in order.
    adj = [[] for _ in range(C)]
    # Store edges as tuples (from, to)
    for s, t in walls:
        adj[s-1].append(t-1)
        adj[t-1].append(s-1)
    
    # Sort adjacency according to angle to vertex
    def angle(i, j):
        x1, y1 = pillars[i]
        x2, y2 = pillars[j]
        return math.atan2(y2 - y1, x2 - x1)
    for i in range(C):
        adj[i].sort(key=lambda x: angle(i, x))
    
    # To find faces, use the planar graph face walking technique:
    # For each directed edge, if not visited, walk around the face on left side.
    visited_edge = set()
    faces = []

    for u in range(C):
        for vi in adj[u]:
            if (u, vi) in visited_edge:
                continue
            face = []
            cur = u
            nxt = vi
            while True:
                visited_edge.add((cur, nxt))
                face.append(cur)
                # At nxt vertex, find the edge (nxt -> next_w) which is next CCW edge from edge (nxt->cur)
                # get adjacency list of nxt
                neighbors = adj[nxt]
                index = neighbors.index(cur)
                # Next edge is the one before 'cur' in CCW order (in the sorted list, CCW order is ascending)
                # so the next edge after (cur->nxt) is the next edge in CCW order from (nxt->cur), it is next after index
                next_index = (index - 1) % len(neighbors)
                prev = nxt
                nxt = neighbors[next_index]
                cur = prev
                if cur == u and nxt == vi:
                    break
            faces.append(face)
    return faces

def point_in_polygon(p, polygon):
    # Ray casting method (works for convex or not)
    x, y = p
    inside = False
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % n]
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside

def main():
    input = sys.stdin.readline
    while True:
        C, W = map(int, input().split())
        if C == 0 and W == 0:
            break
        pillars = [tuple(map(int, (input().split()))) for _ in range(C)]
        walls = [tuple(map(int, (input().split()))) for _ in range(W)]

        # Step 1: Find all faces (rooms + outside) in the graph formed by pillars and walls
        faces = build_faces(C, W, pillars, walls)

        # Step 2: Identify which face is outside face
        # The outside face is the face with the largest area (since polygon is convex, so outside is unbounded)
        def polygon_area(face):
            pts = [pillars[v] for v in face]
            area = 0
            n = len(pts)
            for i in range(n):
                x1, y1 = pts[i]
                x2, y2 = pts[(i+1) % n]
                area += x1 * y2 - y1 * x2
            return abs(area) / 2
        areas = [polygon_area(face) for face in faces]
        outside_index = areas.index(max(areas))

        # Step 3: Build dual graph of the faces
        # Each wall is shared by exactly two faces (or one face and outside)
        # Construct a map from edges (smaller_index, larger_index) to faces
        edge_to_faces = defaultdict(list)
        for fi, face in enumerate(faces):
            n = len(face)
            for i in range(n):
                a = face[i]
                b = face[(i+1) % n]
                edge = (min(a,b), max(a,b))
                edge_to_faces[edge].append(fi)

        # Step 4: Build adjacency list of faces
        face_graph = [[] for _ in range(len(faces))]
        for edge, f_list in edge_to_faces.items():
            if len(f_list) == 2:
                f1, f2 = f_list
                face_graph[f1].append(f2)
                face_graph[f2].append(f1)
            # else touching outside only on one face (outside), handled below

        # Step 5: From outside face, BFS to get minimum distance (#holes) to go outside for each face
        dist = [-1] * len(faces)
        dist[outside_index] = 0
        queue = deque()
        queue.append(outside_index)

        while queue:
            cur = queue.popleft()
            for nxt in face_graph[cur]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[cur] + 1
                    queue.append(nxt)

        # The rooms are faces other than outside (outside face index)
        # For any room (face), the minimal holes passed to go outside is dist[face]
        # We want the maximum of dist over all rooms
        max_dist = max([dist[i] for i in range(len(faces)) if i != outside_index])
        print(max_dist)

if __name__ == "__main__":
    main()