import sys
sys.setrecursionlimit(10**7)

def canonical_path(path):
    revpath = path[::-1]
    return path if path < revpath else revpath

def dfs(u, used, length, path):
    global max_length, ans_path
    if length > max_length or (length == max_length and canonical_path(path) < ans_path):
        max_length = length
        ans_path = canonical_path(path)
    for i, (v, w) in enumerate(graph[u]):
        if not used[i]:
            used[i] = True
            dfs(v, used, length + w, path + [v])
            used[i] = False

while True:
    line = ''
    while line.strip() == '':
        line = sys.stdin.readline()
        if line == '':
            exit()
    ns, nl = map(int, line.strip().split())
    if ns == 0 and nl == 0:
        break
    edges = []
    graph = [[] for _ in range(ns+1)]
    for _ in range(nl):
        while True:
            line = sys.stdin.readline()
            if line.strip() != '':
                break
        s1, s2, d = map(int,line.strip().split())
        edges.append((s1,s2,d))
        # Will assign edge indices later
    # Assign edges indexed in graph[u] as (v, w), but we need per-edge usage in dfs
    # To mark usage per edge, we store edges in order and for each edge add twice (u->v and v->u)
    # We need same index in 'used' for both directions to avoid using edge twice.
    # So we build a new adjacency "edge lists" with edge index for usage, symmetrical.
    edge_list = []
    graph = [[] for _ in range(ns+1)]
    for i,(a,b,d) in enumerate(edges):
        graph[a].append( (b,d,i) )
        graph[b].append( (a,d,i) )
    max_length = -1
    ans_path = [10**9]*(nl*10)
    used = [False]*nl

    for start in range(1, ns+1):
        dfs_stack = []

        def dfs(u, used, length, path):
            global max_length, ans_path
            if length > max_length or (length == max_length and canonical_path(path) < ans_path):
                max_length = length
                ans_path = canonical_path(path)
            for v,w,eid in graph[u]:
                if not used[eid]:
                    used[eid] = True
                    dfs(v, used, length + w, path + [v])
                    used[eid] = False

        dfs(start, used, 0, [start])

    print(max_length)
    print(' '.join(map(str, ans_path)) )