def main():
    import sys
    sys.setrecursionlimit(10**7)

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u = find(u)
        v = find(v)
        if u != v:
            parent[v] = u
            return True
        return False


    lines = sys.stdin.read().strip('\n ').split('\n')
    idx = 0
    while True:
        if idx >= len(lines):
            break
        s,d = map(int, lines[idx].split())
        idx += 1
        if s == 0 and d == 0:
            break

        # node indexing:
        # hot springs: 0 to s-1
        # districts: s to s+d-1

        edges = []
        # read s lines: distances between each hot spring and each district
        for h in range(s):
            dist_line = list(map(int, lines[idx].split()))
            idx += 1
            for di, dist in enumerate(dist_line):
                if dist != 0:
                    edges.append((dist, h, s + di))
        # read d-1 lines: distances between districts
        for i in range(d - 1):
            dist_line = list(map(int, lines[idx].split()))
            idx += 1
            for j, dist in enumerate(dist_line):
                if dist != 0:
                    # between district j and district i + 1 + j
                    u = s + j
                    v = s + i + 1 + j
                    edges.append((dist, u, v))

        edges.sort(key=lambda x: x[0])
        parent = list(range(s + d))
        total = 0
        count = 0
        for dist,u,v in edges:
            if union(u,v):
                total += dist
                count += 1
                if count == s + d -1:
                    break
        print(total)


if __name__ == "__main__":
    main()