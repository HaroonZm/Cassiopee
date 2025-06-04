import math
import sys

def dist(c1, c2):
    x1, y1, z1, r1 = c1
    x2, y2, z2, r2 = c2
    center_dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    gap = center_dist - (r1 + r2)
    return max(0.0, gap)

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, rank, x, y):
    rx = find(parent, x)
    ry = find(parent, y)
    if rx != ry:
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    return False

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
        cells = []
        for _ in range(n):
            x, y, z, r = map(float, input_lines[idx].split())
            idx += 1
            cells.append((x, y, z, r))

        edges = []
        # Build edges: cost is distance between spheres surfaces or 0 if touching/overlapping
        for i in range(n):
            for j in range(i+1, n):
                d = dist(cells[i], cells[j])
                edges.append((d, i, j))

        # Kruskal's MST algorithm
        edges.sort(key=lambda x: x[0])
        parent = list(range(n))
        rank = [0]*n

        total_length = 0.0
        for length, a, b in edges:
            if union(parent, rank, a, b):
                total_length += length

        print(f"{total_length:.3f}")

if __name__ == "__main__":
    main()