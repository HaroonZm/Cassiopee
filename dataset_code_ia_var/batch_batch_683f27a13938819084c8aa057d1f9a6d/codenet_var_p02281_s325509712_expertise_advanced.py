from dataclasses import dataclass
from typing import List, Optional

@dataclass(frozen=True, slots=True)
class Node:
    node_id: int
    left: int
    right: int

    def pre_order(self, nodes: List[Optional['Node']], visit: list):
        visit.append(str(self.node_id))
        if self.left != -1:
            nodes[self.left].pre_order(nodes, visit)
        if self.right != -1:
            nodes[self.right].pre_order(nodes, visit)

    def in_order(self, nodes: List[Optional['Node']], visit: list):
        if self.left != -1:
            nodes[self.left].in_order(nodes, visit)
        visit.append(str(self.node_id))
        if self.right != -1:
            nodes[self.right].in_order(nodes, visit)

    def post_order(self, nodes: List[Optional['Node']], visit: list):
        if self.left != -1:
            nodes[self.left].post_order(nodes, visit)
        if self.right != -1:
            nodes[self.right].post_order(nodes, visit)
        visit.append(str(self.node_id))

def main():
    n = int(input())
    nodes = [None]*n
    has_parent = [False]*n

    for _ in range(n):
        node_id, left, right = map(int, input().split())
        nodes[node_id] = Node(node_id, left, right)
        if left != -1: has_parent[left] = True
        if right != -1: has_parent[right] = True

    root = has_parent.index(False)

    traversals = [
        ('Preorder', Node.pre_order),
        ('Inorder', Node.in_order),
        ('Postorder', Node.post_order)
    ]

    for name, method in traversals:
        print(name)
        visit = []
        method(nodes[root], nodes, visit)
        print(' ' + ''.join(visit))

if __name__ == '__main__':
    main()