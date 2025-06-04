class TreeNode:
    __slots__ = ['key', 'left', 'right']

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AbstractTraversalStrategy:
    def traverse(self, root):
        raise NotImplementedError("Traversal strategy must implement traverse method")


class InorderTraversal(AbstractTraversalStrategy):
    def traverse(self, root):
        return list(self._inorder_gen(root))

    def _inorder_gen(self, node):
        if node is not None:
            yield from self._inorder_gen(node.left)
            yield node.key
            yield from self._inorder_gen(node.right)


class PreorderTraversal(AbstractTraversalStrategy):
    def traverse(self, root):
        return list(self._preorder_gen(root))

    def _preorder_gen(self, node):
        if node is not None:
            yield node.key
            yield from self._preorder_gen(node.left)
            yield from self._preorder_gen(node.right)


class BinarySearchTree:
    def __init__(self, traversal_strategies=None):
        self.root = None
        # Support multiple traversal strategies to enable extension.
        self._traversal_strategies = traversal_strategies or {
            'inorder': InorderTraversal(),
            'preorder': PreorderTraversal()
        }

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        # else: keys are distinct so no equal case needed
        return node

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        while node is not None:
            if key == node.key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def print_traversal(self):
        # Generate outputs from traversal strategies in defined order
        inorder_keys = self._traversal_strategies['inorder'].traverse(self.root)
        preorder_keys = self._traversal_strategies['preorder'].traverse(self.root)
        print(' ' + ' '.join(str(k) for k in inorder_keys))
        print(' ' + ' '.join(str(k) for k in preorder_keys))


class Command(ABC):
    @abstractmethod
    def execute(self, bst: BinarySearchTree):
        pass


class InsertCommand(Command):
    def __init__(self, key):
        self.key = key

    def execute(self, bst: BinarySearchTree):
        bst.insert(self.key)


class FindCommand(Command):
    def __init__(self, key):
        self.key = key

    def execute(self, bst: BinarySearchTree):
        print("yes" if bst.find(self.key) else "no")


class PrintCommand(Command):
    def execute(self, bst: BinarySearchTree):
        bst.print_traversal()


class CommandFactory:
    @staticmethod
    def create_command(parts):
        if parts[0] == 'insert':
            return InsertCommand(int(parts[1]))
        elif parts[0] == 'find':
            return FindCommand(int(parts[1]))
        elif parts[0] == 'print':
            return PrintCommand()
        else:
            raise ValueError("Invalid command")


def main():
    import sys
    import threading

    # Use threading to increase recursion limit and stack size for deep recursions
    sys.setrecursionlimit(10**7)
    threading.stack_size(1 << 27)

    def run():
        m = int(sys.stdin.readline())
        bst = BinarySearchTree()
        for _ in range(m):
            line = sys.stdin.readline().strip()
            parts = line.split()
            cmd = CommandFactory.create_command(parts)
            cmd.execute(bst)

    threading.Thread(target=run).start()


from abc import ABC, abstractmethod
main()