class IslandNetwork:
    class Edge:
        def __init__(self, u, v, cost, index):
            self.u = u
            self.v = v
            self.cost = cost
            self.index = index # to uniquely identify edges if needed

        def __lt__(self, other):
            # For sorting edges by cost
            return self.cost < other.cost

    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.rank = [0] * size

        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def union(self, x, y):
            rx = self.find(x)
            ry = self.find(y)
            if rx == ry:
                return False
            if self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry
            else:
                self.parent[ry] = rx
                if self.rank[rx] == self.rank[ry]:
                    self.rank[rx] += 1
            return True

    class KruskalWithGroup:
        """
        Advanced Kruskal that handles edges of the same cost simultaneously,
        so that we can find all possible MSTs edges group by group
        """
        def __init__(self, n, edges):
            self.n = n
            self.edges = edges
            self.uf = IslandNetwork.UnionFind(n)
            self.selected_edges = []  # edges that are chosen in an MST or candidate MST

        def process(self):
            # Sort edges by cost ascending
            self.edges.sort()

            group_start = 0
            while group_start < len(self.edges):
                group_end = group_start + 1
                c = self.edges[group_start].cost
                while group_end < len(self.edges) and self.edges[group_end].cost == c:
                    group_end += 1

                # Process edges in this cost group collectively
                self._process_group(self.edges[group_start:group_end])

                group_start = group_end

        def _process_group(self, group_edges):
            # Step 1: For the edges in the current group, identify those connecting different components
            # Step 2: Build a graph of components connected by these edges
            # Step 3: For the components graph, find bridges, those bridges correspond to edges that must be in all MSTs
            # Step 4: Union the connected components using these group edges to extend MST forest

            uf = self.uf
            # Identify components before adding these edges
            comp_id_map = {}
            comp_count = 0
            # Map current node to component representative
            comp_repr = [uf.find(i) for i in range(self.n)]
            # Map component representative to compressed id
            for cr in comp_repr:
                if cr not in comp_id_map:
                    comp_id_map[cr] = comp_count
                    comp_count += 1

            # Build graph of component nodes connected by edges
            adj = [[] for _ in range(comp_count)]

            # Edges in DSF graph will be stored with original edge information
            # We'll keep a list of the edges to analyze for bridges
            comp_edges = []

            # For each edge in the group, if endpoints belong to different components in DSF, we add edge in comp graph
            for e in group_edges:
                cu = comp_id_map[uf.find(e.u)]
                cv = comp_id_map[uf.find(e.v)]
                if cu != cv:
                    comp_edges.append((cu, cv, e))
                    adj[cu].append( (cv, e) )
                    adj[cv].append( (cu, e) )

            # Find bridges (edges that appear in all MSTs in this cost group)
            bridges = self._find_bridges(comp_count, adj)

            # Mark those edges corresponding to bridges as selected no-alternative edges
            for (cu, cv, e) in comp_edges:
                if (cu, cv) in bridges or (cv, cu) in bridges:
                    self.selected_edges.append(e)

            # Finally, union all edges in this group that connect different components (MST edges choose any subset but have to extend union)
            for e in group_edges:
                uf.union(e.u, e.v)

        def _find_bridges(self, n, adj):
            """
            Classic bridge-finding in undirected graph by Tarjan's algorithm
            """
            ids = [-1]*n
            low = [-1]*n
            bridges = set()
            self._id_counter = 0
            def dfs(u, parent):
                ids[u] = self._id_counter
                low[u] = self._id_counter
                self._id_counter += 1
                for (w, edge) in adj[u]:
                    if ids[w] == -1:
                        dfs(w, u)
                        low[u] = min(low[u], low[w])
                        if low[w] > ids[u]:
                            # (u, w) is a bridge
                            bridges.add((u,w))
                    elif w != parent:
                        low[u] = min(low[u], ids[w])

            for i in range(n):
                if ids[i]==-1:
                    dfs(i,-1)
            return bridges


    def __init__(self, N, edge_data):
        self.N = N
        self.edges = [IslandNetwork.Edge(u-1,v-1,c,i) for i,(u,v,c) in enumerate(edge_data)]

    def solve(self):
        kruskal = IslandNetwork.KruskalWithGroup(self.N, self.edges)
        kruskal.process()
        # Calculate number and sum of no alternative edges
        total_cost = sum(e.cost for e in kruskal.selected_edges)
        total_count = len(kruskal.selected_edges)
        return total_count, total_cost

def main():
    import sys
    input = sys.stdin.readline
    N,M = map(int,input().split())
    edge_data = [tuple(map(int,input().split())) for _ in range(M)]
    network = IslandNetwork(N, edge_data)
    count, cost = network.solve()
    print(count, cost)

if __name__ == "__main__":
    main()