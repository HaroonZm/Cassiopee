import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 9

N, M = map(int, input().split())
parent = list(range(3*N))
size = [1]*(3*N)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        if size[a]<size[b]:
            a,b = b,a
        parent[b] = a
        size[a] += size[b]

good_rel = []
bad_rel = []

for _ in range(M):
    A,B,C = map(int,input().split())
    A -= 1
    B -= 1
    if C == 0:
        union(A,B)
    else:
        bad_rel.append((A,B))

# After union-find, check for contradictions:
# Bad relation pair in same good group => no solution
for A,B in bad_rel:
    if find(A) == find(B):
        print(0)
        exit()

# Now compress union-find groups to indices
group_map = {}
idx = 0
for i in range(3*N):
    r = find(i)
    if r not in group_map:
        group_map[r] = idx
        idx += 1

G = idx  # number of groups (super-nodes)
# Build graph for bad relations between groups, the graph must be 3-colorable (teams of size 3)

adj = [[] for _ in range(G)]
for A,B in bad_rel:
    u = group_map[find(A)]
    v = group_map[find(B)]
    adj[u].append(v)
    adj[v].append(u)

# Check connected components and bipartiteness (3-colorability condition)
# Actually, the problem can be reduced to checking if the graph is 3-colorable without any contradictory edges.
# But note that since all good relations merge sets, and bad relations imply those sets cannot be on same team.
# Total of 3N students, the sets correspond to supernodes, each set size s.

# The problem is equivalent to counting the number of ways to partition the supernodes into teams of size 3,
# respecting that sets with bad relation cannot be in the same team.

# Since the problem is from ICPC Team section and M<=18, we have at most 36 supernodes (in worst cases).
# But with N up to 10^6, but complexity depends on M, so we can do a backtracking on the supernodes.

# However, since M<=18 and supernodes correspond to union-find sets formed by good relations,
# the number of supernodes G <= 3N but actually at most 3N - number of unions.

# The main constraint is team size: teams contain exactly 3 students.
# sum of sizes of supernodes = 3N
# We have to partition supernodes into triplets respecting bad relations.

# The problem becomes: how many ways to partition nodes into triplets (each triplet is a team),
# such that no edge of bad relation is inside a triplet.

# Since M is small => at most 18 edges, beyond that no edges.
# So we try all possible groupings.

# Represent supernodes by their sizes.
supernode_sizes = [0]*G
for i in range(3*N):
    r = find(i)
    supernode_sizes[group_map[r]] += 1

# If any supernode size > 3, no solution since they must be in one team (good relation)
for s in supernode_sizes:
    if s > 3:
        print(0)
        exit()

# If some supernode size == 3, it's a full team alone - can be assigned only one way
# If size == 1 or 2, must be matched with others to form teams of size 3

# Let's generate all subsets of supernodes of size 1 or 2 or 3 with total size 3,
# and check if any bad relation edge is inside the subset (the subset is a candidate team).

from collections import defaultdict

# Build adjacency matrix for bad relations for quick check
bad_set = [set() for _ in range(G)]
for u in range(G):
    for v in adj[u]:
        bad_set[u].add(v)

# Precompute all subsets that can form a team
team_candidates = []

# Since G can be large, but number of supernodes with size <3 can be less,
# to reduce complexity, note that sizes can be either 1,2 or 3.
# Supernodes with size = 3 are forced teams.

ones = [i for i,s in enumerate(supernode_sizes) if s==1]
twos = [i for i,s in enumerate(supernode_sizes) if s==2]
threes = [i for i,s in enumerate(supernode_sizes) if s==3]

# Each three-sized supernode forms a team alone, M_fixed = number of these teams
M_fixed = len(threes)

# Remove threes from pool
pool = [i for i in range(G) if supernode_sizes[i]<3]

# We'll process subsets of pool to build teams of size 3 by summing supernode_sizes

# Create bitmask to index IDs of pool
id_map = {v:i for i,v in enumerate(pool)}
P = len(pool)

# bad edges inside pool:
bad_mask = [0]*P
for u in pool:
    bu = 0
    for w in bad_set[u]:
        if w in id_map:
            bu |= 1 << id_map[w]
    bad_mask[id_map[u]] = bu

# Precompute subsets with sum=3 and no internal bad edge
valid_teams = []

# Because P can be large (up to ~3N), brute force all subsets impossible
# But M<=18 and thus number of edges small; so meaningful number of supernodes can be up to M+number_of_groups formed by good relation?

# However, problem constraints: M<=18, N up to 10^6
# The union-find merges students with good relations, so total supernodes after union-find <= 3N
# with maximum M=18 edges => maximum supernodes ~ 3N - (number of union operations) at least 0
# But input size huge so DP on all supernodes impossible.

# So the trick is that each supernode size<=3 and sum supernode_sizes=3N

# Since bad edges only exist between M pairs, we have a graph with M edges on supernodes.

# Since M is small, the supernodes form a graph with small edges,
# the number of connected components C in this graph is at least G - M (since some pairs connected by edges).

# The problem reduces to solve in each connected component independently, product of answer of components.

# So first find connected components:

visited = [False]*G
components = []

def dfs_cc(u, comp):
    visited[u] = True
    comp.append(u)
    for w in adj[u]:
        if not visited[w]:
            dfs_cc(w, comp)

for i in range(G):
    if not visited[i]:
        comp = []
        dfs_cc(i, comp)
        components.append(comp)

# For each component, consider only the nodes and edges inside it.
# The combination of components is independent (teams only mix within components).

# The total number of teams = N
# teams formed by threes are fixed
# For each component sum of sizes = S
# Number of teams = S//3

# For component containing some supernodes of size 3, those form mandatory teams; remove them.

# For component DP:
# Let nodes in component with indices in comp, we map their global indices to local.

def component_solve(comp):
    # sizes and edges
    comp_size = len(comp)
    local_id = {v:i for i,v in enumerate(comp)}
    sizes = [supernode_sizes[v] for v in comp]

    # Count fixed teams in this component (supernodes size 3)
    fixed_count = sum(1 for s in sizes if s==3)
    # Remove these nodes from graph since they form their own team
    # Remaining nodes with size 1 or 2 must be combined into teams of size 3

    nodes = [i for i,s in enumerate(sizes) if s<3]
    if not nodes:
        # all nodes size 3 => unique assignment
        return 1

    # Build adjacency matrix for nodes with size <3
    size_nodes = len(nodes)

    # Build conflict graph among nodes, edges = bad edges
    bad_adj = [0]*size_nodes
    # map back to global id
    node_to_global = [comp[i] for i in nodes]
    for i,u in enumerate(node_to_global):
        for w in adj[u]:
            if w in comp:
                j = local_id[w]
                if sizes[j]<3:
                    if j in nodes:
                        k = nodes.index(j)
                        bad_adj[i] |= 1 << k

    # Each node has size = 1 or 2
    # We must partition nodes into teams of sum size=3, with no bad edge inside team

    # We use bitmask dp: dp[mask] = number of ways to partition nodes in mask

    from functools import lru_cache

    total_mask = (1<<size_nodes)-1

    @lru_cache(None)
    def dp(mask):
        if mask == 0:
            return 1
        res = 0
        # choose first node in mask
        first = (mask & -mask).bit_length() - 1
        s_first = sizes[nodes[first]]

        # team size must be 3
        # try to form team with first alone if size 3, but first size<3 so no
        # try to pair with one or two others to form 3
        # try adding one other node
        for snd in range(first+1,size_nodes):
            if (mask & (1<<snd))==0:
                continue
            s_sum = s_first + sizes[nodes[snd]]
            if s_sum > 3:
                continue
            # check bad edges in team with first and snd
            if (bad_adj[first] & (1 << snd)) != 0:
                continue
            # If sum == 3, this subset is a team
            if s_sum == 3:
                new_mask = mask & ~(1<<first) & ~(1<<snd)
                res += dp(new_mask)
                res %= MOD
            else:
                # sum ==1+2=3 or 2+1=3 means need one more node
                for trd in range(snd+1,size_nodes):
                    if (mask & (1<<trd))==0:
                        continue
                    s_tot = s_sum + sizes[nodes[trd]]
                    if s_tot != 3:
                        continue
                    # check no bad edges inside triple
                    if (bad_adj[first] & (1<<trd)) != 0:
                        continue
                    if (bad_adj[snd] & (1<<trd)) != 0:
                        continue
                    new_mask = mask & ~(1<<first) & ~(1<<snd) & ~(1<<trd)
                    res += dp(new_mask)
                    res %= MOD
        return res % MOD

    # we cannot use team of single node since size <3 and no other nodes to add (meaning no packing)
    # if there's no way to form teams of total size 3 from nodes, dp will return 0

    return dp(total_mask)%MOD

ans = 1
for comp in components:
    ans = (ans * component_solve(comp)) % MOD

# Teams with size 3 supernodes are counted uniquely, so multiply by 1 anyway
print(ans % MOD)