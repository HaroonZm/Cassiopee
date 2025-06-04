import heapq
from collections import Counter

text = input()
counter = Counter(text)
heap = []
for char, freq in counter.items():
    node = type('HuffmanTreeNode', (), {})()
    node.char = char
    node.freq = freq
    node.left = None
    node.right = None
    heap.append(node)

def node_lt(self, other):
    return self.freq < other.freq
for node in heap:
    node.__class__.__lt__ = node_lt

heapq.heapify(heap)
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    parent = type('HuffmanTreeNode', (), {})()
    parent.char = ''
    parent.freq = left.freq + right.freq
    parent.left = left
    parent.right = right
    heap.append(parent)
    heapq.heapify(heap)
root = heap[0]

codes = {}
stack = [(root, "")]
while stack:
    node, code = stack.pop()
    if not node.left and not node.right:
        codes[node.char] = code if code != '' else '0'
    else:
        if node.right:
            stack.append((node.right, code + '1'))
        if node.left:
            stack.append((node.left, code + '0'))

output = []
for char in text:
    output.append(codes[char])
print(len(''.join(output)))