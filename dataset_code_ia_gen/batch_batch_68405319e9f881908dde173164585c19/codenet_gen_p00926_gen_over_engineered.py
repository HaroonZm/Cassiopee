class MallVisitPlanner:
    class Shop:
        def __init__(self, position: int):
            self.position = position
            self.constraints_before = set()
            self.constraints_after = set()

    class Constraint:
        def __init__(self, before_shop: int, after_shop: int):
            self.before_shop = before_shop
            self.after_shop = after_shop

    class DependencyGraph:
        def __init__(self, n):
            self.n = n
            self.adj = [[] for _ in range(n+2)]  # 1-based indexing, node 0 unused, node n+1 is exit
            self.in_degree = [0]*(n+2)

        def add_edge(self, u, v):
            self.adj[u].append(v)
            self.in_degree[v] += 1

        # Find strongly connected components to detect cycles
        def strongly_connected_components(self):
            index = 0
            stack = []
            on_stack = [False]*(self.n+2)
            indices = [-1]*(self.n+2)
            lowlink = [-1]*(self.n+2)
            sccs = []

            def strongconnect(v):
                nonlocal index
                indices[v] = index
                lowlink[v] = index
                index += 1
                stack.append(v)
                on_stack[v] = True
                for w in self.adj[v]:
                    if indices[w] == -1:
                        strongconnect(w)
                        lowlink[v] = min(lowlink[v], lowlink[w])
                    elif on_stack[w]:
                        lowlink[v] = min(lowlink[v], indices[w])
                if lowlink[v] == indices[v]:
                    scc = []
                    while True:
                        w = stack.pop()
                        on_stack[w] = False
                        scc.append(w)
                        if w == v:
                            break
                    sccs.append(scc)

            for v in range(1, self.n+1):
                if indices[v] == -1:
                    strongconnect(v)
            return sccs

    class MinimalWalkCalculator:
        def __init__(self, n, constraints):
            self.n = n
            self.constraints = constraints
            self.graph = MallVisitPlanner.DependencyGraph(n)

            # Build graph edges from constraints
            for c, d in constraints:
                # According to problem, must visit shop c after shop d
                # means c after d => edge d->c
                self.graph.add_edge(d, c)

        def find_minimal_length(self):
            # If no constraints, minimal length is entrance(0) to exit(N+1)
            # which is N+1 walking units
            if not self.constraints:
                return self.n + 1

            # We want to find a visiting order that respects d->c edges
            # and find minimal walking distance from entrance(0) → shops → exit(N+1).

            # The problem reduces to: given partial order constraints (d->c),
            # find a visiting sequence covering all shops and respecting constraints
            # minimizing walking distance from 0 to visit all shops in order and exit at n+1

            # Key insight: In absence of constraints, visit shops in order 1..n (distance n+1).
            # With constraints, she might have to return backward to fulfill them.

            # The minimal walking length is equivalent to the sum of:
            # distance from entrance(0) to first visited shop,
            # plus sum of distances between successive shops,
            # plus distance from last visited shop to exit(n+1).

            # Given positions shop k is at k units, and exit at n+1,
            # the cost equals to the length of the minimal path covering shops in order that respects constraints.

            # Let's analyze constraints:
            # If there is a chain d1->c1, c1->c2, etc,
            # user must visit them in that order, which might force backtracking.

            # Approach:
            # The shortest path that respects constraints is the minimal length interval [L,R] covering all shops
            # such that all shops with constraints are visited inside [L,R],
            # and order respects the constraints.

            # However, for arbitrary constraints, minimal length could be computed with DP over intervals after topological sort.

            # To handle this sophisticatedly, I'll build a partial order graph and find longest paths DAG to determine minimal walking.

            # Step 1: Detect cycles, which are impossible per problem statement.
            sccs = self.graph.strongly_connected_components()
            for scc in sccs:
                if len(scc) > 1:
                    raise RuntimeError("Cycles detected in constraints - no valid visiting order")

            # Step 2: Topological sort
            from collections import deque
            q = deque()
            in_degree = self.graph.in_degree[:]
            for i in range(1, self.n+1):
                if in_degree[i] == 0:
                    q.append(i)
            topo = []
            while q:
                u = q.popleft()
                topo.append(u)
                for w in self.graph.adj[u]:
                    in_degree[w] -= 1
                    if in_degree[w] == 0:
                        q.append(w)

            if len(topo) < self.n:
                raise RuntimeError("Impossible to find topological order")

            # Step 3: On this topological order, compute "minimum and maximum possible positions" of shops in visiting order
            # Key observation from problem statement: If c must be visited after d, and c > d:
            # she must pass shop d before reaching c, but must return back to d after c, increments walking distance.
            # The minimal cost is travel from entrance(0) to max visited position in order, plus traverse shops in order respecting constraints,
            # plus return from max position to exit(n+1).

            # The problem essentially requires summing (max position - min position + 1) plus the distance entrance to min and max to exit.

            # Let's find intervals induced by constraints and merge them.

            # Initialize intervals as singletons:
            intervals = [[i, i] for i in range(self.n+2)]  # 0..n+1, 0=entrance, n+1=exit

            # We'll union intervals for shops connected by constraints to identify continuous segments required.

            parent = list(range(self.n+2))
            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            def union(a,b):
                ra, rb = find(a), find(b)
                if ra != rb:
                    # merge intervals
                    intervals[ra][0] = min(intervals[ra][0], intervals[rb][0])
                    intervals[ra][1] = max(intervals[ra][1], intervals[rb][1])
                    parent[rb] = ra

            # For each constraint edge d->c, union their intervals
            for d, c in self.constraints:
                union(d,c)

            # Find min and max shop position over all intervals involving constrained shops
            constrained_roots = set(find(c) for c, _ in self.constraints) | set(find(d) for _, d in self.constraints)

            # The minimal path must span the minimal minPos and maximal maxPos of these intervals plus entrance and exit.

            # If no constraints, intervals is empty => minimal length = n+1

            if not constrained_roots:
                return self.n + 1

            min_pos = self.n+1
            max_pos = 0
            for r in constrained_roots:
                min_pos = min(min_pos, intervals[r][0])
                max_pos = max(max_pos, intervals[r][1])

            # Minimal length travel:
            # start at 0,
            # walk to min_pos,
            # cover segment min_pos to max_pos and back if needed,
            # then exit at n+1

            # The cost is (min_pos - 0) + (max_pos - min_pos)*2 + (n+1 - max_pos)
            # The (max_pos - min_pos)*2 because she may have to go back and forth within that interval if constraints force visiting order backwards

            # However, checking samples for edge cases:
            # Sometimes it's better to just walk straight 0->n+1 if constraints empty.

            # Return calculated value:
            return (min_pos - 0) + 2 * (max_pos - min_pos) + (self.n + 1 - max_pos)

    def __init__(self, n, m, constraints):
        self.n = n
        self.m = m
        self.constraints = constraints
        self.calculator = MallVisitPlanner.MinimalWalkCalculator(n, constraints)

    def solve(self):
        return self.calculator.find_minimal_length()


def main():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    constraints = [tuple(map(int, input().split())) for _ in range(m)]
    planner = MallVisitPlanner(n, m, constraints)
    print(planner.solve())

if __name__ == "__main__":
    main()