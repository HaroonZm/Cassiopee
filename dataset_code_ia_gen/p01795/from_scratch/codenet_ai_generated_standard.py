import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 9

N, M = map(int, sys.stdin.readline().split())
parent = list(range(3 * N))
size = [1] * (3 * N)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

good_edges = []
bad_edges = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    A -= 1
    B -= 1
    if C == 0:
        union(A, B)
    else:
        bad_edges.append((A, B))

comp_map = {}
idx = 0
comp_nodes = {}
for i in range(3 * N):
    r = find(i)
    if r not in comp_map:
        comp_map[r] = idx
        comp_nodes[idx] = []
        idx += 1
    comp_nodes[comp_map[r]].append(i)

# Check size constraints
for c in comp_nodes.values():
    if len(c) > 3:
        print(0)
        exit()

# Build bad relations graph on components
bad_graph = {}
for c in comp_map.values():
    bad_graph[c] = set()
for A, B in bad_edges:
    cA = comp_map[find(A)]
    cB = comp_map[find(B)]
    if cA == cB:
        # Bad relation inside same component => no solution
        print(0)
        exit()
    bad_graph[cA].add(cB)
    bad_graph[cB].add(cA)

# Components are groups of students connected by good relations
# Each group size is 1 to 3.
# We must assign them into teams of size 3 with no bad edges inside a team.
# Since each team size is 3, we basically must partition components into triples summing size 3,
# no bad edges inside one triple (clique forbidden edges)
# The problem reduces to count matchings of groups into teams of sum 3 sizes with constraints.

# Because M <= 18, let's construct a constraint graph on components (number <= M+1) max <= 19 
n = len(comp_nodes)
sizes = [len(comp_nodes[i]) for i in range(n)]

# Check total sum sizes == 3N
if sum(sizes) != 3 * N:
    print(0)
    exit()

# Adjacency matrix for bad edges between components
adj = [0]*n
for i in range(n):
    for j in bad_graph[i]:
        adj[i] |= (1 << j)

# We want to count number of ways to partition components into groups of size with sum sizes==3
# with no bad edges inside the group (i.e., no edges in adj between group members)

# Precompute all valid subsets representing possible teams
valid_teams = []

for mask in range(1, 1 << n):
    # Check if group sum size == 3
    s = 0
    ok = True
    members = []
    for i in range(n):
        if mask & (1 << i):
            s += sizes[i]
            members.append(i)
            if s > 3:
                ok = False
                break
    if not ok or s != 3:
        continue
    # Check no bad edges inside group: for each member i check that adj[i] & mask == 0 except i
    for i in members:
        if (adj[i] & mask) != 0:
            ok = False
            break
    if ok:
        valid_teams.append(mask)

# Use DP to count partitions of [0..n-1] into subsets in valid_teams covering all elements
dp = [0] * (1 << n)
dp[0] = 1
for used in range(1 << n):
    if dp[used] == 0:
        continue
    rest = ((1 << n) - 1) ^ used
    # For each valid team that is subset of rest
    for team in valid_teams:
        if (team & rest) == team:
            dp[used | team] = (dp[used | team] + dp[used]) % MOD

print(dp[(1 << n) - 1])