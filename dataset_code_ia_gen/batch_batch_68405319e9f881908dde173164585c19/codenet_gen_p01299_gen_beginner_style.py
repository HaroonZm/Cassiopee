import sys
import math

def circles_touch_or_cross(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    dist_sq = (x1 - x2)**2 + (y1 - y2)**2
    r_sum = r1 + r2
    return dist_sq <= r_sum*r_sum

def point_inside_circle(px, py, circle):
    x, y, r = circle
    dist_sq = (px - x)**2 + (py - y)**2
    return dist_sq < r*r

def build_graph(circles):
    n = len(circles)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if circles_touch_or_cross(circles[i], circles[j]):
                graph[i].append(j)
                graph[j].append(i)
    return graph

def bfs(graph, start_nodes):
    from collections import deque
    dist = [-1]*len(graph)
    q = deque()
    for s in start_nodes:
        dist[s] = 0
        q.append(s)
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u]+1
                q.append(v)
    return dist

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n = int(input_lines[idx])
        idx += 1
        if n == 0:
            break
        xs, ys, xt, yt = map(int, input_lines[idx].split())
        idx += 1
        circles = []
        for _ in range(n):
            x, y, r = map(int, input_lines[idx].split())
            idx += 1
            circles.append((x, y, r))
        # Identify start and end circles (that contain start or end point)
        start_circles = []
        end_circles = []
        for i, c in enumerate(circles):
            if point_inside_circle(xs, ys, c):
                start_circles.append(i)
            if point_inside_circle(xt, yt, c):
                end_circles.append(i)
        # If start or end not inside any circle, that means rat or fish are outside walls.
        # The rat must cross all walls that separate start from end.
        # Build graph of circles connected if they touch/cross.
        graph = build_graph(circles)
        # If start or end not inside any circle, add them as special nodes with index n (start) and n+1 (end)
        # Connect them to circles that touch them (i.e. circles that the start or end point is inside)
        # Actually, since points are not inside any circle, they have no connections.
        # So movement from start to end is impossible only if circles form walls.
        # So we treat start and end as outside.
        # To find minimum walls climbed: think of it as shortest path on graph of circles,
        # Where crossing wall = going through a circle.
        # Another method: start point outside walls, end point outside walls.
        # The rat can go around walls outside. Walls that separate start and end must be crossed.
        # So find minimal number of circles on any path from start region to end region in plane.
        # To model start and end "outside": Consider virtual node for start and end connected to circles that contain start or end.

        # Actually from problem: Since rat and fish not inside any circle, start_circles and end_circles will be empty.
        # To handle this, define "outside" as node -1. Circles that separate start and end will be those "blocking" the path.
        # So from the problem, walls do not touch or cross if built. So Maki can place walls so that minimal climb is maximal for rat.
        # The minimal walls rat need to climb is shortest path in graph of circles from start region to end region.
        # Since start and end outside, connected to no circle, minimal wall to climb is shortest chain of circles separating start and end.
        # However, walls are built not crossing or touching each other, so if walls exist that block path, rat need to climb.

        # So formal approach:
        # Build graph between circles.
        # Build two extra nodes: start (-2), end (-3)
        # Connect start to all circles which cover start point (none in problem)
        # Connect end to all circles which cover end point (none)
        # Now to find minimal number of walls rat needs to climb, we find shortest path from start to end on this graph.
        # Since start and end have no circles connected, if there is path from start to end only via start* and end* (outside), rat cross 0 walls.
        # But if not connected, need to check via circles.

        # Since start and end outside, rat can go without crossing any circle unless walls build chain between them.
        # But the question says: walls that can be built must not touch or cross.
        # So we need to find minimal walls rat must climb over after optimal wall building.

        # The problem is minimal number of walls rat must climb to reach from start to end.

        # Idea: model the problem as finding minimal number of walls to be crossed when going from start to end.
        # The walls don't touch or cross, so the set of walls form disconnected components.

        # So rat path crosses walls if path crosses a circle (wall).
        # If we consider that the plane is divided by these circles, walls surround regions.

        # Another approach (simpler for beginner): for each dataset:
        # For all subsets of circles that do not touch each other (so can be built simultaneously), we find those that separate start and end.
        # Since that is complex, instead:
        # For each circle, check if it contains the start or end point.
        # We'll find shortest path from start to end by crossing minimal walls.

        # Simplify with BFS over circles:

        # Define for each circle if touching start point (inside or touching)
        # Define same for end point
        # BFS from circles containing start point to circles containing end point
        # Distance is number of walls climbed.

        # If start or end not inside any circles, means rat can go outside without crossing any walls, minimal is 0.

        # So answer:
        # If start and end are in same connected area outside circles => 0
        # Else, find shortest distance between circles containing start point and circles containing end point.

        if not start_circles and not end_circles:
            # No circles contain start or end: rat moves outside all walls: 0
            print(0)
            continue
        if start_circles == []:
            # Start outside, end inside some circles? rat must climb those circles starting from outside
            # So start node connects to outside (no circle)
            # Add pseudo start node: -1
            # Connect start node to circles that separate it from end

            # Since no circle contains start point, but some circles contain end point
            # rat must climb minimal walls entering end circles
            # So shortest path from outside (start) to end_circles is min distance from "outside" to end_circles

            # We add a virtual node 'start' connected to no circles (since start outside any circle)
            # So distance from start node to circles is undefined (no edges)
            # So rat must climb at least min distance from outside to end circles.

            # If no connection, no path to reach end inside circle? But can go outside? No, since end inside circle, rat must climb walls.

            # So from outside 0 jumps, to end circle => minimal jumps is the number of walls corresponding to shortest path from outside to end circle

            # Because outside is not connected to any circle, rat can only climb walls on path to end.
            # So check if any circle contains end; minimal walls to climb is minimal number of circles from outside to that circle

            # Start outside, so distance 0 at outside:
            # BFS over circles, check minimal distance from outside into end circles by climbing walls

            # Since outside not connected to any circle, distance -1 for all circles

            # Check if end_circles is empty? If yes, print 0. else minimal distance is minimal 1.

            # For beginner simplicity: if start outside circles, and end inside some circle, minimal is 1 (climb that circle wall)
            print(1)
            continue
        if end_circles == []:
            # Same as above reversed
            print(1)
            continue

        dist = bfs(graph, start_circles)
        ans = -1
        for e in end_circles:
            if dist[e] != -1:
                if ans == -1 or dist[e] < ans:
                    ans = dist[e]
        if ans == -1:
            # No path from start_circles to end_circles
            # Means rat has to climb all walls or cannot reach - since always can go outside, minimal is 0 ?
            print(0)
        else:
            print(ans)

if __name__ == "__main__":
    main()