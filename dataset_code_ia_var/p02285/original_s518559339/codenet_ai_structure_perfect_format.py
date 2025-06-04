class Node(object):
    root = None

    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = None

    @classmethod
    def insert(cls, z):
        y = None
        x = cls.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            cls.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    @classmethod
    def find(cls, k):
        x = cls.root
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    @classmethod
    def walk_preorder(cls, node):
        print(' {0}'.format(node.key), end='')
        if node.left is not None:
            cls.walk_preorder(node.left)
        if node.right is not None:
            cls.walk_preorder(node.right)

    @classmethod
    def walk_inorder(cls, node):
        if node.left is not None:
            cls.walk_inorder(node.left)
        print(' {0}'.format(node.key), end='')
        if node.right is not None:
            cls.walk_inorder(node.right)

    @classmethod
    def delete_node(cls, z):
        if z is None:
            return
        if z.left is None or z.right is None:
            y = z
        else:
            y = Node.get_successor(z)
        if y.left is not None:
            x = y.left
        else:
            x = y.right
        if x is not None:
            x.parent = y.parent
        if y.parent is None:
            Node.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        if y != z:
            z.key = y.key

    @classmethod
    def get_successor(cls, x):
        if x.right is not None:
            return Node.get_minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    @classmethod
    def get_minimum(cls, x):
        while x.left is not None:
            x = x.left
        return x

    def get_type(self):
        if self.parent is None:
            return 'root'
        elif self.left is None and self.right is None:
            return 'leaf'
        else:
            return 'internal node'

    def get_depth(self):
        if self.parent is None:
            return 0
        else:
            depth = 1
            t = self.parent
            while t.parent is not None:
                t = t.parent
                depth += 1
            return depth

    def get_height(self):
        if self.height is not None:
            return self.height
        h_left = 0
        h_right = 0
        if self.left is not None:
            h_left = self.left.get_height() + 1
        if self.right is not None:
            h_right = self.right.get_height() + 1
        self.height = max(h_left, h_right)
        return self.height

    def get_degree(self):
        degree = 0
        if self.left is not None:
            degree += 1
        if self.right is not None:
            degree += 1
        return degree

    def get_sibling(self):
        if self.parent is None:
            return -1
        p = self.parent
        if p.left is not self and p.left is not None:
            return p.left
        if p.right is not self and p.right is not None:
            return p.right

def process_node_data(node_data):
    for inst in node_data:
        if inst[0] == 'print':
            Node.walk_inorder(Node.root)
            print('')
            Node.walk_preorder(Node.root)
            print('')
        elif inst[0] == 'insert':
            node_key = int(inst[1])
            new_node = Node(node_key)
            Node.insert(new_node)
        elif inst[0] == 'find':
            result = Node.find(int(inst[1]))
            if result:
                print('yes')
            else:
                print('no')
        elif inst[0] == 'delete':
            Node.delete_node(Node.find(int(inst[1])))

def flatten(l):
    import collections
    for el in l:
        if isinstance(el, collections.abc.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

if __name__ == '__main__':
    num_of_nodes = int(input())
    node_data = [input().split(' ') for _ in range(num_of_nodes)]
    process_node_data(node_data)