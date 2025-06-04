import sys
sys.setrecursionlimit(10**7)
from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

class Edge:
    def __init__(self, u: int, v: int, cost: int):
        self.u = u
        self.v = v
        self.cost = cost

class Node:
    def __init__(self, index: int, cicadas: int):
        self.index = index
        self.cicadas = cicadas
        self.edges: List[Edge] = []

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

class Tree(ABC):
    @abstractmethod
    def minimal_pruning_cost(self) -> int:
        pass

class CicadaPruningTree(Tree):
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes
        self.N = len(nodes)
        self.visited = [False]*self.N
        self.dp: List[int] = [0]*self.N  # min cost to remove cicadas in subtree
        self.cicada_count: List[int] = [0]*self.N  # cicadas in subtree

    def minimal_pruning_cost(self) -> int:
        # Run DFS from root 0 to compute DP
        self._dfs(0)
        # minimal cost to remove all cicadas not on root is dp at root
        return self.dp[0]

    def _dfs(self, current: int) -> None:
        self.visited[current] = True
        node = self.nodes[current]
        # Start with cicadas on this node
        subtotal_cicadas = node.cicadas
        subtotal_cost = 0

        for edge in node.edges:
            nxt = edge.v if edge.u == current else edge.u
            if self.visited[nxt]:
                continue
            self._dfs(nxt)
            # after dfs on child nxt:
            # cicada_count[nxt] cicadas in its subtree
            # dp[nxt] minimal cost to remove the subtree cicadas

            # If subtree has cicadas, decide to cut edge or remove inside subtree
            if self.cicada_count[nxt] > 0:
                # either cut this edge paying edge.cost to remove all cicadas in child subtree at once
                # or pay dp[nxt] cost removing inside subtree
                subtotal_cost += min(edge.cost, self.dp[nxt])
                # do not add child's cicadas to parent's cicadas since they are removed
                # if we do dp[nxt], cicadas are removed inside subtree, so 0 remains outside to count
                # if we cut edge, cicadas also removed
            else:
                # no cicadas in subtree, no cost and no cicadas added
                subtotal_cost += 0

            # add cicadas of subtree only if not cut edge; but since we took min, cicadas are removed anyway
            # so cicadas do not accumulate above cut edges

        self.cicada_count[current] = subtotal_cicadas
        self.dp[current] = subtotal_cost

def parse_input() -> Tuple[int, List[int], List[Tuple[int,int,int]]]:
    import sys
    input = sys.stdin.readline
    N = int(input())
    Cs_line = input().strip()
    # sometimes there could be leading/trailing spaces, split carefully
    Cs = list(map(int, Cs_line.split()))
    edges = []
    for _ in range(N-1):
        u,v,p = map(int, input().split())
        edges.append((u,v,p))
    return N, Cs, edges

class Parser:
    def __init__(self):
        pass

    def parse(self) -> Tuple[List[Node], List[Edge]]:
        N, Cs, edge_data = parse_input()
        nodes = [Node(i, Ci) for i,Ci in enumerate(Cs)]
        for u,v,p in edge_data:
            edge = Edge(u,v,p)
            nodes[u].add_edge(edge)
            nodes[v].add_edge(edge)
        return nodes, edge_data

class Solver:
    def __init__(self):
        self.parser = Parser()

    def solve(self):
        nodes, edges = self.parser.parse()
        tree = CicadaPruningTree(nodes)
        ans = tree.minimal_pruning_cost()
        print(ans)

if __name__ == "__main__":
    solver = Solver()
    solver.solve()