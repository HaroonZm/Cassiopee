from typing import Dict, List, Optional, Tuple
from collections import Counter
import heapq


class FrequencyAnalyzer:
    def __init__(self, data: str):
        self.data = data

    def analyze(self) -> Dict[str, int]:
        # Compute frequencies of each character
        return dict(Counter(self.data))


class HuffmanTreeNode:
    __slots__ = ('weight', 'char', 'left', 'right')

    def __init__(self, weight: int, char: Optional[str] = None,
                 left: Optional['HuffmanTreeNode'] = None,
                 right: Optional['HuffmanTreeNode'] = None):
        self.weight = weight
        self.char = char
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        return self.char is not None


class PriorityQueue:
    def __init__(self):
        self._data: List[Tuple[int, int, HuffmanTreeNode]] = []
        self._index = 0  # To avoid comparison between nodes for equal weights

    def push(self, node: HuffmanTreeNode):
        heapq.heappush(self._data, (node.weight, self._index, node))
        self._index += 1

    def pop(self) -> HuffmanTreeNode:
        return heapq.heappop(self._data)[2]

    def __len__(self):
        return len(self._data)


class HuffmanTreeBuilder:
    def __init__(self, frequencies: Dict[str, int]):
        self.frequencies = frequencies

    def build(self) -> HuffmanTreeNode:
        pq = PriorityQueue()
        # Create leaf nodes for each character
        for char, freq in self.frequencies.items():
            pq.push(HuffmanTreeNode(freq, char=char))

        # Special case: if only one character, create a dummy parent node
        if len(pq) == 1:
            only_node = pq.pop()
            dummy = HuffmanTreeNode(only_node.weight, left=only_node)
            pq.push(dummy)

        # Build tree by combining two smallest nodes until one remains
        while len(pq) > 1:
            left = pq.pop()
            right = pq.pop()
            combined_weight = left.weight + right.weight
            combined_node = HuffmanTreeNode(combined_weight, left=left, right=right)
            pq.push(combined_node)

        root = pq.pop()
        return root


class HuffmanCodeEncoder:
    def __init__(self, root: HuffmanTreeNode):
        self.root = root
        self.code_map: Dict[str, str] = {}

    def _dfs(self, node: HuffmanTreeNode, path: str):
        if node.is_leaf():
            # Assign code to character
            self.code_map[node.char] = path if path else '0'
            return
        if node.left:
            self._dfs(node.left, path + '0')
        if node.right:
            self._dfs(node.right, path + '1')

    def encode(self) -> Dict[str, str]:
        self._dfs(self.root, '')
        return self.code_map


class HuffmanCodingSystem:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.frequencies = None
        self.tree_root = None
        self.code_map = None

    def run(self) -> int:
        sa = FrequencyAnalyzer(self.sequence)
        self.frequencies = sa.analyze()

        tb = HuffmanTreeBuilder(self.frequencies)
        self.tree_root = tb.build()

        ec = HuffmanCodeEncoder(self.tree_root)
        self.code_map = ec.encode()

        # Compute total length: sum for each char freq * code length
        total_length = 0
        for c, freq in self.frequencies.items():
            code_length = len(self.code_map[c])
            total_length += freq * code_length
        return total_length


def main():
    import sys
    s = sys.stdin.readline().strip()
    hcs = HuffmanCodingSystem(s)
    result = hcs.run()
    print(result)


if __name__ == "__main__":
    main()