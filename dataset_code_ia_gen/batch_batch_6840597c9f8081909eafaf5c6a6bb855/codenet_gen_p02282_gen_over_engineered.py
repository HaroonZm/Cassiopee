class TreeTraversal:
    """Abstract base class for tree traversal strategies."""
    def traverse(self, tree):
        raise NotImplementedError("Subclasses should implement this!")

class PreorderTraversal(TreeTraversal):
    def traverse(self, tree):
        return self._preorder(tree.root)
    
    def _preorder(self, node):
        if node is None:
            return []
        return [node.value] + self._preorder(node.left) + self._preorder(node.right)

class InorderTraversal(TreeTraversal):
    def traverse(self, tree):
        return self._inorder(tree.root)
    
    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

class PostorderTraversal(TreeTraversal):
    def traverse(self, tree):
        return self._postorder(tree.root)
    
    def _postorder(self, node):
        if node is None:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.value]

class Node:
    __slots__ = ('value', 'left', 'right')
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

class TreeBuilder:
    """Abstract base builder for tree reconstruction"""
    def build(self, preorder, inorder):
        raise NotImplementedError("Subclasses should implement this!")

class BinaryTreeBuilder(TreeBuilder):
    def build(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root_value = preorder[0]
        root = Node(root_value)
        root_index_in_inorder = inorder.index(root_value)
        left_inorder = inorder[:root_index_in_inorder]
        right_inorder = inorder[root_index_in_inorder+1:]
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        root.left = self.build(left_preorder, left_inorder)
        root.right = self.build(right_preorder, right_inorder)
        return root

class TreeReconstructor:
    def __init__(self, builder: TreeBuilder):
        self.builder = builder

    def reconstruct(self, preorder, inorder):
        tree = Tree()
        tree.root = self.builder.build(preorder, inorder)
        return tree

class InputReader:
    """Reads and parses input from standard input."""
    @staticmethod
    def read_input():
        n = int(input().strip())
        preorder = list(map(int, input().strip().split()))
        inorder = list(map(int, input().strip().split()))
        assert len(preorder) == n and len(inorder) == n
        return n, preorder, inorder

class OutputWriter:
    """Handles output formatting and printing."""
    @staticmethod
    def write_postorder(sequence):
        print(' '.join(map(str, sequence)))

class TreeWalkApp:
    def __init__(self):
        self.builder = BinaryTreeBuilder()
        self.reconstructor = TreeReconstructor(self.builder)
        self.postorder_traversal = PostorderTraversal()

    def run(self):
        n, preorder, inorder = InputReader.read_input()
        tree = self.reconstructor.reconstruct(preorder, inorder)
        postorder_sequence = self.postorder_traversal.traverse(tree)
        OutputWriter.write_postorder(postorder_sequence)

if __name__ == '__main__':
    app = TreeWalkApp()
    app.run()