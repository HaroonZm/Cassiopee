class NumberSortingSolver:
    def __init__(self, a: int, b: int, p: int):
        self.a = a
        self.b = b
        self.p = p
        self.numbers = list(range(a, b + 1))
        self.size = len(self.numbers)
        self.adj_list = {}
        self.components = []
    
    class LexicoComparator:
        @staticmethod
        def compare_num_str_lex(n1: int, n2: int) -> bool:
            # Return True if n1 < n2 lexicographically by string representation, else False
            return str(n1) < str(n2)
        
        @staticmethod
        def compare_numeric(n1: int, n2: int) -> bool:
            # Return True if n1 < n2 numerically, else False
            return n1 < n2
        
        @classmethod
        def is_conflict(cls, n1: int, n2: int) -> bool:
            # There is conflict if relative orderings numeric and lexicographic differ
            numeric_less = cls.compare_numeric(n1, n2)
            lex_less = cls.compare_num_str_lex(n1, n2)
            return numeric_less != lex_less

    class GraphBuilder:
        def __init__(self, numbers, comparator):
            self.numbers = numbers
            self.comp = comparator
            self.graph = {num: set() for num in numbers}
        
        def build_graph(self):
            # Connect pairs that break sorted order equivalence:
            # If numeric < but lexicographically > (or converse), add edge because can't be in same valid subset
            n = len(self.numbers)
            nums = self.numbers
            for i in range(n):
                for j in range(i + 1, n):
                    ni, nj = nums[i], nums[j]
                    if self.comp.is_conflict(ni, nj):
                        self.graph[ni].add(nj)
                        self.graph[nj].add(ni)
            return self.graph
    
    class ComponentFinder:
        def __init__(self, graph):
            self.graph = graph
            self.visited = set()
            self.components = []
        
        def dfs(self, node):
            stack = [node]
            comp = []
            while stack:
                cur = stack.pop()
                if cur not in self.visited:
                    self.visited.add(cur)
                    comp.append(cur)
                    neighbors = self.graph[cur]
                    for nxt in neighbors:
                        if nxt not in self.visited:
                            stack.append(nxt)
            return comp
        
        def find_components(self):
            for node in self.graph:
                if node not in self.visited:
                    comp = self.dfs(node)
                    self.components.append(comp)
            return self.components
    
    class IndependentSetCounter:
        def __init__(self, graph, mod):
            self.graph = graph
            self.mod = mod
            self.memo = {}
        
        def bit_repr(self, nodes):
            # map node to index and return list of nodes by index
            self.nodes = nodes
            self.node_index = {node: idx for idx, node in enumerate(nodes)}
            # adjacency bitmasks
            self.adj_mask = [0] * len(nodes)
            for node in nodes:
                idx = self.node_index[node]
                for neighbor in self.graph[node]:
                    if neighbor in self.node_index:
                        nid = self.node_index[neighbor]
                        self.adj_mask[idx] |= (1 << nid)
        
        def count_independent_sets(self):
            # Use bitmask and DP over subsets approach:
            n = len(self.nodes)
            # DP[s] = number of independent sets represented by subset s
            # bottom up could be exponential (2^n) - refined method: use backtracking + memo
            self.memo = {}
            def dfs(used_mask, pos):
                if pos == n:
                    return 1
                key = (used_mask, pos)
                if key in self.memo:
                    return self.memo[key]
                # Skip current node
                res = dfs(used_mask, pos + 1)
                # Take current node: only if none neighbor taken before
                if (used_mask & self.adj_mask[pos]) == 0:
                    res += dfs(used_mask | (1 << pos), pos + 1)
                res %= self.mod
                self.memo[key] = res
                return res
            return dfs(0, 0)
    
    def calculate(self) -> int:
        # Step 1: Build conflict graph
        builder = self.GraphBuilder(self.numbers, self.LexicoComparator)
        self.adj_list = builder.build_graph()
        # Step 2: Find connected components
        finder = self.ComponentFinder(self.adj_list)
        components = finder.find_components()
        # Step 3: For each component count independent sets
        # number of valid subsets = product of count_of_independent_sets over components
        # minus 1 (the empty subset)
        mod = self.p
        result = 1
        for comp in components:
            counter = self.IndependentSetCounter(self.adj_list, mod)
            counter.bit_repr(comp)
            sets_count = counter.count_independent_sets()
            result = (result * sets_count) % mod
        # subtract empty subset globally
        result = (result - 1) % mod
        return result

def main():
    import sys
    for line in sys.stdin:
        if line.strip() == '':
            continue
        A, B, P = map(int, line.strip().split())
        if A == 0 and B == 0 and P == 0:
            break
        solver = NumberSortingSolver(A, B, P)
        print(solver.calculate())

if __name__ == "__main__":
    main()