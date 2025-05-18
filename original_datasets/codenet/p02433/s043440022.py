from typing import List

class Node:
    __slots__ = ['prev', 'next', 'data']

    def __init__(self, prev, next, data) -> None:
        self.prev = prev
        self.next = next
        self.data = data

def insert(x: int, cur: Node) -> Node:
    cur.prev.next = cur.prev = cur = Node(cur.prev, cur, x)
    return cur

def move(x: int, cur: Node) -> Node:
    if x > 0:
        for _ in range(x):
            cur = cur.next
    else:
        for _ in range(-x):
            cur = cur.prev
    return cur

def erase(cur: Node) -> Node:
    cur.next.prev = cur.prev
    cur.prev.next = cur = cur.next
    return cur

if __name__ == "__main__":
    num_query = int(input())
    root = Node(None, None, None)
    cur = root.next = Node(root, None, None)

    for _ in range(num_query):
        op, *value = map(lambda x: int(x), input().split())
        if (0 == op):
            cur = insert(value[0], cur)
        elif (1 == op):
            cur = move(value[0], cur)
        elif (2 == op):
            cur = erase(cur)
        else:
            pass

    ans: List[int] = []
    it = root.next
    while it.next:
        ans.append(it.data)
        it = it.next

    for elem in ans:
        print(elem)