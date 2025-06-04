from typing import List

class Node:
    __slots__ = ("prev", "next", "data")
    def __init__(self, prev, nxt, val):
        self.prev=prev
        self.next=nxt
        self.data=val

def add_front(val, node):
    tmp = Node(node.prev, node, val)
    if node.prev: node.prev.next = tmp
    node.prev = tmp
    return tmp

def jump(steps, cursor):
    index = 0
    while abs(index) < abs(steps):
        if steps > 0:
            cursor = cursor.next
            index += 1
        else:
            cursor = cursor.prev
            index -= 1
    return cursor

def remove(node):
    p, n = node.prev, node.next
    if p: p.next = n
    if n: n.prev = p
    return n

if __name__=='__main__':
    n=int(input())
    Sentinel=None
    root = Node(Sentinel, Sentinel, None)
    dummy = Node(root, Sentinel, None)
    root.next = dummy
    cur=dummy

    # Processing commands, mixing functional and imperative style
    for __ in range(n):
        parts = list(map(int, input().split()))
        op, *args = parts
        if op==0:
            cur = add_front(args[0], cur)
        elif op==1:
            cur = jump(args[0], cur)
        elif op==2:
            cur = remove(cur)
    # Collect results in a plain loop
    res = []
    temp = root.next
    while temp and temp.next:
        res.append(temp.data)
        temp = temp.next
    list(map(print, res))