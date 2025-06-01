MOD = 10**9 + 7

from abc import ABC, abstractmethod
from typing import List, Dict

# Interface for any node in the drug formulation tree
class Node(ABC):
    def __init__(self, node_id: int, optional: bool):
        self.node_id = node_id
        self.optional = optional
        self.children: List[Node] = []

    def add_child(self, child: 'Node'):
        self.children.append(child)

    @abstractmethod
    def count_combinations(self) -> int:
        pass

# Concrete class for "substance nodes" (物質ノード, type E)
class SubstanceNode(Node):
    def __init__(self, node_id: int, optional: bool):
        super().__init__(node_id, optional)

    def count_combinations(self) -> int:
        # If node optional: can choose to include or not (2 options)
        # If not optional: must include (1 option)
        # When included, we must count children combinations recursively.
        if not self.children:
            return 2 if self.optional else 1
        # Count combinations for children
        child_combinations = 1
        for c in self.children:
            child_combinations *= c.count_combinations()
            child_combinations %= MOD
        if self.optional:
            # option to include or not
            # Not selected => 1 combination (empty), Selected => child_combinations
            return (child_combinations + 1) % MOD
        else:
            return child_combinations % MOD

# Abstract base class for selection nodes (選択ノード)
class SelectionNode(Node, ABC):
    def __init__(self, node_id: int, optional: bool):
        super().__init__(node_id, optional)

    @abstractmethod
    def count_combinations(self) -> int:
        # Common logic is handled separately by each subtype
        pass

# OR node (R型)
class OrNode(SelectionNode):
    def __init__(self, node_id: int, optional: bool):
        super().__init__(node_id, optional)

    def count_combinations(self) -> int:
        # or 型 (R) node:
        # If not optional, must select at least one child.
        # If optional, can select none or at least one.
        # Total ways = sum over all non-empty subsets of children of product of children's combinations
        # Since children are not optional, child.count_combinations() means ways child is selected.
        # We use principle of inclusion-exclusion or faster:
        # Total combinations of subsets = product over children of (1 + child_count)
        # -1 (remove empty set) if node not optional
        # else include empty set

        child_plus_one = 1
        for c in self.children:
            child_plus_one *= (c.count_combinations() + 1)  # +1 for "not select this child"
            child_plus_one %= MOD
        if self.optional:
            # optional means can select none => total = child_plus_one subsets including empty
            return child_plus_one % MOD
        else:
            # must select at least one child => subtract empty set
            return (child_plus_one - 1) % MOD

# ALT node (A型)
class AltNode(SelectionNode):
    def __init__(self, node_id: int, optional: bool):
        super().__init__(node_id, optional)

    def count_combinations(self) -> int:
        # alt 型 (A) node:
        # If not optional: exactly one child must be selected
        # If optional: zero or one child may be selected
        # Since children are not optional substance nodes, child's count_combinations() = ways selecting that child
        sum_children = 0
        for c in self.children:
            sum_children += c.count_combinations()
        sum_children %= MOD
        if self.optional:
            # can select 0 child (1 way) + select exactly 1 child (sum_children)
            return (sum_children + 1) % MOD
        else:
            # must select exactly 1 child
            return sum_children % MOD

# Factory pattern to create nodes based on input description
class NodeFactory:
    @staticmethod
    def create_node(node_id: int, description: str) -> Node:
        optional = description.endswith('?')
        base_descr = description[:-1] if optional else description
        if base_descr == 'E':
            return SubstanceNode(node_id, optional)
        elif base_descr == 'R':
            return OrNode(node_id, optional)
        elif base_descr == 'A':
            return AltNode(node_id, optional)
        else:
            raise ValueError(f"Unknown node description: {description}")

# Graph structure holding all nodes and managing connections
class DrugTree:
    def __init__(self, node_descriptions: List[str], edges: List[List[int]]):
        self.N = len(node_descriptions)
        # id: Node , nodes indexed from 1 to N
        self.nodes: Dict[int, Node] = {}
        # create nodes
        for i, desc in enumerate(node_descriptions, 1):
            self.nodes[i] = NodeFactory.create_node(i, desc)

        # add children edges
        # Each edge: from s_i to t_i
        for s, t in edges:
            self.nodes[s].add_child(self.nodes[t])

        # The root is node 1 by problem statement
        self.root = self.nodes[1]

    def compute_combinations(self) -> int:
        # Start counting from root
        # Root is never optional by problem statement
        return self.root.count_combinations() % MOD

# Input/Output management with the defined abstractions
def main():
    import sys
    sys.setrecursionlimit(2000)

    N = int(sys.stdin.readline())
    node_descriptions = [sys.stdin.readline().strip() for _ in range(N)]
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N - 1)]

    drug_tree = DrugTree(node_descriptions, edges)
    res = drug_tree.compute_combinations()
    print(res)

if __name__ == "__main__":
    main()