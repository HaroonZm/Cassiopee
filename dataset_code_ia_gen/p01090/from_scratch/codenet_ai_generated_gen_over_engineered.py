class IslandCity:
    def __init__(self, n, proposals, k):
        self.n = n
        self.proposals = proposals  # List of EdgeProposal
        self.k = k  # Exact number of company A edges to choose

    def minimum_cost_plan(self):
        # We want to select exactly k edges from company A and n-1-k from company B
        # Then these selected edges should form a spanning tree (connect all islands)
        # We need the minimum cost sum under these constraints

        # We'll build an abstraction of a constrained MST solver

        # First, separate edges by company
        edges_A = [e for e in self.proposals if e.company == 'A']
        edges_B = [e for e in self.proposals if e.company == 'B']

        # Sort edges by cost ascending, this helps to try smaller costs first
        edges_A.sort(key=lambda e: e.cost)
        edges_B.sort(key=lambda e: e.cost)

        from math import inf

        # To solve this complicated constrained MST, we can try dynamic programming
        # based on the number of company A edges chosen so far and the connectivity state

        # Number of nodes: n
        # We want to pick exactly n-1 edges

        # However, to keep track of components efficiently and ensure a valid spanning tree,
        # we will use a clever approach:
        # Since n is up to 200, m up to 600, and k up to n - 1,
        # trying all subsets is impossible.
        #
        # Another idea: iterate over all subsets of edges with exactly n-1 edges with k edges from A,
        # but that is also impossible.
        #
        # Alternative approach: We use a parametric search via minimum spanning trees:
        # We'll add a parameter to edge costs that penalizes or rewards choosing company A edges,
        # then binary search the parameter value so that the MST has exactly k edges of company A.
        #
        # The problem: But the output cost must be the sum of real costs, no penalties.
        #
        # So, we can find MSTs with exactly k edges from company A by parametric search:
        # Define a cost function: cost' = cost + lambda if A else cost
        # For a given lambda, build MST minimizing sum cost'
        # Count how many edges of company A in MST
        # By adjusting lambda we force the MST to have the number of A edges that we want

        # We'll implement this parametric search approach.
        # Worst case will be feasible for n=200, m=600.

        def mst_with_lambda(lambda_):
            # Build a list of edges with modified cost = cost + (lambda if company A else 0)
            mod_edges = []
            for e in self.proposals:
                mod_cost = e.cost + (lambda_ if e.company == 'A' else 0)
                mod_edges.append(Edge(e.u, e.v, e.cost, e.company, mod_cost))
            # Kruskal MST
            uf = UnionFind(self.n)
            mod_edges.sort(key=lambda e: e.mod_cost)
            total_cost = 0
            company_A_count = 0
            edges_used = 0
            for e in mod_edges:
                if uf.union(e.u, e.v):
                    total_cost += e.cost  # original cost, not mod_cost
                    if e.company == 'A':
                        company_A_count += 1
                    edges_used += 1
                    if edges_used == self.n - 1:
                        break
            if edges_used < self.n - 1:
                # Not connected MST
                return None, None
            return company_A_count, total_cost

        # Binary search on lambda range
        left = -10000  # sufficiently negative
        right = 10000  # sufficiently positive
        answer = -1

        # Invariant: the number of company A edges in MST is nondecreasing as lambda increases
        # because higher lambda raises cost of using company A edges, so MST uses fewer A edges

        for _ in range(100):
            mid = (left + right) / 2
            count_A, cost = mst_with_lambda(mid)
            if count_A is None:
                # Not connected, try to relax to find some solution
                left = mid
                continue
            if count_A < self.k:
                # We want more company A edges, so lower lambda to make A cheaper
                right = mid
            else:
                # count_A >= k, we want exactly k, so try to increase lambda to reduce A edges
                left = mid
            # Track answer if we get exactly k edges
            if count_A == self.k:
                if answer == -1 or cost < answer:
                    answer = cost

        return answer


class EdgeProposal:
    __slots__ = ('u', 'v', 'cost', 'company')

    def __init__(self, u, v, cost, company):
        self.u = u - 1  # zero-based internally
        self.v = v - 1
        self.cost = cost
        self.company = company

    def __repr__(self):
        return f"EdgeProposal({self.u},{self.v},{self.cost},{self.company})"


class Edge:
    __slots__ = ('u', 'v', 'cost', 'company', 'mod_cost')

    def __init__(self, u, v, cost, company, mod_cost):
        self.u = u
        self.v = v
        self.cost = cost
        self.company = company
        self.mod_cost = mod_cost


class UnionFind:
    __slots__ = ('parent', 'rank')

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1
        return True


def main():
    import sys

    lines = iter(sys.stdin.read().splitlines())
    while True:
        try:
            nmk_line = next(lines)
        except StopIteration:
            break
        if not nmk_line.strip():
            continue
        n, m, k = map(int, nmk_line.strip().split())
        if n == 0 and m == 0 and k == 0:
            break
        proposals = []
        for _ in range(m):
            parts = next(lines).split()
            u, v = int(parts[0]), int(parts[1])
            w = int(parts[2])
            l = parts[3]
            proposals.append(EdgeProposal(u, v, w, l))
        city = IslandCity(n, proposals, k)
        res = city.minimum_cost_plan()
        print(res if res is not None else -1)


if __name__ == '__main__':
    main()