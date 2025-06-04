MOD = 10**9 + 7

from typing import List, Dict, Union, Optional
from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self, idx: int, optional: bool):
        self.idx = idx
        self.optional = optional
        self.children: List['Node'] = []

    def add_child(self, child: 'Node'):
        self.children.append(child)

    @abstractmethod
    def count_combinations(self) -> int:
        ...

class SubstanceNode(Node):
    # Substance node: either optional or not
    def count_combinations(self) -> int:
        # If optional, can choose or not choose (2 ways)
        # If not optional, must choose (1 way)
        return 2 if self.optional else 1

class SelectionNode(Node):
    # Abstract selection node
    def __init__(self, idx: int, optional: bool):
        super().__init__(idx, optional)

    @abstractmethod
    def count_combinations(self) -> int:
        ...

class OrSelectionNode(SelectionNode):
    # Or type: must choose at least one child if not optional,
    # If optional: can choose no children as well
    def count_combinations(self) -> int:
        child_counts = [child.count_combinations() for child in self.children]

        # For Or: total combinations = number of ways to choose subset (non-empty if non-optional),
        # where each chosen child multiplies child_counts, and unchosen contribute 1.
        # Using product for each child's (1 + count) - 1 because at least one chosen:
        # total = product(1 + child_count) - 1
        ways = 1
        for c in child_counts:
            ways = (ways * (1 + c)) % MOD

        if not self.optional:
            ways = (ways - 1) % MOD  # exclude 'choose none'
        # else optional: can choose empty subset, so ways keep

        return ways

class AltSelectionNode(SelectionNode):
    # Alt type: choose exactly one child if not optional,
    # if optional: choose zero or one child
    def count_combinations(self) -> int:
        child_counts = [child.count_combinations() for child in self.children]

        total = sum(child_counts) % MOD
        if self.optional:
            # can choose none (1 way) or one child
            total = (total + 1) % MOD
        # else must choose exactly one child, sum of child counts

        return total

# Factory for Node creation anticipating extensions.
class NodeFactory:
    @staticmethod
    def create_node(idx:int, info: str) -> Node:
        optional = info.endswith('?')
        base = info[:-1] if optional else info

        if base == 'E':
            return SubstanceNode(idx, optional)
        elif base == 'R':
            return OrSelectionNode(idx, optional)
        elif base == 'A':
            return AltSelectionNode(idx, optional)
        else:
            raise ValueError(f'Unknown node type: {info}')

class DrugCombinationTree:
    def __init__(self, n: int):
        self.n = n
        self.nodes: Dict[int, Node] = {}

    def build_nodes(self, node_infos: List[str]) -> None:
        for i in range(1, self.n + 1):
            self.nodes[i] = NodeFactory.create_node(i, node_infos[i-1])

    def build_tree(self, edges: List[List[int]]) -> None:
        # edges: [(s, t), ...], s parent, t child
        for s, t in edges:
            parent = self.nodes[s]
            child = self.nodes[t]
            parent.add_child(child)

    def count_all_combinations(self) -> int:
        # According to problem: root is node 1, not optional by condition given
        root = self.nodes[1]
        # The count_combinations returns total number of ways to realize subtree
        return root.count_combinations() % MOD


def main():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N = int(input())
    node_infos = [input().strip() for _ in range(N)]
    edges = [list(map(int, input().split())) for _ in range(N-1)]

    tree = DrugCombinationTree(N)
    tree.build_nodes(node_infos)
    tree.build_tree(edges)

    ans = tree.count_all_combinations()
    print(ans)

if __name__ == '__main__':
    main()