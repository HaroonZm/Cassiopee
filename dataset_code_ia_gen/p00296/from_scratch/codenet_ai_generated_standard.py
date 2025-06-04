import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class Node:
    __slots__ = ["prev", "next", "num"]
    def __init__(self, num):
        self.num = num
        self.prev = None
        self.next = None

N,M,Q = map(int,input().split())
a = list(map(int,input().split()))
q = list(map(int,input().split()))

nodes = [Node(i) for i in range(N)]
for i in range(N):
    nodes[i].next = nodes[(i+1)%N]
    nodes[i].prev = nodes[(i-1)%N]

current = nodes[0]

for x in a:
    if x%2==0:
        # clock wise
        for _ in range(x):
            current = current.next
    else:
        # counter-clock wise
        for _ in range(x):
            current = current.prev
    # remove current (the x-th receiver)
    current.prev.next = current.next
    current.next.prev = current.prev
    current = current.next

alive = [0]*N
ptr = current
start = current
while True:
    alive[ptr.num] = 1
    ptr = ptr.next
    if ptr == start:
        break

for qq in q:
    print(alive[qq])