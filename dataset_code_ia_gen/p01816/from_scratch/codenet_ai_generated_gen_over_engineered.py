import sys
sys.setrecursionlimit(10**9)
from typing import List, Tuple, Dict, Callable

class Operation:
    def __init__(self, op_str: str):
        # op_str is like 'T=T&X' or 'T=T^Y'
        # Extract operator and operand
        # Format guaranteed by problem
        self.raw = op_str
        self.operator = op_str[3]  # &, |, ^
        self.operand_var = op_str[-1]  # X or Y

    def eval(self, T: int, X: int, Y: int) -> int:
        operand = X if self.operand_var == "X" else Y
        if self.operator == '&':
            return T & operand
        elif self.operator == '|':
            return T | operand
        elif self.operator == '^':
            return T ^ operand
        else:
            raise ValueError("Unknown operator")

class Node:
    def __init__(self, idx: int, op: Operation = None):
        self.idx = idx
        self.op = op
        self.children: List[int] = []

class BitOperationGameSolver:
    def __init__(self, N: int):
        self.N = N
        self.nodes: List[Node] = []
        # Root node op is fixed T=0, no operation effectively
        self.nodes.append(Node(0, None)) # root
        for i in range(1, N):
            self.nodes.append(Node(i))
        self.adj: List[List[int]] = [[] for _ in range(N)]
        self.M = 0
        self.games: List[Tuple[int,int]] = []

    def set_operation(self, idx: int, op: str):
        self.nodes[idx].op = Operation(op)

    def add_edge(self, u: int, v: int):
        self.nodes[u].children.append(v)
        self.nodes[v].children.append(u)

    def build_tree(self):
        # Convert undirected graph to rooted tree at 0 with directed edges downwards
        self.tree_children = [[] for _ in range(self.N)]
        self.parent = [-1]*self.N
        from collections import deque
        q = deque([0])
        self.parent[0] = -2 # root
        while q:
            u = q.popleft()
            for w in self.nodes[u].children:
                if self.parent[w] == -1:
                    self.parent[w] = u
                    self.tree_children[u].append(w)
                    q.append(w)

    def solve(self, games: List[Tuple[int,int]]) -> List[int]:
        self.M = len(games)
        self.games = games

        # We'll do a binary search DP/memo for each game:
        # But constraints: N=1e5, M=1e5 is large.
        # We need a data structure to represent each subtree:
        # Each player tries to maximize/minimize final T.
        #
        # Approach:
        # Build a class TreeGameSolver with DP memo of function T->score for subtree for given (X,Y)
        #
        # Because X,Y vary each query and can be large (2^16),
        # we precompute the subtree states that are independent of X,Y,
        # then for each query we run the game optimizing with given X,Y.
        #
        # The strategy of each player is to choose the child that yields the best outcome for them.
        #
        # Let's factor the problem into abstract classes.

        class StrategyNode:
            def __init__(self, idx: int, children: List['StrategyNode'], op: Operation):
                self.idx = idx
                self.children = children
                self.op = op

            # Compute the optimal score of this subtree for given T,X,Y, turn (True=Alice max, False=Bob min)
            def optimal_score(self, T: int, X: int, Y: int, is_alice_turn: bool, memo: Dict) -> int:
                key = (self.idx, T, is_alice_turn)
                if key in memo:
                    return memo[key]
                # Apply operation for current node
                curT = T
                if self.op is not None:
                    curT = self.op.eval(T, X, Y)
                # If leaf
                if not self.children:
                    # leaf reached final T value
                    memo[key] = curT
                    return curT
                # Otherwise, choose next move by turn
                if is_alice_turn:
                    # Alice tries to maximize
                    v = -1
                    for c in self.children:
                        child_score = c.optimal_score(curT, X, Y, not is_alice_turn, memo)
                        if child_score > v:
                            v = child_score
                    memo[key] = v
                    return v
                else:
                    # Bob tries to minimize
                    v = (1 << 30) + 10
                    for c in self.children:
                        child_score = c.optimal_score(curT, X, Y, not is_alice_turn, memo)
                        if child_score < v:
                            v = child_score
                    memo[key] = v
                    return v

        # Build StrategyNode tree
        strategy_nodes = [None]*self.N

        def build_strategy_node(u: int) -> StrategyNode:
            if strategy_nodes[u] is not None:
                return strategy_nodes[u]
            children_nodes = [build_strategy_node(c) for c in self.tree_children[u]]
            strategy_nodes[u] = StrategyNode(u, children_nodes, self.nodes[u].op)
            return strategy_nodes[u]

        root_node = build_strategy_node(0)

        results = []
        for (X,Y) in self.games:
            memo = dict()
            res = root_node.optimal_score(0, X, Y, True, memo)
            results.append(res)
        return results

def main():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    solver = BitOperationGameSolver(N)
    # read ops lines for nodes 1..N-1
    for i in range(1, N):
        opstr = input().strip()
        solver.set_operation(i, opstr)
    # read edges
    for _ in range(N-1):
        u,v = map(int, input().split())
        solver.add_edge(u, v)
    solver.build_tree()
    games = []
    for _ in range(M):
        X,Y = map(int, input().split())
        games.append((X,Y))
    ans = solver.solve(games)
    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()