class Node:

    def __init__(self, key: int) -> None:
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def input_line() -> (str, int):
    line = input().split()
    if line[0] == 'insert':
        return line[0], int(line[1])
    elif line[0] == 'find':
        return line[0], int(line[1])
    else:
        return line[0], None

def preorder(tree: Node) -> None:
    """先行順巡回。"""
    print(f' {tree.key}', end='')
    if tree.left is not None:
        preorder(tree.left)
    if tree.right is not None:
        preorder(tree.right)

def inorder(tree: Node) -> None:
    """中間順巡回。"""
    if tree.left is not None:
        inorder(tree.left)
    print(f' {tree.key}', end='')
    if tree.right is not None:
        inorder(tree.right)

def insert(new_node: Node) -> None:
    """二分探索木に挿入する。"""

    # rootはglobalに共有する。
    global root

    # new_nodeを付け加える節(parent)の初期値をNoneに設定する。
    parent = None

    # tmpにrootを設定する。
    tmp = root

    # new_nodeを付け加える節(parent)を探索する。
    while tmp is not None:
        parent = tmp
        if new_node.key < tmp.key:
            tmp = tmp.left
        else:
            tmp = tmp.right

    # new_nodeの親を設定する。
    new_node.parent = parent

    # new_nodeの子供を設定する。
    if parent is None:
        # treeが空だった場合は、rootにnew_nodeを設定する。
        root = new_node
    elif new_node.key < parent.key:
        parent.left = new_node
    else:
        parent.right = new_node

def find(key)-> bool:

    global root

    # tmpにrootを設定する。
    tmp = root

    # new_nodeを付け加える節(parent)を探索する。
    while tmp is not None:
        if key == tmp.key:
            return True
        elif key < tmp.key:
            tmp = tmp.left
        else:
            tmp = tmp.right

    return False

root = None  # treeの根を表す。初期値はNone。
N = int(input())
for _i in range(N):
    order, val = input_line()
    if order == 'insert':
        node = Node(val)
        insert(node)
    elif order == 'print':
        inorder(root)
        print()
        preorder(root)
        print()
    elif order == 'find':
        if find(val):
            print('yes')
        else:
            print('no')