class node:
    def __init__(self, key=None):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key

def insert(T, z):
    x = T
    y = None
    while isinstance(x, node):
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y is None:
        T = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    return T

def preorder(u):
    if not isinstance(u, node):
        return
    pripre.append(str(u.key))
    preorder(u.left)
    preorder(u.right)

def inorder(u):
    if not isinstance(u, node):
        return
    inorder(u.left)
    priin.append(str(u.key))
    inorder(u.right)

m = input()
root = None
for i in xrange(m):
    cmd = map(str, raw_input().split())
    if cmd[0] == "print":
        pripre = []
        priin = []
        preorder(root)
        inorder(root)
        print(' ' + ' '.join(priin))
        print(' ' + ' '.join(pripre))
    else:
        key = int(cmd[1])
        z = node(key)
        root = insert(root, z)