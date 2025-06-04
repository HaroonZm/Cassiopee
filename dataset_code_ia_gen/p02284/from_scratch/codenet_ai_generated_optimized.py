import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

class Node:
    __slots__ = ['key','left','right']
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,key):
        if self.root is None:
            self.root=Node(key)
            return
        cur=self.root
        while True:
            if key < cur.key:
                if cur.left is None:
                    cur.left=Node(key)
                    return
                cur=cur.left
            else:
                if cur.right is None:
                    cur.right=Node(key)
                    return
                cur=cur.right

    def find(self,key):
        cur=self.root
        while cur:
            if key==cur.key:
                return True
            elif key < cur.key:
                cur=cur.left
            else:
                cur=cur.right
        return False

    def inorder(self,node,res):
        if node is None:
            return
        self.inorder(node.left,res)
        res.append(node.key)
        self.inorder(node.right,res)

    def preorder(self,node,res):
        if node is None:
            return
        res.append(node.key)
        self.preorder(node.left,res)
        self.preorder(node.right,res)

bst=BST()
m=int(input())
for _ in range(m):
    cmd=input().split()
    if cmd[0]=='insert':
        bst.insert(int(cmd[1]))
    elif cmd[0]=='find':
        print('yes' if bst.find(int(cmd[1])) else 'no')
    else:
        inorder_res=[]
        preorder_res=[]
        bst.inorder(bst.root,inorder_res)
        bst.preorder(bst.root,preorder_res)
        print(' '+' '.join(map(str,inorder_res)))
        print(' '+' '.join(map(str,preorder_res)))