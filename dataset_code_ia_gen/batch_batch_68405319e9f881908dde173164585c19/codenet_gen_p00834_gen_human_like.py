import sys
import math

sys.setrecursionlimit(10**7)

def find(parents, x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(parents, ranks, x, y):
    xroot = find(parents, x)
    yroot = find(parents, y)
    if xroot == yroot:
        return
    if ranks[xroot] < ranks[yroot]:
        parents[xroot] = yroot
    else:
        parents[yroot] = xroot
        if ranks[xroot] == ranks[yroot]:
            ranks[xroot] += 1

def discs(z, spheres):
    circles = []
    for (X, Y, Z, R) in spheres:
        dz = z - Z
        if abs(dz) <= R:
            r = math.sqrt(R*R - dz*dz)
            circles.append((X, Y, r))
    return circles

def connected_components(circles):
    n = len(circles)
    if n == 0:
        return 0
    parents = list(range(n))
    ranks = [0]*n
    for i in range(n):
        x1, y1, r1 = circles[i]
        for j in range(i+1, n):
            x2, y2, r2 = circles[j]
            dx = x1 - x2
            dy = y1 - y2
            dist = math.hypot(dx, dy)
            # Touching or intersecting
            if dist <= r1 + r2 + 1e-12:
                union(parents, ranks, i, j)
    roots = set(find(parents, i) for i in range(n))
    return len(roots)

def find_events(spheres):
    events = set()
    for i, (X1, Y1, Z1, R1) in enumerate(spheres):
        # bottom and top of sphere
        events.add(Z1 - R1)
        events.add(Z1 + R1)
    n = len(spheres)
    for i in range(n):
        X1, Y1, Z1, R1 = spheres[i]
        for j in range(i+1, n):
            X2, Y2, Z2, R2 = spheres[j]
            dx = X2 - X1
            dy = Y2 - Y1
            dz = Z2 - Z1
            d2 = dx*dx + dy*dy + dz*dz
            d = math.sqrt(d2)
            # spheres not mutually tangent, so d != R1+R2 or abs(R1-R2)
            # but intersection of spheres creates circle, we find z values of that circle 
            # The intersection of two spheres is a circle if they intersect
            if d < R1 + R2 and d > abs(R1 - R2):
                # The circle lies in a plane z = c ± h where c = Z1 + t*dz/d, t such that circle center
                # projection on the line between centers, from formula from geometry of sphere intersections
                # Reader methods:https://mathworld.wolfram.com/Sphere-SphereIntersection.html
                # Solve via "plane of intersection"
                # Compute t = (d2 + R1^2 - R2^2)/(2*d)
                t = (d2 + R1*R1 - R2*R2) / (2*d)
                # circle center coordinates = (X1 + t*dx/d, Y1 + t*dy/d, Z1 + t*dz/d)
                # radius of circle = sqrt(R1^2 - t^2)
                # Then circle is in plane z = Z1 + t*dz/d
                cz = Z1 + t * dz / d
                r_circle = math.sqrt(R1*R1 - t*t)
                # Circle in horizontal plane z=cz, its vertical extent is cz ± r_circle
                events.add(cz - r_circle)
                events.add(cz + r_circle)
    return sorted(events)

def main():
    input = sys.stdin.readline
    while True:
        N = int(input())
        if N == 0:
            break
        spheres = []
        for _ in range(N):
            X, Y, Z, R = map(int, input().split())
            spheres.append((X, Y, Z, R))
        events = find_events(spheres)
        # Add z=0 and z=36000 if not present, as problem states from 0 to 36000
        if 0.0 not in events:
            events = [0.0] + events
        if 36000.0 not in events:
            events.append(36000.0)
        # We will consider the cross section number of components for each event point and for z=0 and z=36000

        # We only consider event points within 0 to 36000
        events = [z for z in events if 0 <= z <= 36000]

        # Sort again after adding bounds
        events.sort()

        # Compute number of connected components for each event z
        counts = []
        for z in events:
            c = connected_components(discs(z, spheres))
            counts.append(c)
        # We want binary transitions of number of connected figures as the plane moves up from bottom to top
        # Generate bit: 1 if count increases, 0 if decreases, ignore if equal (no equal per problem statement?)
        # Problem states to assign 1 for increment and 0 for decrement in the transitions between counts
        transitions = []
        for i in range(1, len(counts)):
            if counts[i] > counts[i-1]:
                transitions.append('1')
            else:
                transitions.append('0')

        # Print result
        print(len(transitions))
        print("".join(transitions))

if __name__ == '__main__':
    main()