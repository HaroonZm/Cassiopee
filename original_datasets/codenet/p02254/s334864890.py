import heapq
from collections import Counter

class HuffmanTreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_code_helper(root, code='', codes={}):
    if not root:
        return codes
    
    if not root.left and not root.right:
        codes[root.char] = code if code else '0'
        return codes
    
    huffman_code_helper(root.left, code + '0', codes)
    huffman_code_helper(root.right, code + '1', codes)
    return codes

def huffman_code(text):
    counter = Counter(text)
    heap = []
    for char, freq in counter.items():
        heap.append(HuffmanTreeNode(char, freq))
    heapq.heapify(heap)

    while len(heap) > 1:
        left, right = heapq.heappop(heap), heapq.heappop(heap)
        node = HuffmanTreeNode('', left.freq + right.freq)
        node.left, node.right = left, right
        heapq.heappush(heap, node)
    root = heap[0]

    return huffman_code_helper(root)

def solution():
    text = input()
    codes = huffman_code(text)
    encoded = []
    for char in text:
        encoded.append(codes[char])
    print(len(''.join(encoded)))

solution()