from heapq import heappush, heappop
from collections import Counter

S = input()
d = Counter(S)
tree_dic = {}
h = []
num = 0

class Node:
    def __init__(self, weight):
        self.weight = weight
        self.parent = None
    def __lt__(self, other):
        return self.weight < other.weight

for i in d:
    node = Node(d[i])
    tree_dic[i] = node
    heappush(h, node)

while len(h) > 1:
    tmp0 = heappop(h)
    tmp1 = heappop(h)
    parent = Node(tmp0.weight + tmp1.weight)
    tmp0.parent = parent
    tmp1.parent = parent
    tree_dic[num] = parent
    heappush(h, parent)
    num += 1

ans = 0
length_cache = {}

for i in S:
    node = tree_dic[i]
    count = 0
    if id(node) in length_cache:
        count = length_cache[id(node)]
    else:
        tmp_node = node
        while True:
            if getattr(tmp_node, 'parent', None) is not None:
                count += 1
                tmp_node = tmp_node.parent
            else:
                break
        length_cache[id(node)] = count
    ans += count

if len(S) == 1:
    print(1)
elif len(d) == 1:
    print(len(S))
else:
    print(ans)