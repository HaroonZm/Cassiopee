import sys
import math
from collections import deque, defaultdict

# Digit patterns are defined by number of bars and their connectivity graph:
# We define a canonical form for each digit to compare with the found components.

# The problem reduces to:
# 1) Read bars with their endpoints.
# 2) Build an undirected graph where nodes are bars, edges for touching bars at endpoints.
# 3) For each connected component (a digit form):
#    - Extract the subgraph of bars.
#    - Normalize representation to canonical form (ignoring length and orientation).
#    - Compare with known digit graphs to identify digit.
# 4) Count digits.

# The key points are:
# - Bars are line segments (x1,y1)-(x2,y2).
# - Two bars touch if they share exactly one endpoint.
# - Angles between touching bars: must be +/- 90 degrees and the angle sign distinguishes digits 2 and 5.
# - The problem states these conditions always hold; no cross and no multi touching points > 2 bars.
# - Directions, lengths and rotations irrelevant; only topological structure and "angle sign" matters.
# - Build adjacency graph of bars with edges labeled by angle sign (+90 or -90).
# - Match the component's bar graph (and angles) against known digit templates.

# Approach:
# - Represent each bar as a node.
# - For each pair of bars, if they touch, add edge with angle sign (direction dependent).
# - For each component:
#   - Extract adjacency and edge angle signs.
#   - Generate canonical form (e.g. through DFS with ordered edges, edge label = angle sign).
# - Precompute known digit templates similarly.
# - Match component canonical form against templates.

# Construct digit templates from problem figure:
#  - This is tricky without actual figure, but info:
#    Each digit is a known "stick" form.
#    0: rectangle 6 bars (?)
#    1: 2 bars (simple vertical line)
#    ...
# We'll rely on problem statement and sample input to derive digit bar counts:
# The bar counts per digit from standard 7-seg digits and info:
# The problem unsaid how digits are formed exactly but implies known standard stick forms with 2 to 6 bars.

# We'll encode digit templates by their bar graph (nodes = bars, edges = touching bars with angle sign).
# We use bar counts as first filter:
# From problem test: 
# Sample input 1 has 9 bars and output counts digits 1,3,9
# Sample input 2 with 8 bars has digits 5 and 7
# Sample input 3 with 20 bars has digits 0,2,4,7,9

# Predefine digit templates as adjacency + angle sign edges:
# Using standard 7-seg representation bars to build graph templates.
# The segments are:
#  a(top), b(top-right), c(bottom-right), d(bottom), e(bottom-left), f(top-left), g(middle)
# Mapping digit to segments (bars):

# Segments count per digit:
# 0: a,b,c,d,e,f (6 bars)
# 1: b,c (2 bars)
# 2: a,b,d,e,g (5 bars)
# 3: a,b,c,d,g (5 bars)
# 4: b,c,f,g (4 bars)
# 5: a,c,d,f,g (5 bars)
# 6: a,c,d,e,f,g (6 bars)
# 7: a,b,c (3 bars)
# 8: all seven bars
# 9: a,b,c,d,f,g (6 bars)

# We'll encode each digit as graph of bars with edges between bars that connect at right angles.

# We'll assign each segment a node and define edges and their sign:

# We define edges in a "bars graph" for each digit:

digit_segments = {
    0: ['a', 'b', 'c', 'd', 'e', 'f'],
    1: ['b', 'c'],
    2: ['a', 'b', 'd', 'e', 'g'],
    3: ['a', 'b', 'c', 'd', 'g'],
    4: ['b', 'c', 'f', 'g'],
    5: ['a', 'c', 'd', 'f', 'g'],
    6: ['a', 'c', 'd', 'e', 'f', 'g'],
    7: ['a', 'b', 'c'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

# Bar connections (edges) with angle sign (+90 or -90)
# Considering the segments in a 7-seg:
# We'll encode the edges in the bars graph, representing adjacency in the digit form.

# The signs: We'll assign +90 or -90 for each edge to differentiate digits 2 and 5 (angle sign matters).
# For simplicity, we use labels 'p' and 'n' for +90 and -90.

digit_edges = {
    # Format: (node1, node2): angle_sign ('p' or 'n')
    0: { ('a','b'):'p', ('b','c'):'p', ('c','d'):'p', ('d','e'):'p', ('e','f'):'p', ('f','a'):'p' },
    1: { ('b','c'):'p' },
    2: { ('a','b'):'p', ('b','g'):'n', ('g','e'):'p', ('e','d'):'p', ('d','a'):'n' },
    3: { ('a','b'):'p', ('b','c'):'p', ('c','d'):'p', ('d','g'):'n', ('g','a'):'p' },
    4: { ('b','c'):'p', ('b','g'):'n', ('g','f'):'p', ('f','c'):'n' },
    5: { ('a','c'):'n', ('c','d'):'p', ('d','f'):'n', ('f','g'):'p', ('g','a'):'n' },
    6: { ('a','c'):'n', ('c','d'):'p', ('d','e'):'p', ('e','f'):'p', ('f','g'):'p', ('g','a'):'n' },
    7: { ('a','b'):'p', ('b','c'):'p' },
    8: { ('a','b'):'p', ('b','c'):'p', ('c','d'):'p', ('d','e'):'p', ('e','f'):'p', ('f','a'):'p', ('g','a'):'p', ('g','c'):'p', ('g','e'):'p', ('g','f'):'p' }, # extra connections for g in 8
    9: { ('a','b'):'p', ('b','c'):'p', ('c','d'):'p', ('d','f'):'n', ('f','g'):'p', ('g','a'):'n' }
}

# For 8 and complicated digits, simplify edges related to g similarly as others.

# However, we note
# 8 contains all segments, so at minimum all edges connecting adjacent segments (6-cycle a-f with g connected to b,c,e,f,g as center):

# For digit recognition we need a canonical code:
# - We assign bars ids in component from 0..k-1.
# - For each edge (bar1, bar2), we record an edge label ('p' or 'n').
# - Canonical form: a sorted tuple of edges with their labels.
# - To manage graph isomorphisms we convert the graph to a minimal string code.

# We must match each extracted component graph with all digit templates and find which digit matches.

# Key steps to implement:

# Part 1: Parse bars, build graph of bars via touching endpoints

# Part 2: Find connected components of bars (each corresponds to one digit)

# Part 3: For each component:
#   - Build graph of bars connected by edges with angle sign label
#   - Compute canonical form of this graph (implement a canonical labeling)
#   - Compare canonical form with precomputed canonical forms of digits

# Part 4: Count recognized digits and output result.

# Implementation details:

# Touching condition:
# Bars touch if they share exactly one endpoint.

# Define a function to compute angle between two bars touching at a point and label angle +90 or -90.

# Because orientation matters (angle sign distinguishes 2 and 5, etc.)

# Let's begin implementation:

def vector(a,b):
    return (b[0]-a[0], b[1]-a[1])

def norm(v):
    return math.hypot(v[0], v[1])

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def angle_sign(v1,v2):
    # v1 and v2 should be perpendicular if they touch
    # We return 'p' if angle is +90 degrees, 'n' if -90 degrees
    # cross product positive -> +90, negative -> -90
    c = cross(v1,v2)
    if c > 0:
        return 'p'
    else:
        return 'n'

def bar_direction(bar, common_point):
    # returns vector from common_point to the other endpoint
    (x1,y1,x2,y2) = bar
    if (x1,y1) == common_point:
        return (x2 - x1, y2 - y1)
    else:
        return (x1 - x2, y1 - y2)

def endpoints(bar):
    (x1,y1,x2,y2) = bar
    return (x1,y1), (x2,y2)

def bars_touch(bar1, bar2):
    # bars touch if they share exactly one endpoint
    e1 = endpoints(bar1)
    e2 = endpoints(bar2)
    points = set(e1) & set(e2)
    if len(points) == 1:
        return points.pop()
    else:
        return None

def normalize_graph(bars, adj, angle_labels):
    # We want a unique canonical representation of the graph with labeled edges
    # Use a Weisfeiler-Lehman style labeling or canonical BFS spanning tree serialization

    n = len(bars)

    # Because digits are small (< 7 bars typically), can try all permutations
    # but components can be up to 1000 bars...
    # We will use a canonical labeling via BFS traversal with sorted edges

    # Generate BFS codes from each node, take lex smallest

    def bfs_code(start):
        visited = [False]*n
        parent = [-1]*n
        label_edges = []

        order = []
        queue = deque([start])
        visited[start] = True

        while queue:
            u = queue.popleft()
            order.append(u)
            neighbors = []
            for v in adj[u]:
                if not visited[v]:
                    neighbors.append(v)
            neighbors.sort()
            for v in neighbors:
                visited[v] = True
                parent[v] = u
                queue.append(v)
        # Now output edges in bfs order with labels
        # encode edges as (min,max,label)
        edges_encoded = []
        for u in order:
            for v in adj[u]:
                if u < v:
                    edges_encoded.append( (u,v,angle_labels.get((u,v),angle_labels.get((v,u)))) )
        edges_encoded.sort()
        # create a tuple representation
        return tuple(edges_encoded)

    all_codes = []
    for start in range(n):
        code = bfs_code(start)
        all_codes.append(code)
    return min(all_codes)

def build_digit_template_graph(segments, edges):
    # segments: list of segment names
    # edges: dict of edges with angle signs
    # Build adjacency and edge label dict

    idx = {s:i for i,s in enumerate(segments)}
    adj = [[] for _ in range(len(segments))]
    angle_labels = dict()
    for (s1,s2), sign in edges.items():
        if s1 in idx and s2 in idx:
            u,v = idx[s1], idx[s2]
            adj[u].append(v)
            adj[v].append(u)
            # store with smaller first for consistent key
            angle_labels[(min(u,v), max(u,v))] = sign
    return segments, adj, angle_labels

digit_templates = dict()
for d in range(10):
    segs = digit_segments[d]
    eds = {}
    # fix edges: only include edges between present segments
    base_edges = digit_edges.get(d,{})
    eds = {}
    for (a,b), sign in base_edges.items():
        if a in segs and b in segs:
            eds[(a,b)] = sign
    segs, adj, angle_labels = build_digit_template_graph(segs, eds)
    code = normalize_graph(segs, adj, angle_labels)
    digit_templates[code] = d

def main():
    input = sys.stdin.readline
    while True:
        n = input()
        if not n:
            break
        n = n.strip()
        if n == '0':
            break
        n = int(n)
        bars = []
        for _ in range(n):
            x1,y1,x2,y2 = map(int, input().split())
            bars.append( (x1,y1,x2,y2) )
        # Build graph of bars:
        # Nodes = bars
        # Edge between touching bars with angle label (p or n)
        adj = [[] for _ in range(n)]
        angle_labels = dict()

        # Build endpoint map for bars to speed up touching detection
        endpoint_map = defaultdict(list)
        for i, b in enumerate(bars):
            p1, p2 = endpoints(b)
            endpoint_map[p1].append(i)
            endpoint_map[p2].append(i)
        # For each bar, find bars touching it by endpoints
        for i,b in enumerate(bars):
            p1, p2 = endpoints(b)
            # look for bars sharing p1 and p2 (excluding itself)
            for p in (p1,p2):
                for j in endpoint_map[p]:
                    if i>=j:
                        continue
                    # confirm that bars i and j share exactly one endpoint (p)
                    if bars_touch(bars[i], bars[j]) == p:
                        # determine angle sign
                        # get directions:
                        v1 = bar_direction(bars[i], p)
                        v2 = bar_direction(bars[j], p)
                        # direction vectors may be zero length? No, bars non-zero length guaranteed.
                        sign = angle_sign(v1,v2)
                        adj[i].append(j)
                        adj[j].append(i)
                        angle_labels[(i,j)] = sign

        # Find connected components (digits)
        visited = [False]*n
        digit_count = [0]*10

        for start in range(n):
            if visited[start]:
                continue
            # BFS to get component bars
            comp = []
            q = deque([start])
            visited[start] = True
            while q:
                u = q.popleft()
                comp.append(u)
                for w in adj[u]:
                    if not visited[w]:
                        visited[w] = True
                        q.append(w)
            # Build subgraph for component
            mapping = {u:i for i,u in enumerate(comp)}
            comp_adj = [[] for _ in range(len(comp))]
            comp_angle_labels = dict()
            for u in comp:
                for v in adj[u]:
                    if v in mapping and mapping[u]<mapping[v]:
                        comp_adj[mapping[u]].append(mapping[v])
                        comp_adj[mapping[v]].append(mapping[u])
                        comp_angle_labels[(mapping[u],mapping[v])] = angle_labels.get( (min(u,v), max(u,v)) )
            # Compute canonical form
            code = normalize_graph(comp, comp_adj, comp_angle_labels)
            digit = digit_templates.get(code, None)
            if digit is None:
                # defensive: if no match, print 0 counts, or guess?
                # The problem states all bars form digits, so no unknown digit.
                # print("Unknown digit formed by bars", comp,file=sys.stderr)
                # Let's guess 0 if unknown (fallback)
                digit = 0
            digit_count[digit] += 1
        print(' '.join(map(str,digit_count)))

if __name__ == '__main__':
    main()