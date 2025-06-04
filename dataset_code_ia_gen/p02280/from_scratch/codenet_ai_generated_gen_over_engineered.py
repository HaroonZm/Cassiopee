class TreeNode:
    __slots__ = ['id', 'left', 'right', 'parent', 'depth', 'height']

    def __init__(self, node_id: int):
        self.id = node_id
        self.left = None  # type: TreeNode | None
        self.right = None  # type: TreeNode | None
        self.parent = None  # type: TreeNode | None
        self.depth = -1
        self.height = -1


class BinaryTree:
    def __init__(self, n: int):
        self.n = n
        self.nodes = {i: TreeNode(i) for i in range(n)}
        self.root = None

    def add_children(self, node_id: int, left_id: int, right_id: int):
        node = self.nodes[node_id]
        if left_id != -1:
            left_node = self.nodes[left_id]
            node.left = left_node
            left_node.parent = node
        if right_id != -1:
            right_node = self.nodes[right_id]
            node.right = right_node
            right_node.parent = node

    def find_root(self):
        for node in self.nodes.values():
            if node.parent is None:
                self.root = node
                return

    def compute_depths(self):
        def dfs_depth(node: TreeNode, d: int):
            node.depth = d
            if node.left:
                dfs_depth(node.left, d + 1)
            if node.right:
                dfs_depth(node.right, d + 1)

        if self.root:
            dfs_depth(self.root, 0)

    def compute_heights(self):
        def dfs_height(node: TreeNode) -> int:
            if node is None:
                return -1
            left_h = dfs_height(node.left) if node.left else -1
            right_h = dfs_height(node.right) if node.right else -1
            node.height = 1 + max(left_h, right_h)
            return node.height

        if self.root:
            dfs_height(self.root)

    def sibling_id(self, node: TreeNode) -> int:
        if node.parent is None:
            return -1
        p = node.parent
        if p.left and p.right:
            return p.left.id if p.right == node else p.right.id
        return -1

    def degree(self, node: TreeNode) -> int:
        deg = 0
        if node.left is not None:
            deg += 1
        if node.right is not None:
            deg += 1
        return deg

    def node_type(self, node: TreeNode) -> str:
        if node.parent is None:
            return "root"
        deg = self.degree(node)
        if deg == 0:
            return "leaf"
        return "internal node"

    def print_nodes_info(self):
        for i in range(self.n):
            node = self.nodes[i]
            p = node.parent.id if node.parent else -1
            s = self.sibling_id(node)
            deg = self.degree(node)
            dep = node.depth
            h = node.height
            t = self.node_type(node)
            print(f"node {node.id}: parent = {p}, sibling = {s}, degree = {deg}, depth = {dep}, height = {h}, {t}")


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    tree = BinaryTree(n)
    for _ in range(n):
        node_id, left_id, right_id = map(int, input().split())
        tree.add_children(node_id, left_id, right_id)
    tree.find_root()
    tree.compute_depths()
    tree.compute_heights()
    tree.print_nodes_info()


if __name__ == "__main__":
    main()