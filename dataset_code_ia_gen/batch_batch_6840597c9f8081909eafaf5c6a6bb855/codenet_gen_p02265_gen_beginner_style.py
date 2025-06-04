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
        new_node = Node(x)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def delete(self, x):
        current = self.head
        while current is not None:
            if current.key == x:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                break
            current = current.next

    def deleteFirst(self):
        if self.head is not None:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None

    def deleteLast(self):
        if self.tail is not None:
            if self.tail.prev is not None:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None

    def printList(self):
        current = self.head
        keys = []
        while current is not None:
            keys.append(str(current.key))
            current = current.next
        print(" ".join(keys))

n = int(input())
dll = DoublyLinkedList()
for _ in range(n):
    command = input().split()
    if command[0] == "insert":
        dll.insert(int(command[1]))
    elif command[0] == "delete":
        dll.delete(int(command[1]))
    elif command[0] == "deleteFirst":
        dll.deleteFirst()
    elif command[0] == "deleteLast":
        dll.deleteLast()

dll.printList()