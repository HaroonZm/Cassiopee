class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.adj = []  # list of Edge
        self.has_base = False

class TreeSplitter:
    def __init__(self, n, t, k):
        self.n = n
        self.t = t
        self.k = k
        self.nodes = [Node(i) for i in range(n+1)]
        self.INF = 10**9

    def add_edge(self, u, v, cost):
        edge_uv = Edge(u, v, cost)
        edge_vu = Edge(v, u, cost)
        self.nodes[u].adj.append(edge_uv)
        self.nodes[v].adj.append(edge_vu)

    def set_bases(self, bases):
        for b in bases:
            self.nodes[b].has_base = True

    def solve(self):
        # We will root the tree at 1 (problem statement assumes nodes numbered 1..n)
        self.dp = [None]*(self.n+1)
        self.visited = [False]*(self.n+1)
        def dfs(u):
            self.visited[u] = True
            # dp[u]: dict mapping number of cuts (0 to k) -> minimal cost for subtree rooted at u
            # but we also need to consider number of bases in subtree:
            # Actually we want dp[u][c]: minimal cost to split subtree rooted at u
            # with c cuts and at least c+1 base-containing components
            # Actually, base count in subtree is important for DP dimension:
            base_count = 1 if self.nodes[u].has_base else 0
            
            # dp[c][b]: minimum cost when cutting c edges in subtree,
            # generating c+1 regions which contain b bases in total (b should match subtree's base count eventually)
            # but only b from 0 up to subtree base count matter.
            # Actually since subtree structure is fixed, total bases is fixed, so b is base count in subtree rooted at u.
            # Actually we only need dp[c]: minimal cost when we do c cuts in subtree of u.
            # But we need base count per subtree to check constraints when merging children's dp
            
            # We will store:
            # An object with:
            # - total_bases: base count in subtree
            # - dp[c]: minimal cost to disconnect subtree with c cuts such that each of c+1 regions has at least one base.
            
            dp = {0: 0}
            total_bases = base_count

            for edge in self.nodes[u].adj:
                v = edge.v
                if self.visited[v]: continue
                dfs(v)
                child_info = self.dp[v]
                child_bases = child_info['total_bases']
                child_dp = child_info['dp']

                # We'll combine dp of u so far and child's dp; this is similar to merging two subtrees
                # The problem:
                # We want to form partition with c cuts, meaning total connected regions = c+1
                # For merging current dp (with some cuts c1) and child's dp (with c2 cuts):
                # - Option 1: Do not cut edge (u,v): combine regions, total cuts = c1 + c2,
                #   regions = (c1+1) + (c2 +1) - 1 = c1 + c2 +1
                # - Option 2: Cut edge (u,v): pay cost edge.cost, total cuts = c1 + c2 + 1,
                #   regions = (c1+1) + (c2 +1) = c1 + c2 + 2

                # However we must ensure that in final regions each has at least one base.
                # Since we always cut edges that separate subtrees with bases, base count info is crucial.

                # Let's define new dp dict new_dp = {}
                new_dp = {}

                for c1, cost1 in dp.items():
                    for c2, cost2 in child_dp.items():
                        # Option 1: not cut
                        # regions = (c1+1)+(c2+1)-1 = c1 + c2 +1 cuts
                        # but total cuts still c1 + c2, as no edge cut added
                        # Does base condition hold? bases are merged.
                        c = c1 + c2
                        val = cost1 + cost2
                        if c <= self.k:
                            if c not in new_dp or new_dp[c] > val:
                                new_dp[c] = val
                        # Option 2: cut this edge
                        # cuts = c1 + c2 + 1
                        c_cut = c1 + c2 + 1
                        val_cut = cost1 + cost2 + edge.cost
                        if c_cut <= self.k:
                            if c_cut not in new_dp or new_dp[c_cut] > val_cut:
                                new_dp[c_cut] = val_cut

                dp = new_dp
                total_bases += child_bases

            self.dp[u] = {'total_bases': total_bases, 'dp': dp}

        dfs(1)
        # final answer must have exactly k cuts and k+1 regions each with base:
        # We store only solutions with viable partitions, so dp at root with k cuts is the answer.
        ans = self.dp[1]['dp'].get(self.k, self.INF)
        return ans

class InputProcessor:
    def __init__(self):
        self.case_num = 0

    def process(self):
        while True:
            line = ''
            while line.strip() == '':
                line = input()
            n, t, k = map(int,line.strip().split())
            if n == 0 and t == 0 and k == 0:
                break
            splitter = TreeSplitter(n, t, k)
            for _ in range(n-1):
                u,v,cost = map(int,input().strip().split())
                splitter.add_edge(u,v,cost)
            bases = []
            for _ in range(t):
                bases.append(int(input().strip()))
            splitter.set_bases(bases)
            self.case_num +=1
            res = splitter.solve()
            print(f"Case {self.case_num}: {res}")

if __name__ == "__main__":
    InputProcessor().process()