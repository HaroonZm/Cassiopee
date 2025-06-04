from heapq import *

st = input()
uniq_chars = list(set(st))

# Initial heap construction
a = []
for ch in uniq_chars:
    a.append((st.count(ch), ch))
heapify(a)

# Node dictionary and parent mapping
class Node:
    def __init__(self, key, char=None):
        self.key = key
        self.char = char
        self.pare = None

nodes = {}
for cnt, ch in a:
    n = Node(cnt, ch)
    nodes[ch] = n

root = None
while len(a) > 1:
    p1, p2 = heappop(a)
    q1, q2 = heappop(a)
    newkey = p1 + q1
    newchar = p2 + q2
    x = Node(newkey, newchar)
    nodes[newchar] = x
    nodes[p2].pare = x
    nodes[q2].pare = x
    if len(a) == 0:
        root = x
        break
    heappush(a, (newkey, newchar))
if len(a) == 1 and root is None:
    root = nodes[a[0][1]]

Sum = 0
for ch in uniq_chars:
    n = nodes[ch]
    cnt = 1
    cur = n
    while cur.pare is not None:
        cnt += 1
        cur = cur.pare
    Sum += cnt * n.key
print(Sum)