class TrainFareSystem:
    class Edge:
        def __init__(self, u: int, v: int):
            self.u = u
            self.v = v

        def other(self, node: int) -> int:
            return self.v if node == self.u else self.u

    class Graph:
        def __init__(self, n: int):
            self.n = n
            self.adj = [[] for _ in range(n + 1)]  # 1-based nodes
            self.edges = []

        def add_edge(self, u: int, v: int):
            edge = TrainFareSystem.Edge(u, v)
            eid = len(self.edges)
            self.edges.append(edge)
            self.adj[u].append(eid)
            self.adj[v].append(eid)

    class DijkstraResult:
        def __init__(self, dist, parent_edge):
            self.dist = dist
            self.parent_edge = parent_edge

    def __init__(self, n: int, edges_uv, q: int, raise_plan):
        self.n = n
        self.m = len(edges_uv)
        self.q = q
        self.graph = self.Graph(n)
        for u, v in edges_uv:
            self.graph.add_edge(u, v)
        self.raise_plan = raise_plan

    def calculate_initial_distances(self):
        from collections import deque
        # Because initial weight = 1 for all edges, shortest path dist = BFS layers
        dist = [float('inf')] * (self.n + 1)
        parent_edge = [-1] * (self.n + 1)
        dist[1] = 0
        queue = deque([1])
        while queue:
            node = queue.popleft()
            for eid in self.graph.adj[node]:
                e = self.graph.edges[eid]
                nxt = e.other(node)
                if dist[nxt] > dist[node] + 1:
                    dist[nxt] = dist[node] + 1
                    parent_edge[nxt] = eid
                    queue.append(nxt)
        return self.DijkstraResult(dist, parent_edge)

    def build_tree_from_parents(self, parent_edge):
        # Build tree from parent edges, root=1
        tree = [[] for _ in range(self.n + 1)]
        for v in range(2, self.n + 1):
            eid = parent_edge[v]
            if eid == -1:
                continue
            edge = self.graph.edges[eid]
            u = edge.other(v)
            tree[u].append(v)
        return tree

    def dfs_subtree_size(self, tree, node, size_arr):
        size_arr[node] = 1
        for nxt in tree[node]:
            self.dfs_subtree_size(tree, nxt, size_arr)
            size_arr[node] += size_arr[nxt]

    def solve(self):
        # Step 1: compute initial shortest path tree from node 1 with weight=1
        dres = self.calculate_initial_distances()
        dist_init = dres.dist
        parent_edge = dres.parent_edge

        # Step 2: Build shortest path tree from initial shortest paths (edges on shortest path)
        tree = self.build_tree_from_parents(parent_edge)

        # Step 3: DFS to get subtree sizes to count nodes affected by incrementing an edge in the shortest path tree
        subtree_size = [0] * (self.n + 1)
        self.dfs_subtree_size(tree, 1, subtree_size)

        # Step 4: Mark edges that are in the shortest path tree
        in_tree = [False] * self.m
        for v in range(2, self.n + 1):
            eid = parent_edge[v]
            if eid != -1:
                in_tree[eid] = True

        # Step 5: Initialize dissatisfaction counts per year
        # Initially, no dissatisfaction (year 0)
        dissatisfactions = [0] * (self.q + 1)  # 1-based year; dissatisfactions[j] = count in year j

        # Step 6: We simulate years and price raises.
        # Each price increase changes cost of one edge from 1 to 2.
        # Increasing an edge on the shortest path tree increases cost to all in its subtree by 1.
        # Increasing edge not in shortest path tree has no effect on shortest path costs, because alternate routes cost >= current.
        # When an edge in the tree is increased, dissatisfaction increases by size of subtree except root (city1).

        # We will track dissatisfaction count incrementally.
        current_dissatisfaction = 0
        # Map from edge id to iteration/year index
        edge_price_up_year = [-1] * self.m
        for year, eid in enumerate(self.raise_plan, 1):
            edge_price_up_year[eid - 1] = year

        # We prepare a list of (year, impact) for all relevant edges (those in tree)
        # At the year when edge's price increases, dissatisfaction += subtree_size of child node connected by that edge.
        year_events = [0] * (self.q + 2)  # +2 for safety
        for eid in range(self.m):
            if in_tree[eid]:
                # Identify child node of this edge in tree (since tree edges go from parent to child)
                u = self.graph.edges[eid].u
                v = self.graph.edges[eid].v
                # parent is the endpoint with lower dist (ie, closer to root)
                if dist_init[u] < dist_init[v]:
                    parent = u
                    child = v
                else:
                    parent = v
                    child = u
                year = edge_price_up_year[eid]
                if year != -1:
                    # At year-th price raise, dissatisfaction increases by subtree_size[child]
                    year_events[year] += subtree_size[child]

        # Step 7: Accumulate dissatisfaction over years
        for year in range(1, self.q + 1):
            current_dissatisfaction += year_events[year]
            dissatisfactions[year] = current_dissatisfaction

        # Step 8: Output dissatisfaction count for each year
        # City 1 never dissatisfied by problem statement
        # The subtree sizes exclude city 1 from increment count naturally (root's subtree size includes whole)
        return dissatisfactions[1:]  # year 1 to Q


def main():
    import sys
    input = sys.stdin.readline

    N, M, Q = map(int, input().split())
    edges_uv = [tuple(map(int, input().split())) for _ in range(M)]
    raise_plan = [int(input()) for _ in range(Q)]

    system = TrainFareSystem(N, edges_uv, Q, raise_plan)
    results = system.solve()
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    main()