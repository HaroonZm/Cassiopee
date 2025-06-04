from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Tuple


class Node:
    def __init__(self, node_id: int):
        self.id = node_id
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def __repr__(self):
        return f"Node({self.id})"


class TreeBuilder:
    def __init__(self, nodes_info: List[Tuple[int, int, int]]):
        self.nodes_info = nodes_info
        self.nodes: Dict[int, Node] = {}
        self.root: Optional[Node] = None

    def _instantiate_nodes(self):
        for node_id, _, _ in self.nodes_info:
            self.nodes[node_id] = Node(node_id)

    def _link_nodes(self):
        # Track children to find root later
        children = set()
        for node_id, left_id, right_id in self.nodes_info:
            node = self.nodes[node_id]
            if left_id != -1:
                node.left = self.nodes[left_id]
                children.add(left_id)
            if right_id != -1:
                node.right = self.nodes[right_id]
                children.add(right_id)
        candidates = set(self.nodes.keys()) - children
        # Assume one root
        if len(candidates) != 1:
            raise ValueError(f"Invalid tree structure: expected single root but got {candidates}")
        self.root = self.nodes[candidates.pop()]

    def build(self) -> Node:
        self._instantiate_nodes()
        self._link_nodes()
        return self.root


class TreeWalkStrategy(ABC):
    @abstractmethod
    def walk(self, node: Optional[Node]) -> List[int]:
        pass


class PreorderWalk(TreeWalkStrategy):
    def walk(self, node: Optional[Node]) -> List[int]:
        if node is None:
            return []
        # Preorder: root, left, right
        return [node.id] + self.walk(node.left) + self.walk(node.right)


class InorderWalk(TreeWalkStrategy):
    def walk(self, node: Optional[Node]) -> List[int]:
        if node is None:
            return []
        # Inorder: left, root, right
        return self.walk(node.left) + [node.id] + self.walk(node.right)


class PostorderWalk(TreeWalkStrategy):
    def walk(self, node: Optional[Node]) -> List[int]:
        if node is None:
            return []
        # Postorder: left, right, root
        return self.walk(node.left) + self.walk(node.right) + [node.id]


class TreeWalkContext:
    def __init__(self, strategy: TreeWalkStrategy):
        self.strategy = strategy

    def execute(self, tree_root: Optional[Node]) -> List[int]:
        return self.strategy.walk(tree_root)


class InputReader:
    @staticmethod
    def read_input() -> Tuple[int, List[Tuple[int, int, int]]]:
        n = int(input())
        nodes_info = []
        for _ in range(n):
            parts = input().strip().split()
            if len(parts) != 3:
                raise ValueError("Invalid node description, expected exactly three integers per line.")
            node_id, left, right = map(int, parts)
            nodes_info.append((node_id, left, right))
        return n, nodes_info


class Solution:
    def __init__(self, n: int, nodes_info: List[Tuple[int, int, int]]):
        self.n = n
        self.nodes_info = nodes_info
        self.tree_root: Optional[Node] = None

    def prepare_tree(self):
        builder = TreeBuilder(self.nodes_info)
        self.tree_root = builder.build()

    def perform_walks(self) -> List[Tuple[str, List[int]]]:
        walks = []
        for name, strategy in [('Preorder', PreorderWalk()), ('Inorder', InorderWalk()), ('Postorder', PostorderWalk())]:
            context = TreeWalkContext(strategy)
            result = context.execute(self.tree_root)
            walks.append((name, result))
        return walks

    def print_results(self, walks: List[Tuple[str, List[int]]]):
        for name, traversal in walks:
            print(name)
            print(" " + " ".join(str(node_id) for node_id in traversal))


def main():
    n, nodes_info = InputReader.read_input()
    solution = Solution(n, nodes_info)
    solution.prepare_tree()
    walks = solution.perform_walks()
    solution.print_results(walks)


if __name__ == "__main__":
    main()