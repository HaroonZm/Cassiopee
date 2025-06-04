import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

class Node:
    __slots__ = ['key', 'priority', 'left', 'right']
    def __init__(self,key,priority):
        self.key=key
        self.priority=priority
        self.left=None
        self.right=None

def rightRotate(t):
    s=t.left
    t.left=s.right
    s.right=t
    return s

def leftRotate(t):
    s=t.right
    t.right=s.left
    s.left=t
    return s

def insert(t,key,priority):
    if t is None:
        return Node(key,priority)
    if key==t.key:
        return t
    if key<t.key:
        t.left=insert(t.left,key,priority)
        if t.priority < t.left.priority:
            t=rightRotate(t)
    else:
        t.right=insert(t.right,key,priority)
        if t.priority < t.right.priority:
            t=leftRotate(t)
    return t

def find(t,key):
    while t:
        if key==t.key:
            return True
        if key<t.key:
            t=t.left
        else:
            t=t.right
    return False

def _delete(t,key):
    if t.left is None and t.right is None:
        return None
    if t.left is None:
        t=leftRotate(t)
    elif t.right is None:
        t=rightRotate(t)
    else:
        if t.left.priority > t.right.priority:
            t=rightRotate(t)
        else:
            t=leftRotate(t)
    return delete(t,key)

def delete(t,key):
    if t is None:
        return None
    if key < t.key:
        t.left=delete(t.left,key)
    elif key > t.key:
        t.right=delete(t.right,key)
    else:
        return _delete(t,key)
    return t

def inorder(t,res):
    if t:
        inorder(t.left,res)
        res.append(t.key)
        inorder(t.right,res)

def preorder(t,res):
    if t:
        res.append(t.key)
        preorder(t.left,res)
        preorder(t.right,res)

m=int(input())
root=None
out=[]
for _ in range(m):
    cmd,*args=input().split()
    if cmd=="insert":
        k,p= int(args[0]),int(args[1])
        root=insert(root,k,p)
    elif cmd=="find":
        k=int(args[0])
        out.append("yes" if find(root,k) else "no")
    elif cmd=="delete":
        k=int(args[0])
        root=delete(root,k)
    else:
        res_in=[]
        res_pre=[]
        inorder(root,res_in)
        preorder(root,res_pre)
        out.append(" "+" ".join(map(str,res_in)))
        out.append(" "+" ".join(map(str,res_pre)))
print("\n".join(out))