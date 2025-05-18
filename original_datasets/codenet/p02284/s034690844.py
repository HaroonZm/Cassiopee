class BinarySearchTree(object):
    __slots__ = ['root']

    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = [key, None, None]

        if self.root is None:
            self.root = new_node
            return

        parent, child = None, self.root
        while child:
            parent = child
            child = child[1] if key < child[0] else child[2]

        if key < parent[0]:
            parent[1] = new_node
        else:
            parent[2] = new_node

    def find(self, key):
        current = self.root
        while current and current[0] != key:
            current = current[1] if key < current[0] else current[2]

        return current

    def walk(self, walk_type):
        a = []
        self._walk(self.root, a, walk_type)
        return a

    def _walk(self, node, a, walk_type):
        if walk_type == 0:
            a.append(node[0])
        if node[1]:
            self._walk(node[1], a, walk_type)
        if walk_type == 1:
            a.append(node[0])
        if node[2]:
            self._walk(node[2], a, walk_type)

if __name__ == '__main__':
    import sys
    input()
    tree = BinarySearchTree()

    for cmd in (l.split() for l in sys.stdin):
        if cmd[0] == 'insert':
            tree.insert(int(cmd[1]))
        elif cmd[0] == 'find':
            print('yes' if tree.find(int(cmd[1])) else 'no')
        else:
            print('', *tree.walk(1))
            print('', *tree.walk(0))