class List:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def insert(self, value):
        node = self.__class__(value)
        node.prev, node.next = self.prev, self
        if self.prev is not None:
            self.prev.next = node
        self.prev = node
        return node

    def delete(self):
        p, n = self.prev, self.next
        self.prev, self.next = None, None
        if p is None:
            n.prev = None
        else:
            n.prev, p.next = p, n
        return n

    def move(self, i):
        node = self
        if i > 0:
            for _ in range(i):
                node = node.next
        else:
            for _ in range(-i):
                node = node.prev
        return node

    def __iter__(self):
        return List.ListIterator(self)

    class ListIterator:
        def __init__(self, node):
            while node.prev is not None:
                node = node.prev
            self.node = node

        def __iter__(self):
            return self

        def __next__(self):
            val = self.node.value
            if val is None:
                raise StopIteration
            self.node = self.node.next
            return val

def run():
    n = int(input())
    li = List()

    for _ in range(n):
        command = input()
        if command.startswith('0'):
            li = li.insert(int(command[2:]))
        elif command.startswith('1'):
            li = li.move(int(command[2:]))
        elif command.startswith('2'):
            li = li.delete()
        else:
            raise ValueError('invalid command')

    for v in li:
        print(v)

if __name__ == '__main__':
    run()