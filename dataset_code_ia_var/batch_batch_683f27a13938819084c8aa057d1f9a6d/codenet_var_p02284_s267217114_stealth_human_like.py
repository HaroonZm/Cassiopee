class Node:
    # Simple node for BST - not much fancy here.
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def input_line():
    # Reads input like "insert 8"
    chunks = input().split()
    cmd = chunks[0]
    if cmd == "insert":
        return cmd, int(chunks[1])
    elif cmd == "find":
        # Should always have second part... I guess.
        return cmd, int(chunks[1])
    else:
        # Presume 'print' or something else with no num
        return cmd, None

def preorder(node):  # root, left, right
    # I just like preorder more sometimes
    if node is None:
        return
    print(" {}".format(node.key), end='') # hope this format is fine
    # left first
    preorder(node.left)
    # right after
    preorder(node.right)

def inorder(node):  # left, root, right
    if node:
        inorder(node.left)
        print(' {}'.format(node.key), end='')
        inorder(node.right)
    # nothing fancy

def insert(new_node):
    # BST insert, probably not the best way but works
    global root
    y = None  # will be parent of x
    x = root
    while x is not None:
        y = x
        if new_node.key < x.key:
            x = x.left
        else:
            x = x.right
    new_node.parent = y
    # Place new_node where we found null
    if y is None:
        root = new_node   # tree was empty
    elif new_node.key < y.key:
        y.left = new_node
    else:
        y.right = new_node
    # Done, but no balancing or anything like that

def find(key):
    # Looks for the key, returns True if found else False
    global root
    current = root
    while current is not None:
        if current.key == key:
            return True
        elif key < current.key:
            current = current.left
        else:
            current = current.right
    return False  # didn't find it

root = None   # start with empty tree

N = int(input())
for _ in range(N):
    cmd, value = input_line()
    if cmd == 'insert':
        n = Node(value)
        insert(n)
    elif cmd == 'print':
        inorder(root)
        print()
        preorder(root)
        print()
    elif cmd == 'find':
        if find(value):
            print("yes")
        else:
            print("no")
    # else: could maybe warn, but assuming only correct commands come in