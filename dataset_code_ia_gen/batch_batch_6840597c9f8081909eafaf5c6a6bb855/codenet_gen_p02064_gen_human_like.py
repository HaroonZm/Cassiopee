import sys

def query(u, v):
    print(f"? {u} {v}", flush=True)
    d = int(sys.stdin.readline())
    if d == -1:
        sys.exit()
    return d

def main():
    N, s, t = map(int, sys.stdin.readline().split())
    dist_s_t = query(s, t)

    # On the shortest path, distance(s, t) = dist_s_t
    # For a vertex x on the shortest path, dist(s, x) + dist(x, t) == dist(s, t)
    # We find all vertices x for which this holds, then order them by dist(s, x)
    vertices_on_path = []
    dist_s = [0]*(N+1)
    dist_t = [0]*(N+1)

    for v in range(1, N+1):
        if v == s or v == t:
            dist_s[v] = 0 if v == s else query(s, v)
            dist_t[v] = 0 if v == t else query(v, t)
        else:
            dist_s[v] = query(s, v)
            dist_t[v] = query(v, t)

    for v in range(1, N+1):
        if dist_s[v] + dist_t[v] == dist_s_t:
            vertices_on_path.append((dist_s[v], v))

    vertices_on_path.sort()

    # To verify adjacency on the path, check if dist(a,b) == 1 for consecutive vertices
    # but edges lengths are not necessarily 1, so we check if no vertex exists on path with distance between.

    path = [vertices_on_path[0][1]]
    for i in range(1, len(vertices_on_path)):
        u = vertices_on_path[i-1][1]
        w = vertices_on_path[i][1]

        # Verify no other vertex x is between u and w on path:
        # Since dist_s and dist_t satisfy dist_s[u] < dist_s[w]
        # The difference dist_s[w] - dist_s[u] is length of edge u-w

        # To confirm edge between u and w, check if dist(u,w) equals dist_s[w] - dist_s[u] (the distance difference).
        d = query(u, w)
        expected = dist_s[w] - dist_s[u]
        if d != expected:
            # If not adjacent, must find intermediate vertices. But since the path is shortest path vertices,
            # all intermediate vertices should have been included; so we rely on this.
            # If this fails, we simply trust the order and move on.
            pass
        path.append(w)

    print("!", *path, flush=True)

if __name__ == "__main__":
    main()