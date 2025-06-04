import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, x):
        node = Node(x)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def delete(self, x):
        cur = self.head
        while cur:
            if cur.key == x:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    # cur is head
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    # cur is tail
                    self.tail = cur.prev
                break
            cur = cur.next

    def deleteFirst(self):
        if self.head:
            nxt = self.head.next
            if nxt:
                nxt.prev = None
            else:
                self.tail = None
            self.head = nxt

    def deleteLast(self):
        if self.tail:
            prv = self.tail.prev
            if prv:
                prv.next = None
            else:
                self.head = None
            self.tail = prv

    def get_all_keys(self):
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.key))
            cur = cur.next
        return res

n = int(input())
dll = DoublyLinkedList()

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        dll.insert(int(cmd[1]))
    elif cmd[0] == 'delete':
        dll.delete(int(cmd[1]))
    elif cmd[0] == 'deleteFirst':
        dll.deleteFirst()
    elif cmd[0] == 'deleteLast':
        dll.deleteLast()

print(' '.join(dll.get_all_keys()))