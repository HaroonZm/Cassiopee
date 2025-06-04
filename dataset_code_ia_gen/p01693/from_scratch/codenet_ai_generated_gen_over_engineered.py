class DerangementTransformer:
    class Permutation:
        def __init__(self, elements):
            self.elements = elements
            self.size = len(elements)

        def is_derangement(self):
            return all(self.elements[i] != i + 1 for i in range(self.size))

        def fixed_points(self):
            return [i for i in range(self.size) if self.elements[i] == i + 1]

        def clone(self):
            return DerangementTransformer.Permutation(self.elements[:])

        def apply_swap(self, i, j):
            self.elements[i], self.elements[j] = self.elements[j], self.elements[i]

        def __getitem__(self, index):
            return self.elements[index]

        def __setitem__(self, index, value):
            self.elements[index] = value

    class SwapOperation:
        def __init__(self, i, j, permutation):
            self.i = i
            self.j = j
            self.permutation = permutation

        def cost(self):
            # cost = (p_i + p_j) * |i - j|
            return (self.permutation[self.i] + self.permutation[self.j]) * abs(self.i - self.j)

        def apply(self):
            self.permutation.apply_swap(self.i, self.j)

    class DerangementSolver:
        def __init__(self, permutation):
            self.permutation = permutation

        def solve(self):
            # If already derangement
            if self.permutation.is_derangement():
                return 0

            # Fixed points indices
            fixed = self.permutation.fixed_points()
            n = self.permutation.size

            # Build a graph where nodes are indices, edges represent possible swaps to fix fixed points.
            # We'll construct a weighted graph for minimum weight perfect matching.

            # We want to find pairs of indices to swap to remove all fixed points, minimizing total cost.

            # Strategy:
            # - The minimal set of swaps that ensure no fixed points remain.
            # - Note: After removing fixed points by swaps, no element equals its index+1.
            # - Since swapping non-fixed points might increase cost unnecessarily, we focus on fixed points.
            #
            # We'll form a graph with vertices = fixed points + possibly others to break cycles efficiently.
            # But problem is complex. Instead, note that a derangement is a permutation without fixed points.
            #
            # Let's use a weighted graph with vertices = all elements.
            # Edges represent possible swaps between any two positions.
            #
            # We'll interpret the problem as:
            # Find a permutation q reachable by swaps from p s.t. q is derangement and cost minimal.
            #
            # Because swaps are reversible and cost defined, and swap cost depends on p_i and p_j and distance,
            # an optimal solution can be constructed by carefully analyzing fixed points.
            #
            # Because of complexity, we try a reduction:
            #
            # - Any fixed point must move to a different position.
            # - Swapping two fixed points fixes both if after swapping neither position has element == index+1.
            #
            # We must find minimal cost matching on fixed points to avoid fixed points.
            #
            # The problem reduces to finding a minimum weight perfect matching in a graph with nodes = fixed points,
            # edges = swap cost between those points if swapping breaks the fixed points.
            #
            # But sometimes swapping between fixed and non-fixed points or cycles may be needed.
            #
            # To keep solution general and extensible, let's build a graph of fixed points and attempt minimum weight perfect matching.
            #
            # We'll use the standard Hungarian algorithm.

            # First, collect all indices involved in fixed points
            fixed_points = self.permutation.fixed_points()
            if not fixed_points:
                return 0

            # Sometimes number of fixed points is odd: 
            # We can add a dummy node to make the number even, representing a swap with a non-fixed point.

            # Build cost matrix for fixed points

            import math

            m = len(fixed_points)
            # We create a cost matrix for matching:
            # cost[i][j] = cost of swapping fixed_points[i] and fixed_points[j] if it breaks fixed points at both positions.
            # If not feasible, cost is large.
            # We want to find minimum cost perfect matching on this matrix.

            # Define a helper to check if swapping i and j breaks fixed points
            def swap_breaks_fixed(pi, pj):
                # After swapping elements at pi and pj,
                # check if position pi and pj still are fixed points?
                val_i = self.permutation[pi]
                val_j = self.permutation[pj]
                # after swap: position pi has val_j, position pj has val_i
                # fixed point if element == position +1
                fixed_i = (val_j == pi + 1)
                fixed_j = (val_i == pj + 1)
                return (not fixed_i) and (not fixed_j)

            # Add pseudo fixed point (dummy) to fix odd number of fixed points
            # When number is odd, add one dummy that costs 0 if removing fixed point by swapping with non-fixed point.

            # The general approach:
            # - If number of fixed points is even:
            #   Compute min weight perfect matching on fixed points graph.
            # - If odd:
            #   Add dummy node with edges representing swapping with some non-fixed point that fixes the point.

            # Precompute swap costs between fixed points
            INF = 10**9
            # We'll create a cost matrix for even number of nodes
            # If odd, increment size and add dummy node.

            # Find candidates for dummy node edges (non-fixed points)
            non_fixed_points = [i for i in range(n) if i not in fixed_points]

            # We will build an extended matrix

            size = m
            dummy_added = False
            if m % 2 == 1:
                dummy_added = True
                size = m + 1

            cost = [[INF] * size for _ in range(size)]

            # Fill base matrix for fixed points
            for i in range(m):
                for j in range(i + 1, m):
                    pi = fixed_points[i]
                    pj = fixed_points[j]
                    if swap_breaks_fixed(pi, pj):
                        c = (self.permutation[pi] + self.permutation[pj]) * abs(pi - pj)
                        cost[i][j] = c
                        cost[j][i] = c

            # If odd, add dummy node edges
            if dummy_added:
                # dummy node index = m
                dummy = m
                # For each fixed point i, we can pair with a non-fixed point k so that swapping i,k breaks i's fixed point
                # so cost[i][dummy] = minimal cost among such swaps
                for i in range(m):
                    pi = fixed_points[i]
                    val_i = self.permutation[pi]
                    mincost = INF
                    for k in non_fixed_points:
                        val_k = self.permutation[k]
                        # after swap, position pi has val_k
                        # check if fixed point at pi removed?
                        if val_k != pi + 1:
                            # swap cost
                            c = (val_i + val_k) * abs(pi - k)
                            if c < mincost:
                                mincost = c
                    cost[i][dummy] = mincost
                    cost[dummy][i] = mincost
                cost[dummy][dummy] = INF

            # Hungarian algorithm for minimum weight perfect matching

            class Hungarian:
                def __init__(self, cost_matrix):
                    self.n = len(cost_matrix)
                    self.cost = cost_matrix
                    self.max_value = max(max(row) for row in cost_matrix if row) if cost_matrix else 0
                    self.u = [0]*(self.n+1)
                    self.v = [0]*(self.n+1)
                    self.p = [0]*(self.n+1)
                    self.way = [0]*(self.n+1)

                def solve(self):
                    INF = 10**9
                    n = self.n
                    for i in range(1, n+1):
                        self.p[0] = i
                        j0 = 0
                        minv = [INF]*(n+1)
                        used = [False]*(n+1)
                        while True:
                            used[j0] = True
                            i0 = self.p[j0]
                            j1 = 0
                            delta = INF
                            for j in range(1, n+1):
                                if not used[j]:
                                    cur = self.cost[i0-1][j-1] - self.u[i0] - self.v[j]
                                    if cur < minv[j]:
                                        minv[j] = cur
                                        self.way[j] = j0
                                    if minv[j] < delta:
                                        delta = minv[j]
                                        j1 = j
                            for j in range(n+1):
                                if used[j]:
                                    self.u[self.p[j]] += delta
                                    self.v[j] -= delta
                                else:
                                    minv[j] -= delta
                            j0 = j1
                            if self.p[j0] == 0:
                                break
                        # augmenting path
                        while True:
                            j1 = self.way[j0]
                            self.p[j0] = self.p[j1]
                            j0 = j1
                            if j0 == 0:
                                break
                    # answer is -v[0]
                    ans = -self.v[0]
                    match = [-1]*n
                    for j in range(1, n+1):
                        if self.p[j] > 0 and self.p[j]-1 < n and j-1 < n:
                            match[self.p[j]-1] = j-1
                    return ans, match

            hungarian = Hungarian(cost)
            minimal_cost, matching = hungarian.solve()

            # minimal_cost can be INF if no feasible solution.
            if minimal_cost >= INF:
                # No way to fix all fixed points by swapping pairs?
                # Then fix all fixed points individually by swapping with non-fixed points (if possible)
                total_cost = 0
                # For each fixed point, find minimal cost swap with a non-fixed point that breaks fixed point
                for pi in fixed_points:
                    val_i = self.permutation[pi]
                    best = INF
                    for k in non_fixed_points:
                        val_k = self.permutation[k]
                        if val_k != pi + 1:
                            c = (val_i + val_k) * abs(pi - k)
                            if c < best:
                                best = c
                    if best == INF:
                        # Not fixable, problem constraints might guarantee solution, so fallback large
                        best = 0
                    total_cost += best
                return total_cost
            else:
                return minimal_cost

    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.permutation = self.Permutation(p)

    def minimal_derangement_cost(self):
        solver = self.DerangementSolver(self.permutation)
        return solver.solve()


def main():
    import sys
    sys.setrecursionlimit(10**7)
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    transformer = DerangementTransformer(n, p)
    print(transformer.minimal_derangement_cost())

if __name__ == "__main__":
    main()