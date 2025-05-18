MAX = 10000
NIL = -1

class Node:
    def __init__(self):
        self.parent = NIL
        self.left = 0
        self.right = 0

# ノード毎の深さ
D = [None for i in range(MAX)]
# ノード毎の高さ
H = [None for i in range(MAX)]

# 深さセット
def setDepth(u,d):
    if u == NIL: return
    D[u] = d
    setDepth(T[u].left, d + 1)
    setDepth(T[u].right, d + 1)

# 高さセット
def setHeight(u):
    h1 = 0
    h2 = 0
    if T[u].left != NIL:
        h1 = setHeight(T[u].left)+1
    if T[u].right != NIL:
        h2 = setHeight(T[u].right)+1
    H[u] = max(h1,h2)
    return H[u]

# 兄弟取得
def getSibling(u):
    if T[u].parent == NIL:
        return NIL
    if T[T[u].parent].left != u and T[T[u].parent].left != NIL:
        return T[T[u].parent].left
    if T[T[u].parent].right != u and T[T[u].parent].right != NIL:
        return T[T[u].parent].right
    return NIL

n = int(input())

T = []
# n個のノードを用意
for loop in range(n):
    node = Node()
    T.append(node)

def printNode(u):
    deg = 0
    if T[u].left != NIL:
        deg += 1
    if T[u].right != NIL:
        deg += 1
    print("node %d: parent = %d, sibling = %d, degree = %d, depth = %d, height = %d, "%(u, T[u].parent,  getSibling(u), deg, D[u], H[u]),end = "")

    if T[u].parent == NIL:
        print("root")
    elif T[u].left == NIL and T[u].right == NIL:
        print("leaf")
    else:
        print("internal node")

for i in range(n):
    v,l,r = map(int,input().split())
    T[v].left = l
    T[v].right = r
    if l != NIL:
        T[l].parent = v
    if r != NIL:
        T[r].parent = v

for i in range(n):
    if T[i].parent == NIL:
        root = i
        setDepth(root,0)
        setHeight(root)

for i in range(n):
    printNode(i)