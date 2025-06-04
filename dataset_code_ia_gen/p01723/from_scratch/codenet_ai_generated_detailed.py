import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

def modinv(x, mod=MOD):
    # Fermat's little theorem for modular inverse
    return pow(x, mod - 2, mod)

def precompute_factorials(n, mod=MOD):
    # Precompute factorials and inverses for n choose k calculations
    fact = [1] * (n + 1)
    invfact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    invfact[n] = modinv(fact[n], mod)
    for i in range(n - 1, 0, -1):
        invfact[i] = invfact[i + 1] * (i + 1) % mod
    return fact, invfact

def comb(n, r, fact, invfact, mod=MOD):
    # Compute nCr modulo mod
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % mod * invfact[n - r] % mod

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    edges = [[] for _ in range(N)]
    indegree = [0] * N

    # Read comparisons:
    # Ai is taller than Bi => edge from Ai to Bi, Ai > Bi
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edges[a].append(b)
        indegree[b] += 1

    # The problem gives a partial order of tower heights with edges a->b meaning tower a > tower b.

    # Our task: 
    # Count the number of possible correct tables T, i.e. number of ways to assign tower heights obeying the partial order
    # and rules from description, modulo 10^9+7.

    # The height relations satisfy:
    # - For compared pairs: strictly greater.
    # - For others not compared directly, heights can be equal or differing; equal heights allowed except for pairs compared (must be strictly different).

    # We want to count the number of consistent T, i.e. possible height assignments producing matrices T consistent with given comparison results.

    # Key insight:
    # This reduces to counting the number of ways to "linearly order" the towers with possible ties allowed,
    # consistent with the partial order given by comparisons (edges).

    # The partial order graph has no cycles (guaranteed no contradictions).
    # Each tower compares with any tower larger than itself at most once.

    # We want to count the number of "weak orders" compatible with the partial order.
    # Weak orders allow ties between incomparable elements.

    # Each weak order corresponds to a way to merge chains of comparably ordered elements, grouping incomparable nodes into levels.

    # The given partial order induces a Directed Acyclic Graph (DAG).
    # Number of possible correct tables equals number of ways to arrange nodes into levels obeying edges u>v => level(u) < level(v).
    # Heights assigned corresponds to layers (levels) of nodes.

    # The problem can be solved by counting the number of ways to linearly order the DAG with possible ties,
    # respecting edges direction, and counting how groups can be formed.

    # Approach:
    # Decompose the DAG into its connected components.
    # Then count ways per strongly connected component (which are trivial here because graph is DAG).
    # Then count ways by DP combining children counts.

    # Since graph is DAG (no cycles), we can model it as a tree by choosing roots.

    # However graph is general DAG, not necessarily tree.

    # Trick here is the problem's key:
    # Each tower is compared greater than a tower at most once, i.e. each node has at most one outgoing edge to a node which is greater.

    # Actually, "each tower is compared to towers taller than itself at most once"
    # So, for each tower, edges from it to towers lower than itself are at most once per tower.
    # This implies partial order is a forest of rooted trees directed from root (tallest) down to smaller towers.

    # Because N-1 edges exist, and no contradictions, the graph is a forest of rooted trees.

    # This allows us to treat the DAG as a forest of rooted trees.

    # We want to count the number of possible total orders consistent with given partial order, allowing ties.

    # The key to solving:
    # The number of ways to merge subtrees is given by multinomial coefficients.

    # Define DP(u):
    # returns (size_u, ways_u)
    # size_u: number of nodes in subtree rooted at u
    # ways_u: number of ways to assign heights consistent with partial order in subtree u.

    # For a tree node u with children c1, c2,... ck:
    # The towers in subtrees are incomparable to each other, thus the ways to assign heights:
    # You can assign equal heights to nodes if no restriction (but children subtrees are connected by a strict inequality to u)
    # The root is always strictly taller than its children.
    # Children subtrees are incomparable with each other; so, their nodes can be tied or ordered arbitrarily respecting their own partial orders.

    # Actually, edges are from tower a to b meaning a > b, so in tree parents are taller than children who are smaller.

    # So heights must satisfy: height(u) > height(v) for each edge u->v, so no tie between parent and child.

    # Children subtrees are incomparable to each other; their relative ordering can have ties arbitrarily.

    # So total ways to combine child subtrees:
    # We have the sizes s1, s2,... sk and number of ways w1, w2,... wk.
    # The ways to interleave these child subtrees with ties allowed are given by the "ordered Bell numbers" or via multinomial:

    # The order among children subtrees is arbitrary and can have equal heights (ties), since no constraints between children.

    # Number of ways to merge k subtrees each with sizes si is the multinomial coefficient:
    # ways_children = multinomial(s1, s2, ..., sk)
    # and multiply by product of ways_i for each subtree.

    # We sum up:
    # size_u = 1 + sum of sizes of children
    # ways_u = (product of ways_i) * comb(total_children_size, s1,...,sk)

    # The multinomial coefficient counts the number of ways to interleave layers of children subtrees respecting that nodes in different children can have ties.

    # Wait, need to be careful: parent must be at strictly greater height (height level strictly less since height levels are like ranks).

    # So height assignments: parent height > children heights (strict), but children can be on the same height level or different levels among themselves.

    # So children can be tied or ordered arbitrarily.

    # Therefore, ways to combine child subtrees is simplex:
    # Number of ways = product of ways_i * combination_of_positions_of_children.

    # Since nodes inside each subtree have their ordering already counted in ways_i, now we count ways to merge subtrees with possible ties among them.

    # This merging corresponds to counting the weak orders of the children subtrees.

    # The number ways to order multiple multisets with possible ties equals the multinomial coefficient.

    # But careful: since children subtrees are disjoint sets of nodes and incomparable with each other: their nodes can be arranged with possible ties arbitrarily.

    # Total arrangements of children nodes types while preserving subtree orders and allowing ties between nodes of different children are counted by multinomial coefficients.

    # The formula is the multinomial coefficient for distributing the children nodes into layers combined with ways_i.

    # Thus we can model ways_u as:
    # ways_u = (multinomial coefficient of child subtree sizes) * product of ways_i

    # We precompute factorials for multinomial coefficients.

    # Finally, the graph might be a forest.
    # To get the total ways, we multiply the ways of each tree.

    # Identify roots (nodes with indegree = 0) and run DP from each.

    fact, invfact = precompute_factorials(N)

    def multinomial(sizes):
        # Compute multinomial coefficient for sizes
        total = sum(sizes)
        res = fact[total]
        for sz in sizes:
            res = (res * invfact[sz]) % MOD
        return res

    visited = [False]*N

    def dfs(u):
        # DP on trees to get (size, ways)
        visited[u] = True
        sizes = []
        ways_list = []
        for v in edges[u]:
            if not visited[v]:
                sz, ways = dfs(v)
                sizes.append(sz)
                ways_list.append(ways)
        size_u = 1 + sum(sizes)
        # ways to combine children subtrees
        ways_children = multinomial(sizes)
        for w in ways_list:
            ways_children = (ways_children * w) % MOD
        return size_u, ways_children

    roots = [i for i in range(N) if indegree[i] == 0]

    total_ways = 1
    for r in roots:
        if not visited[r]:
            sz, ways = dfs(r)
            total_ways = (total_ways * ways) % MOD

    print(total_ways)

if __name__ == "__main__":
    main()