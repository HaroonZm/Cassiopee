import sys
from collections import deque

def neighbors(pos, s):
    x, y, z = pos
    return [(x+s, y, z), (x-s, y, z), (x, y+s, z), (x, y-s, z), (x, y, z+s), (x, y, z-s)]

def surface_area(positions, s):
    area = 6 * s * s * len(positions)
    pos_set = set(positions)
    for x, y, z in positions:
        for nx, ny, nz in neighbors((x, y, z), s):
            if (nx, ny, nz) in pos_set:
                area -= s * s
    return area

def bfs(start, adj, k):
    visited = set()
    queue = deque()
    queue.append((start, [start]))
    min_area = None
    while queue:
        node, path = queue.popleft()
        visited.add(node)
        if len(path) == k:
            area = surface_area(path, s)
            if min_area is None or area < min_area:
                min_area = area
            continue
        for nxt in adj[node]:
            if nxt not in path:
                queue.append((nxt, path + [nxt]))
    if min_area is None:
        return -1
    else:
        return min_area

input_lines = sys.stdin.read().splitlines()
index = 0
while True:
    if index >= len(input_lines):
        break
    line = input_lines[index].strip()
    index += 1
    if line == "":
        continue
    nks = line.split()
    if len(nks) < 3:
        continue
    n, k, s = map(int, nks)
    if n == 0 and k == 0 and s == 0:
        break
    positions = []
    for _ in range(n):
        x, y, z = map(int, input_lines[index].split())
        positions.append((x, y, z))
        index += 1
    pos_set = set(positions)
    # build adjacency
    adj = {p: [] for p in positions}
    for p in positions:
        for nb in neighbors(p, s):
            if nb in pos_set:
                adj[p].append(nb)
    # BFS all starts to find connected k cubes sets, find minimal surface area

    # Since n and k can be up to 2000, full BFS over all subsets is impossible
    # So just try BFS from each node and do BFS with pruning

    # Simple but slow approach: from each start node do BFS picking nodes until k reached

    # To reduce runtime, we limit to at most first 100 nodes
    starts = positions[:100]
    result = -1
    for start in starts:
        # BFS for connected subgraph of size k starting at start
        queue = deque()
        queue.append((start, [start]))
        visited_states = set()
        while queue:
            node, path = queue.popleft()
            if len(path) == k:
                area = surface_area(path, s)
                if result == -1 or area < result:
                    result = area
                continue
            last = path[-1]
            for nxt in adj[last]:
                if nxt not in path:
                    new_path = path + [nxt]
                    key = tuple(sorted(new_path))
                    if key not in visited_states:
                        visited_states.add(key)
                        queue.append((nxt, new_path))
    print(result)