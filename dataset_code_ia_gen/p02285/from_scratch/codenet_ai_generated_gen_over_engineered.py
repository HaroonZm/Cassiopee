class BSTNode:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def minimum(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def successor(self):
        # Successor is the minimum key in the right subtree if exists
        if self.right is not None:
            return self.right.minimum()
        # Otherwise, go up to finds a node that is left child of its parent
        current = self
        parent = self.parent
        while parent is not None and current == parent.right:
            current = parent
            parent = parent.parent
        return parent


class BSTOperationStrategy:
    def execute(self, bst, *args, **kwargs):
        raise NotImplementedError()


class BSTInsertOperation(BSTOperationStrategy):
    def execute(self, bst, key):
        z = BSTNode(key)
        y = None  # parent trailing pointer
        x = bst.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            bst.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        bst.size += 1


class BSTFindOperation(BSTOperationStrategy):
    def execute(self, bst, key):
        node = bst.search_node(key)
        return node is not None


class BSTDeleteOperation(BSTOperationStrategy):
    def transplant(self, bst, u, v):
        if u.parent is None:
            bst.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def execute(self, bst, key):
        z = bst.search_node(key)
        if z is None:
            return
        if z.left is None:
            self.transplant(bst, z, z.right)
        elif z.right is None:
            self.transplant(bst, z, z.left)
        else:
            y = z.right.minimum()
            if y.parent != z:
                self.transplant(bst, y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(bst, z, y)
            y.left = z.left
            y.left.parent = y
        bst.size -= 1


class BSTPrintOperation(BSTOperationStrategy):
    def inorder_walk(self, node, result):
        if node is not None:
            self.inorder_walk(node.left, result)
            result.append(node.key)
            self.inorder_walk(node.right, result)

    def preorder_walk(self, node, result):
        if node is not None:
            result.append(node.key)
            self.preorder_walk(node.left, result)
            self.preorder_walk(node.right, result)

    def execute(self, bst):
        inorder_result = []
        self.inorder_walk(bst.root, inorder_result)
        preorder_result = []
        self.preorder_walk(bst.root, preorder_result)
        return inorder_result, preorder_result


class BSTBase:
    def __init__(self):
        self.root = None
        self.size = 0

    def search_node(self, key):
        current = self.root
        while current is not None and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current


class BinarySearchTree(BSTBase):
    def __init__(self):
        super().__init__()
        self.operations = {
            'insert': BSTInsertOperation(),
            'find': BSTFindOperation(),
            'delete': BSTDeleteOperation(),
            'print': BSTPrintOperation(),
        }

    def perform(self, cmd, arg=None):
        op = self.operations.get(cmd)
        if op is None:
            raise ValueError(f"Unsupported operation: {cmd}")
        if arg is None:
            return op.execute(self)
        else:
            return op.execute(self, arg)


class BSTController:
    def __init__(self, bst):
        self.bst = bst

    def handle_commands(self, inputs):
        output_lines = []
        for line in inputs:
            parts = line.strip().split()
            cmd = parts[0]
            arg = int(parts[1]) if len(parts) > 1 else None
            if cmd == 'insert':
                self.bst.perform('insert', arg)
            elif cmd == 'find':
                found = self.bst.perform('find', arg)
                output_lines.append("yes" if found else "no")
            elif cmd == 'delete':
                self.bst.perform('delete', arg)
            elif cmd == 'print':
                inorder, preorder = self.bst.perform('print')
                output_lines.append(' ' + ' '.join(map(str, inorder)))
                output_lines.append(' ' + ' '.join(map(str, preorder)))
            else:
                # Gracefully handle unexpected commands if any
                pass
        return output_lines


def main():
    import sys

    input = sys.stdin.readline
    m = int(input())
    bst = BinarySearchTree()
    controller = BSTController(bst)

    commands = [input() for _ in range(m)]
    result = controller.handle_commands(commands)
    print('\n'.join(result))


if __name__ == '__main__':
    main()