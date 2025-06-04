class Node:
    def __init__(self, key, left, right, parent):
        self.key = key
        self.left = left
        self.right = right
        self.p = parent

    def __repr__(self):
        return str(self.key)

def insert(T, z):
    y = None
    x = T
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is None:
        T = z
        print(T)
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def find(T, k, show):
    x = T
    while x is not None:
        if k == x.key:
            if show:
                print('yes')
            return x
        if k < x.key:
            x = x.left
        else:
            x = x.right
    print('no')

def getScu(x):
    if x.right is None:
        y = x.p
        while y is not None and x == y.right:
            x = y
            y = x.p
        return y
    x = x.right
    while x is not None:
        y = x
        x = x.left
    return y

def delete(T, x):
    if x.left is None and x.right is None:
        if x.p.key < x.key:
            x.p.right = None
        else:
            x.p.left = None
    elif x.left is None:
        y = x.right
        x.key = y.key
        x.right = y.right
        x.left = y.left
    elif x.right is None:
        y = x.left
        x.key = y.key
        x.right = y.right
        x.left = y.left
    else:
        y = getScu(x)
        delete(T, y)
        x.key = y.key

def printPreorder(x):
    if x is None:
        return
    printPreorder(x.left)
    print(end=' ')
    print(x, end='')
    printPreorder(x.right)

def printMidorder(x):
    if x is None:
        return
    print(end=' ')
    print(x, end='')
    printMidorder(x.left)
    printMidorder(x.right)

def printal(x):
    printPreorder(x)
    print()
    printMidorder(x)
    print()

N = int(input())
Q = input().split()
T = Node(int(Q[1]), None, None, None)
for i in range(N - 1):
    Q = input().split()
    if Q[0] == "print":
        printal(T)
        continue
    elif Q[0] == "find":
        find(T, int(Q[1]), True)
        continue
    elif Q[0] == "delete":
        delete(T, find(T, int(Q[1]), False))
        continue
    insert(T, Node(int(Q[1]), None, None, None))